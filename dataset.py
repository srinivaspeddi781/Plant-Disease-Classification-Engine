CLASS_NAMES = {
    0: 'Apple_Apple_scab', 1: 'Apple_Black_rot', 2: 'Apple_Cedar_apple_rust', 3: 'Apple__healthy', 
    4: 'Blueberry_healthy', 5: 'Cherry_Powdery_mildew', 6: 'Cherry_healthy', 7: 'Corn__Cercospora_leaf_spot Gray_leaf_spot', 
    8: 'Corn_Common_rust', 9: 'Corn__Northern_Leaf_Blight', 10: 'Corn_healthy', 11: 'Grape_Black_rot', 
    12: 'Grape__Esca_(Black_Measles)', 13: 'Grape__Leaf_blight_(Isariopsis_Leaf_Spot)', 14: 'Grape_healthy', 
    15: 'Orange_Haunglongbing_(Citrus_greening)', 16: 'Peach___Bacterial_spot', 17: 'Peach_healthy', 
    18: 'Pepper_bell__Bacterial_spot', 19: 'Pepper_bell_healthy', 20: 'Potato_Early_blight', 
    21: 'Potato_Late_blight', 22: 'Potato_healthy', 23: 'Raspberry__healthy', 24: 'Soybean__healthy', 
    25: 'Squash_Powdery_mildew', 26: 'Strawberry_Leaf_scorch', 27: 'Strawberry_healthy', 
    28: 'Tomato_Bacterial_spot', 29: 'Tomato_Early_blight', 30: 'Tomato__Late_blight', 31: 'Tomato_Leaf_Mold', 
    32: 'Tomato_Septoria_leaf_spot', 33: 'Tomato__Spider_mites Two-spotted_spider_mite', 
    34: 'Tomato_Target_Spot', 35: 'Tomato__Tomato_Yellow_Leaf_Curl_Virus', 36: 'Tomato__Tomato_mosaic_virus', 
    37: 'Tomato_healthy', 38: 'Cucumber_Bacterial_Wilt', 39: 'Melon_Fungal_Downy_Mildew',
    40: 'Cabbage_Black_Rot_Bacterial', 41: 'Lettuce_Fungal_Bottom_Rot'
}

def get_recommendation(class_name):
    disease_name = class_name.replace('_', ' ').replace('  ', ' ').strip()
    
    # Healthy plants
    if 'healthy' in class_name.lower():
        return (
            f"🤖 AI Analysis: The {disease_name.split(' ')[0]} plant shows no visible signs of disease.\n\n"
            f"🌱 AI Preventive Care Plan:\n"
            f"1. Watering: Maintain consistent, deep watering specific to this plant type.\n"
            f"2. Nutrition: Ensure adequate balanced fertilization during the growing season.\n"
            f"3. Monitoring: Continue regular inspections for early signs of pests or environmental stress."
        )

    # Specific AI generated recommendations
    ai_response = f"🤖 AI Diagnosis: Detected features consistent with **{disease_name}**.\n\n"
    ai_response += "🔬 AI Recommended Treatment Plan:\n"
    
    if class_name == 'Apple_Apple_scab':
        ai_response += "1. Fungicide: Apply fungicides containing captan, myclobutanil, or sulfur.\n2. Hygiene: Rake and destroy fallen leaves to reduce the source of infection.\n3. Pruning: Prune trees to open the canopy for better air circulation and faster drying."
    elif class_name == 'Apple_Black_rot':
        ai_response += "1. Pruning: Prune out and destroy all dead, diseased, or cankered wood.\n2. Fungicide: Apply protectant fungicides like captan.\n3. Sanitation: Remove mummified fruit from trees to prevent the spread."
    elif class_name == 'Corn_Common_rust':
        ai_response += "1. Chemical Control: Apply fungicides containing azoxystrobin or propiconazole early in the disease cycle.\n2. Seed Selection: Plant rust-resistant corn hybrids in the next season.\n3. Scouting: Regularly monitor fields during cool, moist conditions."
    elif class_name == 'Potato_Early_blight':
        ai_response += "1. Crop Rotation: Rotate to non-solanaceous crops for at least 2 years.\n2. Fungicide: Apply chlorothalonil or mancozeb as preventative sprays.\n3. Irrigation: Avoid overhead irrigation; water at the base to keep foliage dry."
    elif class_name == 'Tomato_Bacterial_spot':
        ai_response += "1. Chemical Control: Apply copper-based bactericides combined with mancozeb.\n2. Cultural Practices: Avoid working in wet foliage and avoid overhead watering.\n3. Sanitation: Remove deeply infected plants and practice strict weed control."
    elif class_name == 'Tomato_Late_blight':
        ai_response += "1. Urgent Action: Apply effective systemic or protectant fungicides (e.g., chlorothalonil) immediately.\n2. Plant Destruction: Remove and destroy severely infected plants to halt rapid spread.\n3. Environment: Ensure excellent air circulation and avoid prolonged leaf wetness."
    elif class_name == 'Grape_Black_rot':
        ai_response += "1. Sanitation: Remove mummified berries and infected canes during dormant pruning.\n2. Fungicides: Use an aggressive fungicide program from early spring through mid-summer.\n3. Canopy Management: Maximize airflow through shoot positioning and leaf removal."
    elif class_name == 'Cucumber_Bacterial_Wilt':
        ai_response += "1. Pest Control: Control striped and spotted cucumber beetles early, as they transmit this bacteria.\n2. Removal: Immediately remove and destroy wilted vines to prevent spread.\n3. Row Covers: Use floating row covers to physically exclude beetles until flowering."
    elif class_name == 'Melon_Fungal_Downy_Mildew':
        ai_response += "1. Fungicide: Apply protectant fungicides such as chlorothalonil or mancozeb before symptoms appear.\n2. Airflow: Maximize plant spacing to ensure rapid drying of leaves after rain or dew.\n3. Irrigation: Avoid overhead watering; use drip irrigation to keep foliage dry."
    elif class_name == 'Cabbage_Black_Rot_Bacterial':
        ai_response += "1. Seed Selection: Use certified disease-free or hot-water treated seeds.\n2. Crop Rotation: Rotate with non-cruciferous crops for at least 3 years.\n3. Weed Control: Eradicate wild mustard and other cruciferous weeds that harbor the bacteria."
    elif class_name == 'Lettuce_Fungal_Bottom_Rot':
        ai_response += "1. Soil Drainage: Ensure beds are well-drained and avoid planting in low-lying, wet areas.\n2. Fungicide: Apply targeted soil-directed fungicides (e.g., iprodione) shortly after thinning or transplanting.\n3. Debris Management: Deeply plow crop residues immediately after harvest to speed decomposition."
    else:
        ai_response += f"1. Isolation: Isolate the affected plant to prevent potential spread of {disease_name}.\n2. Symptom Management: Remove heavily infected leaves to reduce disease pressure.\n3. Expert Consultation: Consult a local agricultural extension office or a plant pathology expert for a targeted treatment plan."

    ai_response += "\n\n⚠️ Disclaimer: AI suggestions are for informational purposes. Always follow product labels and local regulations when applying treatments."
    return ai_response
