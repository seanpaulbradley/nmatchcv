import os
import pandas as pd
import requests
from pathlib import Path

# Get user Documents directory
documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')

# Set save directory 
save_dir = os.path.join(documents_dir, 'github/nmatchcv')

# Create save directory if doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir) 

# Download TSV file
tsv_url = 'https://osf.io/download/xtafs'
tsv_path = os.path.join(save_dir, 'things_concepts.tsv')


# Set working directory 
os.chdir(save_dir)

# Download TSV file w/ image URLs and unique IDs in it
response = requests.get(tsv_url, stream=True)
with open(tsv_path, 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk: 
            f.write(chunk)
response.raise_for_status()


# Read downloaded TSV
df = pd.read_csv(tsv_path, sep='\t')

for index, row in df.iterrows():
    url = row['Example image'] + '.jpeg'
    unique_id = row['uniqueID']
    
    # Create subfolder
    folder = Path('example_images') / unique_id
    folder.mkdir(parents=True, exist_ok=True)

    # Download image
    response = requests.get(url)
    image_path = folder / 'img1.jpeg'
    with open(image_path, 'wb') as f:
        f.write(response.content)
