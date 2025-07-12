#!/usr/bin/env python3
"""
Photo Organizer - Version 2.0
Modern and simple application to automatically sort your photos by date
Interface designed for non-technical users
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

# Translation dictionaries
TRANSLATIONS = {
    'en': {
        # Months
        'months': {
            1: "January", 2: "February", 3: "March", 4: "April",
            5: "May", 6: "June", 7: "July", 8: "August", 
            9: "September", 10: "October", 11: "November", 12: "December"
        },
        # Interface
        'app_title': "📸 Photo Organizer - Simple and Efficient",
        'app_subtitle': "Sort your photos automatically by date in just a few clicks",
        'folders_section': " 📁 Folder Selection ",
        'source_label': "🔍 Folder containing your photos:",
        'source_help': "(All photos will be found automatically, even in subfolders)",
        'dest_label': "💾 Folder to save sorted photos:",
        'dest_help': "(Photos will be organized by year then by month)",
        'choose_button': "📂 Choose",
        'options_section': " ⚙️ Processing Options ",
        'sort_option': "📅 Sort photos by date",
        'sort_help_on': "✓ Will create folders by year (e.g.: 2023, 2024) then by month (e.g.: January, February)",
        'sort_help_off': "○ All photos will be placed directly in the destination folder",
        'copy_option': "📋 Keep original photos",
        'copy_help_on': "✓ Original photos remain in their current folder (recommended for safety)",
        'copy_help_off': "○ Photos will be moved (deleted from their current location)",
        'organize_button': "🚀 ORGANIZE MY PHOTOS",
        'organize_processing': "⏳ Processing...",
        'language_label': "🌍 Language:",
        # Status
        'status_ready': "✨ Ready to organize your photos!",
        'status_source_selected': "📁 Source folder selected",
        'status_dest_selected': "💾 Destination folder selected",
        'status_searching': "🔍 Searching for photos...",
        'status_found': "📊 {} photos found - Processing...",
        'status_processing': "📸 Processing... {}/{} photos",
        'status_done_success': "🎉 Done! {} photos organized successfully",
        'status_done_duplicates': "✅ Done! {} new photos, {} duplicates ignored",
        'status_done_errors': "✅ Done! {} photos processed, {} duplicates ignored, {} errors",
        # Messages
        'error_folders': "Please select source and destination folders",
        'error_source_missing': "Source folder does not exist",
        'info_no_photos': "No photos found in source folder",
        'success_title': "🎉 Success",
        'success_message': "Organization completed!\n\n{}\n\n📁 Your photos are in: {}",
        'warning_title': "⚠️ Completed with warnings", 
        'warning_message': "Organization completed!\n\n{}",
        'photos_organized': "✅ {} photos organized",
        'duplicates_ignored': "🔄 {} duplicates ignored",
        'errors_found': "⚠️ {} errors",
        # Dialogs
        'choose_source_title': "Choose folder containing your photos",
        'choose_dest_title': "Choose destination folder",
        'unknown_folder': "Unknown"
    },
    'fr': {
        # Months
        'months': {
            1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril",
            5: "Mai", 6: "Juin", 7: "Juillet", 8: "Août",
            9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"
        },
        # Interface
        'app_title': "📸 Organisateur de Photos - Simple et Efficace",
        'app_subtitle': "Triez automatiquement vos photos par date en quelques clics",
        'folders_section': " 📁 Sélection des dossiers ",
        'source_label': "🔍 Dossier contenant vos photos:",
        'source_help': "(Toutes les photos seront trouvées automatiquement, même dans les sous-dossiers)",
        'dest_label': "💾 Dossier où sauvegarder les photos triées:",
        'dest_help': "(Les photos seront organisées par année puis par mois)",
        'choose_button': "📂 Choisir",
        'options_section': " ⚙️ Options de traitement ",
        'sort_option': "📅 Trier les photos par date",
        'sort_help_on': "✓ Créera des dossiers par année (ex: 2023, 2024) puis par mois (ex: Janvier, Février)",
        'sort_help_off': "○ Toutes les photos seront placées directement dans le dossier de destination",
        'copy_option': "📋 Conserver les photos originales",
        'copy_help_on': "✓ Les photos originales restent dans leur dossier actuel (recommandé pour la sécurité)",
        'copy_help_off': "○ Les photos seront déplacées (supprimées de leur emplacement actuel)",
        'organize_button': "🚀 ORGANISER MES PHOTOS",
        'organize_processing': "⏳ Traitement en cours...",
        'language_label': "🌍 Langue:",
        # Status
        'status_ready': "✨ Prêt à organiser vos photos !",
        'status_source_selected': "📁 Dossier source sélectionné",
        'status_dest_selected': "💾 Dossier de destination sélectionné",
        'status_searching': "🔍 Recherche des photos...",
        'status_found': "📊 {} photos trouvées - Traitement en cours...",
        'status_processing': "📸 Traitement... {}/{} photos",
        'status_done_success': "🎉 Terminé ! {} photos organisées avec succès",
        'status_done_duplicates': "✅ Terminé ! {} nouvelles photos, {} doublons ignorés",
        'status_done_errors': "✅ Terminé ! {} photos traitées, {} doublons ignorés, {} erreurs",
        # Messages
        'error_folders': "Veuillez sélectionner les dossiers source et destination",
        'error_source_missing': "Le dossier source n'existe pas",
        'info_no_photos': "Aucune photo trouvée dans le dossier source",
        'success_title': "🎉 Succès",
        'success_message': "Organisation terminée !\n\n{}\n\n📁 Vos photos sont dans: {}",
        'warning_title': "⚠️ Terminé avec avertissements",
        'warning_message': "Organisation terminée !\n\n{}",
        'photos_organized': "✅ {} photos organisées",
        'duplicates_ignored': "🔄 {} doublons ignorés", 
        'errors_found': "⚠️ {} erreurs",
        # Dialogs
        'choose_source_title': "Choisir le dossier contenant vos photos",
        'choose_dest_title': "Choisir le dossier de destination",
        'unknown_folder': "Inconnu"
    }
}

class PhotoOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("📸 Organisateur de Photos - Simple et Efficace")
        self.root.geometry("700x800")
        self.root.resizable(True, True)
        
        # Configuration file
        self.config_file = "photo_organizer_config.json"
        
        self.source_folder = tk.StringVar()
        self.dest_folder = tk.StringVar()
        
        # Processing options
        self.sort_by_date = tk.BooleanVar(value=True)
        self.copy_mode = tk.BooleanVar(value=True)
        
        # Default language (English)
        self.current_language = tk.StringVar(value='en')
        
        # Load saved configuration
        self.load_config()
        
        # Modern style configuration
        self.setup_style()
        self.setup_ui()
        
        # Save config on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_style(self):
        """Configure a modern style for the interface"""
        style = ttk.Style()
        
        # Modern colors
        style.configure('Title.TLabel', font=('Segoe UI', 18, 'bold'), foreground='#2c3e50')
        style.configure('Heading.TLabel', font=('Segoe UI', 12, 'bold'), foreground='#34495e')
        style.configure('Info.TLabel', font=('Segoe UI', 10), foreground='#7f8c8d')
        style.configure('Modern.TButton', font=('Segoe UI', 10, 'bold'), padding=10)
        style.configure('Action.TButton', font=('Segoe UI', 14, 'bold'), padding=15)
        
        # Style for frames
        style.configure('Card.TFrame', relief='solid', borderwidth=1)
        
    def load_config(self):
        """Load saved configuration"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.source_folder.set(config.get('source_folder', ''))
                    self.dest_folder.set(config.get('dest_folder', ''))
                    self.sort_by_date.set(config.get('sort_by_date', True))
                    self.copy_mode.set(config.get('copy_mode', True))
                    self.current_language.set(config.get('language', 'en'))
        except Exception as e:
            print(f"Error loading configuration: {e}")
    
    def save_config(self):
        """Save current configuration"""
        try:
            config = {
                'source_folder': self.source_folder.get(),
                'dest_folder': self.dest_folder.get(),
                'sort_by_date': self.sort_by_date.get(),
                'copy_mode': self.copy_mode.get(),
                'language': self.current_language.get()
            }
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving configuration: {e}")
    
    def on_closing(self):
        """Called when closing the application"""
        self.save_config()
        self.root.destroy()
    
    def get_text(self, key):
        """Get translated text according to current language"""
        lang = self.current_language.get()
        return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)
    
    def change_language(self, *args):
        """Change interface language"""
        self.save_config()  # Save language change immediately
        self.refresh_ui()
    
    def refresh_ui(self):
        """Refresh all interface texts with the new language"""
        # Window title
        self.root.title(self.get_text('app_title'))
        
        # Update main labels
        self.title_label.config(text="📸 " + ("Photo Organizer" if self.current_language.get() == 'en' else "Organisateur de Photos"))
        self.subtitle_label.config(text=self.get_text('app_subtitle'))
        
        # Sections
        self.folders_frame.config(text=self.get_text('folders_section'))
        self.options_frame.config(text=self.get_text('options_section'))
        
        # Folder labels
        self.source_label.config(text=self.get_text('source_label'))
        self.source_help_label.config(text=self.get_text('source_help'))
        self.dest_label.config(text=self.get_text('dest_label'))
        self.dest_help_label.config(text=self.get_text('dest_help'))
        
        # Buttons
        self.source_button.config(text=self.get_text('choose_button'))
        self.dest_button.config(text=self.get_text('choose_button'))
        self.start_button.config(text=self.get_text('organize_button'))
        
        # Options
        self.sort_checkbox.config(text=self.get_text('sort_option'))
        self.copy_checkbox.config(text=self.get_text('copy_option'))
        self.language_label.config(text=self.get_text('language_label'))
        
        # Update help texts
        self.on_sort_option_changed()
        self.on_copy_option_changed()
        
        # Status
        if hasattr(self, 'status_label'):
            self.status_label.config(text=self.get_text('status_ready'))
        
    def setup_ui(self):
        # Main container with generous padding
        main_container = ttk.Frame(self.root, padding="20")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Resize configuration
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        # No extensible area, optimized fixed size
        
        # === MAIN TITLE ===
        title_frame = ttk.Frame(main_container)
        title_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        title_frame.columnconfigure(0, weight=1)
        
        self.title_label = ttk.Label(title_frame, text="📸 Photo Organizer", 
                                    style='Title.TLabel')
        self.title_label.grid(row=0, column=0)
        
        self.subtitle_label = ttk.Label(title_frame, text=self.get_text('app_subtitle'), 
                                       style='Info.TLabel')
        self.subtitle_label.grid(row=1, column=0, pady=(5, 0))
        
        # === LANGUAGE SELECTOR ===
        lang_frame = ttk.Frame(title_frame)
        lang_frame.grid(row=2, column=0, pady=(10, 0))
        
        self.language_label = ttk.Label(lang_frame, text=self.get_text('language_label'), 
                                       style='Info.TLabel')
        self.language_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.language_combo = ttk.Combobox(lang_frame, textvariable=self.current_language,
                                          values=['en', 'fr'], state='readonly', width=8)
        self.language_combo.pack(side=tk.LEFT)
        self.language_combo.bind('<<ComboboxSelected>>', self.change_language)
        
        # === FOLDERS SECTION ===
        self.folders_frame = ttk.LabelFrame(main_container, text=self.get_text('folders_section'), 
                                           padding="15", style='Card.TFrame')
        self.folders_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        self.folders_frame.columnconfigure(1, weight=1)
        
        # Source folder
        self.source_label = ttk.Label(self.folders_frame, text=self.get_text('source_label'), 
                                     style='Heading.TLabel')
        self.source_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.source_help_label = ttk.Label(self.folders_frame, text=self.get_text('source_help'), 
                                          style='Info.TLabel')
        self.source_help_label.grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=(0, 10))
        
        source_entry = ttk.Entry(self.folders_frame, textvariable=self.source_folder, font=('Segoe UI', 10))
        source_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=(0, 10))
        
        self.source_button = ttk.Button(self.folders_frame, text=self.get_text('choose_button'), 
                                       command=self.select_source_folder, style='Modern.TButton')
        self.source_button.grid(row=2, column=2)
        
        # Visual separator
        ttk.Separator(self.folders_frame, orient='horizontal').grid(row=3, column=0, columnspan=3, 
                                                                   sticky=(tk.W, tk.E), pady=15)
        
        # Destination folder
        self.dest_label = ttk.Label(self.folders_frame, text=self.get_text('dest_label'), 
                                   style='Heading.TLabel')
        self.dest_label.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        self.dest_help_label = ttk.Label(self.folders_frame, text=self.get_text('dest_help'), 
                                        style='Info.TLabel')
        self.dest_help_label.grid(row=5, column=0, columnspan=3, sticky=tk.W, pady=(0, 10))
        
        dest_entry = ttk.Entry(self.folders_frame, textvariable=self.dest_folder, font=('Segoe UI', 10))
        dest_entry.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=(0, 10))
        
        self.dest_button = ttk.Button(self.folders_frame, text=self.get_text('choose_button'), 
                                     command=self.select_dest_folder, style='Modern.TButton')
        self.dest_button.grid(row=6, column=2)
        
        # === OPTIONS SECTION ===
        self.options_frame = ttk.LabelFrame(main_container, text=self.get_text('options_section'), 
                                           padding="15", style='Card.TFrame')
        self.options_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Date sorting option with clear explanation
        sort_frame = ttk.Frame(self.options_frame)
        sort_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.sort_checkbox = ttk.Checkbutton(sort_frame, text=self.get_text('sort_option'), 
                                           variable=self.sort_by_date, 
                                           command=self.on_sort_option_changed)
        self.sort_checkbox.grid(row=0, column=0, sticky=tk.W)
        
        self.sort_info = ttk.Label(sort_frame, text="", style='Info.TLabel', wraplength=600)
        self.sort_info.grid(row=1, column=0, sticky=tk.W, padx=(25, 0), pady=(5, 0))
        
        # Copy/move option with clear explanation  
        copy_frame = ttk.Frame(self.options_frame)
        copy_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        self.copy_checkbox = ttk.Checkbutton(copy_frame, text=self.get_text('copy_option'), 
                                           variable=self.copy_mode,
                                           command=self.on_copy_option_changed)
        self.copy_checkbox.grid(row=0, column=0, sticky=tk.W)
        
        self.copy_info = ttk.Label(copy_frame, text="", style='Info.TLabel', wraplength=600)
        self.copy_info.grid(row=1, column=0, sticky=tk.W, padx=(25, 0), pady=(5, 0))
        
        # Initial update of help texts
        self.on_sort_option_changed()
        self.on_copy_option_changed()
        
        # === MAIN BUTTON ===
        action_frame = ttk.Frame(main_container)
        action_frame.grid(row=3, column=0, pady=15, sticky=tk.W+tk.E)
        action_frame.columnconfigure(0, weight=1)
        
        self.start_button = ttk.Button(action_frame, text=self.get_text('organize_button'), 
                                      command=self.start_organizing, style='Action.TButton')
        self.start_button.grid(row=0, column=0)
        
        # === PROGRESS AREA ===
        progress_frame = ttk.Frame(main_container)
        progress_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(15, 20))
        progress_frame.columnconfigure(0, weight=1)
        
        # Progress bar
        self.progress = ttk.Progressbar(progress_frame, mode='determinate', style='TProgressbar')
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Simple status label
        self.status_label = ttk.Label(progress_frame, text=self.get_text('status_ready'), 
                                     style='Info.TLabel', anchor='center')
        self.status_label.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
    def on_sort_option_changed(self):
        """Update help text for sorting option"""
        if self.sort_by_date.get():
            text = self.get_text('sort_help_on')
        else:
            text = self.get_text('sort_help_off')
        self.sort_info.config(text=text)
        
    def on_copy_option_changed(self):
        """Update help text for copy option"""
        if self.copy_mode.get():
            text = self.get_text('copy_help_on')
        else:
            text = self.get_text('copy_help_off')
        self.copy_info.config(text=text)
        
    def select_source_folder(self):
        folder = filedialog.askdirectory(title=self.get_text('choose_source_title'))
        if folder:
            self.source_folder.set(folder)
            self.save_config()  # Immediate save
            self.update_status(self.get_text('status_source_selected'))
            
    def select_dest_folder(self):
        folder = filedialog.askdirectory(title=self.get_text('choose_dest_title'))
        if folder:
            self.dest_folder.set(folder)
            self.save_config()  # Immediate save
            self.update_status(self.get_text('status_dest_selected'))
    
    def update_status(self, message):
        """Update status message"""
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def get_photo_date(self, filepath):
        """Extract photo date from EXIF metadata"""
        try:
            with Image.open(filepath) as image:
                exifdata = image.getexif()
                
                # Search for photo date
                for tag_id in exifdata:
                    tag = TAGS.get(tag_id, tag_id)
                    data = exifdata.get(tag_id)
                    
                    if tag in ["DateTime", "DateTimeOriginal", "DateTimeDigitized"]:
                        try:
                            return datetime.strptime(data, "%Y:%m:%d %H:%M:%S")
                        except:
                            continue
        except Exception as e:
            pass  # Silent EXIF errors for non-technical users
        
        # If no EXIF data, use file modification date
        try:
            return datetime.fromtimestamp(os.path.getmtime(filepath))
        except:
            return datetime.now()
    
    def get_year_month_path(self, date):
        """Generate folder path in 'Year/Month' format"""
        try:
            lang = self.current_language.get()
            months = TRANSLATIONS[lang]['months']
            month_name = months[date.month]
            year = date.strftime("%Y")
            return os.path.join(year, month_name)
        except:
            return os.path.join(str(datetime.now().year), self.get_text('unknown_folder'))
    
    def files_are_identical(self, file1_path, file2_path):
        """Check if two files are identical (same size and content)"""
        try:
            # Quick size check
            if os.path.getsize(file1_path) != os.path.getsize(file2_path):
                return False
            
            # If same size, hash verification (more reliable)
            def get_file_hash(filepath):
                hash_md5 = hashlib.md5()
                with open(filepath, "rb") as f:
                    # Read in chunks for large files
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
                return hash_md5.hexdigest()
            
            return get_file_hash(file1_path) == get_file_hash(file2_path)
        except:
            return False
    
    def organize_photos(self):
        """Organize photos by date"""
        source = self.source_folder.get()
        destination = self.dest_folder.get()
        
        if not source or not destination:
            messagebox.showerror("❌ Error", self.get_text('error_folders'))
            return
        
        if not os.path.exists(source):
            messagebox.showerror("❌ Error", self.get_text('error_source_missing'))
            return
        
        # Disable button during processing
        self.start_button.config(state='disabled', text=self.get_text('organize_processing'))
        
        # Supported photo file extensions
        photo_extensions = {'.jpg', '.jpeg', '.png', '.tiff', '.tif', '.bmp', '.gif', '.raw', '.cr2', '.nef', '.arw', '.heic', '.webp'}
        
        # Collect all photo files
        self.update_status(self.get_text('status_searching'))
        photo_files = []
        for root, dirs, files in os.walk(source):
            for file in files:
                if Path(file).suffix.lower() in photo_extensions:
                    photo_files.append(os.path.join(root, file))
        
        total_files = len(photo_files)
        if total_files == 0:
            messagebox.showinfo("ℹ️ Information", self.get_text('info_no_photos'))
            self.start_button.config(state='normal', text=self.get_text('organize_button'))
            return
        
        # Status update
        self.update_status(self.get_text('status_found').format(total_files))
        self.progress['maximum'] = total_files
        
        processed = 0
        errors = 0
        skipped_duplicates = 0
        
        for i, photo_path in enumerate(photo_files):
            try:
                filename = os.path.basename(photo_path)
                
                # Determine destination folder based on sorting option
                if self.sort_by_date.get():
                    # Get photo date and create folder by date
                    photo_date = self.get_photo_date(photo_path)
                    year_month_path = self.get_year_month_path(photo_date)
                    dest_folder_path = os.path.join(destination, year_month_path)
                    dest_info = f"{filename} → {year_month_path.replace(os.sep, '/')}"
                else:
                    # No sorting, directly in destination folder
                    dest_folder_path = destination
                    dest_info = f"{filename} → dossier destination"
                
                # Create folder if it doesn't exist
                os.makedirs(dest_folder_path, exist_ok=True)
                
                # Destination file name
                dest_file_path = os.path.join(dest_folder_path, filename)
                
                # Check if file already exists
                if os.path.exists(dest_file_path):
                    # Check if it's exactly the same file
                    if self.files_are_identical(photo_path, dest_file_path):
                        # Identical file already present, ignore it
                        skipped_duplicates += 1
                        if (processed + skipped_duplicates) % 10 == 0:
                            self.update_status(self.get_text('status_processing').format(processed + skipped_duplicates, total_files))
                        continue
                    else:
                        # Different file with same name, add a number
                        counter = 1
                        original_dest_path = dest_file_path
                        while os.path.exists(dest_file_path):
                            name, ext = os.path.splitext(original_dest_path)
                            dest_file_path = f"{name}_{counter}{ext}"
                            counter += 1
                
                # Copy or move based on chosen option
                if self.copy_mode.get():
                    shutil.copy2(photo_path, dest_file_path)
                    action = "📋"
                else:
                    shutil.move(photo_path, dest_file_path)
                    action = "📦"
                
                # Occasional status update
                if (processed + skipped_duplicates) % 10 == 0:  # Every 10 photos
                    self.update_status(self.get_text('status_processing').format(processed + skipped_duplicates, total_files))
                processed += 1
                
            except Exception as e:
                errors += 1
                # Silent errors for simplicity
            
            # Update progress bar
            self.progress['value'] = i + 1
            self.root.update_idletasks()
        
        # Final status
        if errors == 0 and skipped_duplicates == 0:
            self.update_status(self.get_text('status_done_success').format(processed))
        elif skipped_duplicates > 0 and errors == 0:
            self.update_status(self.get_text('status_done_duplicates').format(processed, skipped_duplicates))
        else:
            self.update_status(self.get_text('status_done_errors').format(processed, skipped_duplicates, errors))
        
        # Re-enable button
        self.start_button.config(state='normal', text=self.get_text('organize_button'))
        
        # Final notification
        message_parts = []
        if processed > 0:
            message_parts.append(self.get_text('photos_organized').format(processed))
        if skipped_duplicates > 0:
            message_parts.append(self.get_text('duplicates_ignored').format(skipped_duplicates))
        if errors > 0:
            message_parts.append(self.get_text('errors_found').format(errors))
            
        if errors == 0:
            messagebox.showinfo(self.get_text('success_title'), 
                              self.get_text('success_message').format(chr(10).join(message_parts), destination))
        else:
            messagebox.showwarning(self.get_text('warning_title'), 
                                 self.get_text('warning_message').format(chr(10).join(message_parts)))
    
    def start_organizing(self):
        """Start organization in a separate thread"""
        # Save config before starting
        self.save_config()
        threading.Thread(target=self.organize_photos, daemon=True).start()

def main():
    root = tk.Tk()
    app = PhotoOrganizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()