#!/usr/bin/env python3
"""
Script to generate test images with random EXIF dates
"""

import os
import random
from datetime import datetime, timedelta
from PIL import Image, ImageDraw
from PIL.ExifTags import TAGS
import piexif

def generate_random_date():
    """Generate a random date between 2020 and 2024"""
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    # Generate a random date
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    random_date = start_date + timedelta(days=random_days)
    
    # Add a random time
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    return random_date.replace(hour=random_hour, minute=random_minute, second=random_second)

def create_test_image(filename, date, size=(800, 600)):
    """Create a test image with a specific EXIF date"""
    
    # Create a simple colored image
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan']
    color = random.choice(colors)
    
    # Create the image
    img = Image.new('RGB', size, color=color)
    draw = ImageDraw.Draw(img)
    
    # Add text with the date
    text = f"Image de test\n{date.strftime('%d/%m/%Y %H:%M')}"
    draw.text((50, 50), text, fill='white')
    
    # Create EXIF data
    date_str = date.strftime("%Y:%m:%d %H:%M:%S")
    
    exif_dict = {
        "0th": {
            piexif.ImageIFD.Make: "TestCamera",
            piexif.ImageIFD.Model: "TestModel",
            piexif.ImageIFD.DateTime: date_str,
            piexif.ImageIFD.Software: "PhotoGenerator"
        },
        "Exif": {
            piexif.ExifIFD.DateTimeOriginal: date_str,
            piexif.ExifIFD.DateTimeDigitized: date_str,
        },
        "GPS": {},
        "1st": {},
        "thumbnail": None
    }
    
    # Convert to EXIF bytes
    exif_bytes = piexif.dump(exif_dict)
    
    # Save image with EXIF data
    img.save(filename, "JPEG", exif=exif_bytes, quality=85)
    print(f"Created: {os.path.basename(filename)} - {date.strftime('%B %Y')}")

def main():
    # Destination folder
    test_folder = "/mnt/d/PhotoTransfer/photos_test"
    
    # Create subfolders to simulate a real structure
    subfolders = [
        "",  # Root
        "Vacances",
        "Famille", 
        "Vacances/Ete_2023",
        "Travail"
    ]
    
    for subfolder in subfolders:
        full_path = os.path.join(test_folder, subfolder)
        os.makedirs(full_path, exist_ok=True)
    
    # Generate 30 images with random dates
    for i in range(1, 31):
        # Choose a subfolder randomly
        subfolder = random.choice(subfolders)
        
        # Generate a random date
        random_date = generate_random_date()
        
        # Filename
        filename = f"IMG_{i:04d}.jpg"
        full_path = os.path.join(test_folder, subfolder, filename)
        
        # Create the image
        create_test_image(full_path, random_date)
    
    print(f"\n30 test images created in {test_folder}")
    print("You can now test your photo organizer!")

if __name__ == "__main__":
    main()