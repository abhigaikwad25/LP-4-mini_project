


# # Path of file : C:/Users/user/Desktop/Mini-Project-LP-3/mini_project_csdf/demo.jpg



import os
import hashlib
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_hash(image_path):
    """Generate SHA-256 hash of the image."""
    hasher = hashlib.sha256()
    with open(image_path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def extract_metadata(image_path):
    """Extract important metadata from the image."""
    with Image.open(image_path) as img:
        metadata = {
            'Filename': os.path.basename(image_path),
            'Image Size': img.size,
            'Format': img.format,
            'Mode': img.mode,
            'Color Space': img.info.get('color_space', 'N/A'),
            'Compression': img.info.get('compression', 'N/A'),
            'Orientation': img.info.get('orientation', 'N/A'),
            'Software': img.info.get('software', 'N/A'),
            'DateTimeOriginal': img.info.get('date_time_original', 'N/A'),
            'GPSInfo': img._getexif().get(34853, 'N/A') if img._getexif() else 'N/A',  # GPSInfo tag
        }
        
        # Extract EXIF data
        exif_data = img._getexif()
        if exif_data is not None:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                # Only keep relevant EXIF data
                if tag in ['Make', 'Model', 'DateTime', 'ExposureTime', 'FNumber', 'ISOSpeedRatings', 
                            'FocalLength', 'MeteringMode', 'Flash', 'WhiteBalance', 'ExposureBias']:
                    metadata[tag] = value
        
        return metadata

if __name__ == '__main__':
    # Get the current working directory
    current_dir = os.getcwd()
    print(f'Current Working Directory: {current_dir}')
    
    # Prompt for the image path
    image_path = input('Enter the path of the image to analyze: ')
    
    # Generate image hash
    image_hash = get_image_hash(image_path)
    print(f'Image Hash (SHA-256): {image_hash}')
    
    # Extract and display important metadata
    important_metadata = extract_metadata(image_path)
    print('\nExtracted Important Metadata:')
    for key, value in important_metadata.items():
        print(f'{key}: {value}')
