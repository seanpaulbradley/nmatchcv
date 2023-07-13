import os
import pandas as pd
import requests
from pathlib import Path

# Save in github clone directory for nmatchv for current user
documents_dir = os.path.join(os.path.expanduser('~'), 'Documents') 
save_dir = os.path.join(documents_dir, 'github/nmatchcv')
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
os.chdir(save_dir)

# Read in tsv w/ image urls + unique IDs
df = pd.read_csv('things_concepts.tsv', sep='\t')

# Iterate through rows of tsv, saving images in subfolders w/ unique ID names
for index, row in df.iterrows():
    url = row['Example image']
    unique_id = row['uniqueID']

    # Create subfolder for each image class
    folder = Path('example_images') / unique_id
    folder.mkdir(parents=True, exist_ok=True)

    # Download image...since only 1 is expected, we'll just name it img1.jpeg directly
    response = requests.get(url)
    image_path = folder / 'img1.jpeg'
    with open(image_path, 'wb') as f:
        f.write(response.content)