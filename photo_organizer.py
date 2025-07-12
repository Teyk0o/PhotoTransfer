#!/usr/bin/env python3
"""
Organisateur de Photos - Version 2.0
Application moderne et simple pour trier automatiquement vos photos par date
Interface pensée pour les utilisateurs non-techniques
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import shutil
from datetime import datetime
from pathlib import Path
import threading
import json
import hashlib
from PIL import Image
from PIL.ExifTags import TAGS

# Dictionnaire des noms de mois en français
MOIS_FRANCAIS = {
    1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril",
    5: "Mai", 6: "Juin", 7: "Juillet", 8: "Août",
    9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"
}

class PhotoOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("📸 Organisateur de Photos - Simple et Efficace")
        self.root.geometry("700x800")
        self.root.resizable(True, True)
        
        # Fichier de configuration
        self.config_file = "photo_organizer_config.json"
        
        self.source_folder = tk.StringVar()
        self.dest_folder = tk.StringVar()
        
        # Options de traitement
        self.sort_by_date = tk.BooleanVar(value=True)
        self.copy_mode = tk.BooleanVar(value=True)
        
        # Charger la configuration sauvegardée
        self.load_config()
        
        # Configuration du style moderne
        self.setup_style()
        self.setup_ui()
        
        # Sauvegarder la config à la fermeture
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_style(self):
        """Configure un style moderne pour l'interface"""
        style = ttk.Style()
        
        # Couleurs modernes
        style.configure('Title.TLabel', font=('Segoe UI', 18, 'bold'), foreground='#2c3e50')
        style.configure('Heading.TLabel', font=('Segoe UI', 12, 'bold'), foreground='#34495e')
        style.configure('Info.TLabel', font=('Segoe UI', 10), foreground='#7f8c8d')
        style.configure('Modern.TButton', font=('Segoe UI', 10, 'bold'), padding=10)
        style.configure('Action.TButton', font=('Segoe UI', 14, 'bold'), padding=15)
        
        # Style pour les frames
        style.configure('Card.TFrame', relief='solid', borderwidth=1)
        
    def load_config(self):
        """Charge la configuration sauvegardée"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.source_folder.set(config.get('source_folder', ''))
                    self.dest_folder.set(config.get('dest_folder', ''))
                    self.sort_by_date.set(config.get('sort_by_date', True))
                    self.copy_mode.set(config.get('copy_mode', True))
        except Exception as e:
            print(f"Erreur lors du chargement de la configuration: {e}")
    
    def save_config(self):
        """Sauvegarde la configuration actuelle"""
        try:
            config = {
                'source_folder': self.source_folder.get(),
                'dest_folder': self.dest_folder.get(),
                'sort_by_date': self.sort_by_date.get(),
                'copy_mode': self.copy_mode.get()
            }
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la configuration: {e}")
    
    def on_closing(self):
        """Appelé lors de la fermeture de l'application"""
        self.save_config()
        self.root.destroy()
        
    def setup_ui(self):
        # Conteneur principal avec padding généreux
        main_container = ttk.Frame(self.root, padding="20")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuration du redimensionnement
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        # Pas de zone extensible, taille fixe optimisée
        
        # === TITRE PRINCIPAL ===
        title_frame = ttk.Frame(main_container)
        title_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        title_frame.columnconfigure(0, weight=1)
        
        ttk.Label(title_frame, text="📸 Organisateur de Photos", 
                 style='Title.TLabel').grid(row=0, column=0)
        ttk.Label(title_frame, text="Triez automatiquement vos photos par date en quelques clics", 
                 style='Info.TLabel').grid(row=1, column=0, pady=(5, 0))
        
        # === SECTION DOSSIERS ===
        folders_frame = ttk.LabelFrame(main_container, text=" 📁 Sélection des dossiers ", 
                                      padding="15", style='Card.TFrame')
        folders_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        folders_frame.columnconfigure(1, weight=1)
        
        # Dossier source
        ttk.Label(folders_frame, text="🔍 Dossier contenant vos photos:", 
                 style='Heading.TLabel').grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        ttk.Label(folders_frame, text="(Toutes les photos seront trouvées automatiquement, même dans les sous-dossiers)", 
                 style='Info.TLabel').grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=(0, 10))
        
        source_entry = ttk.Entry(folders_frame, textvariable=self.source_folder, font=('Segoe UI', 10))
        source_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=(0, 10))
        ttk.Button(folders_frame, text="📂 Choisir", command=self.select_source_folder, 
                  style='Modern.TButton').grid(row=2, column=2)
        
        # Séparateur visuel
        ttk.Separator(folders_frame, orient='horizontal').grid(row=3, column=0, columnspan=3, 
                                                              sticky=(tk.W, tk.E), pady=15)
        
        # Dossier destination
        ttk.Label(folders_frame, text="💾 Dossier où sauvegarder les photos triées:", 
                 style='Heading.TLabel').grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        ttk.Label(folders_frame, text="(Les photos seront organisées par année puis par mois)", 
                 style='Info.TLabel').grid(row=5, column=0, columnspan=3, sticky=tk.W, pady=(0, 10))
        
        dest_entry = ttk.Entry(folders_frame, textvariable=self.dest_folder, font=('Segoe UI', 10))
        dest_entry.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=(0, 10))
        ttk.Button(folders_frame, text="📂 Choisir", command=self.select_dest_folder, 
                  style='Modern.TButton').grid(row=6, column=2)
        
        # === SECTION OPTIONS ===
        options_frame = ttk.LabelFrame(main_container, text=" ⚙️ Options de traitement ", 
                                      padding="15", style='Card.TFrame')
        options_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Option tri par date avec explication claire
        sort_frame = ttk.Frame(options_frame)
        sort_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.sort_checkbox = ttk.Checkbutton(sort_frame, text="📅 Trier les photos par date", 
                                           variable=self.sort_by_date, 
                                           command=self.on_sort_option_changed)
        self.sort_checkbox.grid(row=0, column=0, sticky=tk.W)
        
        self.sort_info = ttk.Label(sort_frame, text="", style='Info.TLabel', wraplength=600)
        self.sort_info.grid(row=1, column=0, sticky=tk.W, padx=(25, 0), pady=(5, 0))
        
        # Option copie/déplacement avec explication claire  
        copy_frame = ttk.Frame(options_frame)
        copy_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        self.copy_checkbox = ttk.Checkbutton(copy_frame, text="📋 Conserver les photos originales", 
                                           variable=self.copy_mode,
                                           command=self.on_copy_option_changed)
        self.copy_checkbox.grid(row=0, column=0, sticky=tk.W)
        
        self.copy_info = ttk.Label(copy_frame, text="", style='Info.TLabel', wraplength=600)
        self.copy_info.grid(row=1, column=0, sticky=tk.W, padx=(25, 0), pady=(5, 0))
        
        # Mise à jour initiale des textes d'aide
        self.on_sort_option_changed()
        self.on_copy_option_changed()
        
        # === BOUTON PRINCIPAL ===
        action_frame = ttk.Frame(main_container)
        action_frame.grid(row=3, column=0, pady=15, sticky=tk.W+tk.E)
        action_frame.columnconfigure(0, weight=1)
        
        self.start_button = ttk.Button(action_frame, text="🚀 ORGANISER MES PHOTOS", 
                                      command=self.start_organizing, style='Action.TButton')
        self.start_button.grid(row=0, column=0)
        
        # === ZONE DE PROGRESSION ===
        progress_frame = ttk.Frame(main_container)
        progress_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(15, 20))
        progress_frame.columnconfigure(0, weight=1)
        
        # Barre de progression
        self.progress = ttk.Progressbar(progress_frame, mode='determinate', style='TProgressbar')
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Label de statut simple
        self.status_label = ttk.Label(progress_frame, text="✨ Prêt à organiser vos photos !", 
                                     style='Info.TLabel', anchor='center')
        self.status_label.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
    def on_sort_option_changed(self):
        """Met à jour le texte d'aide pour l'option de tri"""
        if self.sort_by_date.get():
            text = "✓ Créera des dossiers par année (ex: 2023, 2024) puis par mois (ex: Janvier, Février)"
        else:
            text = "○ Toutes les photos seront placées directement dans le dossier de destination"
        self.sort_info.config(text=text)
        
    def on_copy_option_changed(self):
        """Met à jour le texte d'aide pour l'option de copie"""
        if self.copy_mode.get():
            text = "✓ Les photos originales restent dans leur dossier actuel (recommandé pour la sécurité)"
        else:
            text = "○ Les photos seront déplacées (supprimées de leur emplacement actuel)"
        self.copy_info.config(text=text)
        
    def select_source_folder(self):
        folder = filedialog.askdirectory(title="Choisir le dossier contenant vos photos")
        if folder:
            self.source_folder.set(folder)
            self.save_config()  # Sauvegarde immédiate
            self.update_status(f"📁 Dossier source sélectionné")
            
    def select_dest_folder(self):
        folder = filedialog.askdirectory(title="Choisir le dossier de destination")
        if folder:
            self.dest_folder.set(folder)
            self.save_config()  # Sauvegarde immédiate
            self.update_status(f"💾 Dossier de destination sélectionné")
    
    def update_status(self, message):
        """Met à jour le message de statut"""
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def get_photo_date(self, filepath):
        """Extrait la date de prise de vue depuis les métadonnées EXIF"""
        try:
            with Image.open(filepath) as image:
                exifdata = image.getexif()
                
                # Recherche de la date de prise de vue
                for tag_id in exifdata:
                    tag = TAGS.get(tag_id, tag_id)
                    data = exifdata.get(tag_id)
                    
                    if tag in ["DateTime", "DateTimeOriginal", "DateTimeDigitized"]:
                        try:
                            return datetime.strptime(data, "%Y:%m:%d %H:%M:%S")
                        except:
                            continue
        except Exception as e:
            pass  # Erreurs EXIF silencieuses pour les utilisateurs non-techniques
        
        # Si pas de données EXIF, utiliser la date de modification du fichier
        try:
            return datetime.fromtimestamp(os.path.getmtime(filepath))
        except:
            return datetime.now()
    
    def get_year_month_path(self, date):
        """Génère le chemin des dossiers au format 'Année/Mois'"""
        try:
            month_name = MOIS_FRANCAIS[date.month]
            year = date.strftime("%Y")
            return os.path.join(year, month_name)
        except:
            return os.path.join(str(datetime.now().year), "Inconnu")
    
    def files_are_identical(self, file1_path, file2_path):
        """Vérifie si deux fichiers sont identiques (même taille et même contenu)"""
        try:
            # Vérification rapide par la taille
            if os.path.getsize(file1_path) != os.path.getsize(file2_path):
                return False
            
            # Si même taille, vérification par hash (plus fiable)
            def get_file_hash(filepath):
                hash_md5 = hashlib.md5()
                with open(filepath, "rb") as f:
                    # Lire par chunks pour les gros fichiers
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
                return hash_md5.hexdigest()
            
            return get_file_hash(file1_path) == get_file_hash(file2_path)
        except:
            return False
    
    def organize_photos(self):
        """Organise les photos par date"""
        source = self.source_folder.get()
        destination = self.dest_folder.get()
        
        if not source or not destination:
            messagebox.showerror("❌ Erreur", "Veuillez sélectionner les dossiers source et destination")
            return
        
        if not os.path.exists(source):
            messagebox.showerror("❌ Erreur", "Le dossier source n'existe pas")
            return
        
        # Désactiver le bouton pendant le traitement
        self.start_button.config(state='disabled', text="⏳ Traitement en cours...")
        
        # Extensions de fichiers photos supportées
        photo_extensions = {'.jpg', '.jpeg', '.png', '.tiff', '.tif', '.bmp', '.gif', '.raw', '.cr2', '.nef', '.arw', '.heic', '.webp'}
        
        # Collecte de tous les fichiers photos
        self.update_status("🔍 Recherche des photos...")
        photo_files = []
        for root, dirs, files in os.walk(source):
            for file in files:
                if Path(file).suffix.lower() in photo_extensions:
                    photo_files.append(os.path.join(root, file))
        
        total_files = len(photo_files)
        if total_files == 0:
            messagebox.showinfo("ℹ️ Information", "Aucune photo trouvée dans le dossier source")
            self.start_button.config(state='normal', text="🚀 ORGANISER MES PHOTOS")
            return
        
        # Mise à jour du statut
        self.update_status(f"📊 {total_files} photos trouvées - Traitement en cours...")
        self.progress['maximum'] = total_files
        
        processed = 0
        errors = 0
        skipped_duplicates = 0
        
        for i, photo_path in enumerate(photo_files):
            try:
                filename = os.path.basename(photo_path)
                
                # Déterminer le dossier de destination selon l'option de tri
                if self.sort_by_date.get():
                    # Obtenir la date de la photo et créer le dossier par date
                    photo_date = self.get_photo_date(photo_path)
                    year_month_path = self.get_year_month_path(photo_date)
                    dest_folder_path = os.path.join(destination, year_month_path)
                    dest_info = f"{filename} → {year_month_path.replace(os.sep, '/')}"
                else:
                    # Pas de tri, directement dans le dossier de destination
                    dest_folder_path = destination
                    dest_info = f"{filename} → dossier destination"
                
                # Créer le dossier s'il n'existe pas
                os.makedirs(dest_folder_path, exist_ok=True)
                
                # Nom du fichier de destination
                dest_file_path = os.path.join(dest_folder_path, filename)
                
                # Vérifier si le fichier existe déjà
                if os.path.exists(dest_file_path):
                    # Vérifier si c'est exactement le même fichier
                    if self.files_are_identical(photo_path, dest_file_path):
                        # Fichier identique déjà présent, on l'ignore
                        skipped_duplicates += 1
                        if (processed + skipped_duplicates) % 10 == 0:
                            self.update_status(f"📸 Traitement... {processed + skipped_duplicates}/{total_files} photos")
                        continue
                    else:
                        # Fichier différent avec même nom, on ajoute un numéro
                        counter = 1
                        original_dest_path = dest_file_path
                        while os.path.exists(dest_file_path):
                            name, ext = os.path.splitext(original_dest_path)
                            dest_file_path = f"{name}_{counter}{ext}"
                            counter += 1
                
                # Copier ou déplacer selon l'option choisie
                if self.copy_mode.get():
                    shutil.copy2(photo_path, dest_file_path)
                    action = "📋"
                else:
                    shutil.move(photo_path, dest_file_path)
                    action = "📦"
                
                # Mise à jour du statut occasionnelle
                if (processed + skipped_duplicates) % 10 == 0:  # Toutes les 10 photos
                    self.update_status(f"📸 Traitement... {processed + skipped_duplicates}/{total_files} photos")
                processed += 1
                
            except Exception as e:
                errors += 1
                # Erreurs silencieuses pour simplicité
            
            # Mise à jour de la barre de progression
            self.progress['value'] = i + 1
            self.root.update_idletasks()
        
        # Statut final
        if errors == 0 and skipped_duplicates == 0:
            self.update_status(f"🎉 Terminé ! {processed} photos organisées avec succès")
        elif skipped_duplicates > 0 and errors == 0:
            self.update_status(f"✅ Terminé ! {processed} nouvelles photos, {skipped_duplicates} doublons ignorés")
        else:
            self.update_status(f"✅ Terminé ! {processed} photos traitées, {skipped_duplicates} doublons ignorés, {errors} erreurs")
        
        # Réactiver le bouton
        self.start_button.config(state='normal', text="🚀 ORGANISER MES PHOTOS")
        
        # Notification finale
        message_parts = []
        if processed > 0:
            message_parts.append(f"✅ {processed} photos organisées")
        if skipped_duplicates > 0:
            message_parts.append(f"🔄 {skipped_duplicates} doublons ignorés")
        if errors > 0:
            message_parts.append(f"⚠️ {errors} erreurs")
            
        if errors == 0:
            messagebox.showinfo("🎉 Succès", f"Organisation terminée !\n\n{chr(10).join(message_parts)}\n\n📁 Vos photos sont dans: {destination}")
        else:
            messagebox.showwarning("⚠️ Terminé avec avertissements", f"Organisation terminée !\n\n{chr(10).join(message_parts)}")
    
    def start_organizing(self):
        """Lance l'organisation dans un thread séparé"""
        # Sauvegarder la config avant de commencer
        self.save_config()
        threading.Thread(target=self.organize_photos, daemon=True).start()

def main():
    root = tk.Tk()
    app = PhotoOrganizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()