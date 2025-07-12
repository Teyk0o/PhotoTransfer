#!/usr/bin/env python3
"""
Script pour générer des images de test avec des dates EXIF aléatoires
"""

import os
import random
from datetime import datetime, timedelta
from PIL import Image, ImageDraw
from PIL.ExifTags import TAGS
import piexif

def generate_random_date():
    """Génère une date aléatoire entre 2020 et 2024"""
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    # Générer une date aléatoire
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    random_date = start_date + timedelta(days=random_days)
    
    # Ajouter une heure aléatoire
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    return random_date.replace(hour=random_hour, minute=random_minute, second=random_second)

def create_test_image(filename, date, size=(800, 600)):
    """Crée une image de test avec une date EXIF spécifique"""
    
    # Créer une image colorée simple
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan']
    color = random.choice(colors)
    
    # Créer l'image
    img = Image.new('RGB', size, color=color)
    draw = ImageDraw.Draw(img)
    
    # Ajouter du texte avec la date
    text = f"Image de test\n{date.strftime('%d/%m/%Y %H:%M')}"
    draw.text((50, 50), text, fill='white')
    
    # Créer les données EXIF
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
    
    # Convertir en bytes EXIF
    exif_bytes = piexif.dump(exif_dict)
    
    # Sauvegarder l'image avec les données EXIF
    img.save(filename, "JPEG", exif=exif_bytes, quality=85)
    print(f"Créé: {os.path.basename(filename)} - {date.strftime('%B %Y')}")

def main():
    # Dossier de destination
    test_folder = "/mnt/d/PhotoTransfer/photos_test"
    
    # Créer des sous-dossiers pour simuler une vraie structure
    subfolders = [
        "",  # Racine
        "Vacances",
        "Famille", 
        "Vacances/Ete_2023",
        "Travail"
    ]
    
    for subfolder in subfolders:
        full_path = os.path.join(test_folder, subfolder)
        os.makedirs(full_path, exist_ok=True)
    
    # Générer 30 images avec des dates aléatoires
    for i in range(1, 31):
        # Choisir un sous-dossier aléatoirement
        subfolder = random.choice(subfolders)
        
        # Générer une date aléatoire
        random_date = generate_random_date()
        
        # Nom de fichier
        filename = f"IMG_{i:04d}.jpg"
        full_path = os.path.join(test_folder, subfolder, filename)
        
        # Créer l'image
        create_test_image(full_path, random_date)
    
    print(f"\n30 images de test créées dans {test_folder}")
    print("Vous pouvez maintenant tester votre organisateur de photos !")

if __name__ == "__main__":
    main()