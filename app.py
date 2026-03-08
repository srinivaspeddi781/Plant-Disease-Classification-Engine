import os
from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TF logging warnings

try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False
    print("Warning: TensorFlow is not installed. Please run 'pip install tensorflow' to enable dynamic predictions.")

app = Flask(__name__)
# Configure upload folder
UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB max upload size

from dataset import CLASS_NAMES, get_recommendation

import tensorflow as tf

# Create global graph and session variables
global graph, sess
graph = tf.compat.v1.get_default_graph()
sess = tf.compat.v1.Session()

MODEL_PATH = 'mobilenetv2_best.keras'
model = None

if TF_AVAILABLE:
    try:
        with graph.as_default(), sess.as_default():
            if os.path.exists(MODEL_PATH):
                model = load_model(MODEL_PATH)
                # Pre-warm model to lock graph
                try:
                    model.predict(np.zeros((1, 224, 224, 3)))
                except Exception:
                    pass
                print(f"Model '{MODEL_PATH}' loaded successfully.")
            else:
                print(f"Warning: Model '{MODEL_PATH}' not found in the project root folder.")
    except Exception as e:
        print(f"Error loading model: {e}")

def model_predict(image_path):
    if not TF_AVAILABLE:
        return "Error: TensorFlow is not installed. Please install it using 'pip install tensorflow' to run dynamic AI predictions."
        
    if model is None:
        return f"Error: The prediction model '{MODEL_PATH}' was not found. Please upload your trained model to the project root folder."
    
    try:
        # Load and preprocess image dynamically
        try:
            img = load_img(image_path, target_size=(224, 224))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = x / 255.0  # Rescale exactly as in training
        except Exception as img_e:
            return f"Error loading or processing the image: {str(img_e)}"
        
        # Run real-time machine learning inference
        # In Flask threaded context, we must use the graph that the model was loaded to
        with graph.as_default(), sess.as_default():
            preds = model.predict(x)
            predicted_class_index = int(np.argmax(preds, axis=1)[0])
            confidence = float(np.max(preds))
        
        predicted_class_name = CLASS_NAMES[predicted_class_index]
        
        # Clean up class name for display
        display_name = predicted_class_name.replace('_', ' ').strip()
        
        recommendation = get_recommendation(predicted_class_name)
        
        return {
            'class': display_name,
            'confidence': f"{confidence * 100:.2f}%",
            'recommendation': recommendation
        }
    except Exception as e:
        return f"Error during model inference: {str(e)}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Predict
        result = model_predict(filepath)
        
        if isinstance(result, str) and result.startswith("Error"):
            return jsonify({'error': result}), 500
            
        # Get path for web browser to render image
        image_url = url_for('static', filename=f'uploads/{filename}')
        
        # Pass result to template
        return render_template('result.html', result=result, image_url=image_url)

if __name__ == '__main__':
    # Try creating static folder inside uploads just to be safe if moved
    app.run(debug=True, port=5000)
