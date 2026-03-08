import os
import time
import requests
import itertools
from duckduckgo_search import DDGS
from dataset import CLASS_NAMES

output_dir = "images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Clear old synthetic images
for f in os.listdir(output_dir):
    if f.endswith('.jpg') or f.endswith('.png'):
        os.remove(os.path.join(output_dir, f))

print(f"Downloading real plant leaf images for {len(CLASS_NAMES)} classes...")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

count = 0
try:
    with DDGS() as ddgs:
        for idx, class_name in CLASS_NAMES.items():
            query_name = class_name.replace('_', ' ').replace('  ', ' ')
            
            if 'healthy' in class_name.lower():
                search_query = f"{query_name.replace('healthy', '').strip()} healthy leaf photograph macro"
            else:
                search_query = f"{query_name} leaf disease photograph macro"
                
            print(f"[{count}/100] Searching for: {search_query}")
            
            try:
                # Use itertools.islice for max_results in newer duckduckgo-search versions
                results_gen = ddgs.images(search_query)
                results = list(itertools.islice(results_gen, 3))
                
                if not results:
                    continue
                    
                for i, res in enumerate(results):
                    img_url = res.get('image')
                    if not img_url: continue
                    
                    try:
                        response = requests.get(img_url, headers=headers, timeout=5)
                        if response.status_code == 200:
                            ext = img_url.split('.')[-1][:4] # simple extension guess
                            if ext.lower() not in ['jpg', 'jpeg', 'png', 'webp']:
                                ext = 'jpg'
                                
                            clean_name = class_name.replace('__', '_').replace(' ', '_').replace('(', '').replace(')', '')
                            filename = os.path.join(output_dir, f"{clean_name}_{i+1}.{ext}")
                            
                            with open(filename, 'wb') as f:
                                f.write(response.content)
                            count += 1
                    except Exception as e:
                        pass # Ignore download failures
            except Exception as e:
                pass # Ignore search failures
            
            time.sleep(1) # Prevent rate limiting
            if count >= 105:
                print("Successfully downloaded over 100 real images! Stopping.")
                break

except Exception as e:
    print(f"Critial error during search: {e}")

print(f"Finished downloading {count} real leaf images into '{output_dir}'.")
