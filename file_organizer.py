
import shutil
from pathlib import Path

# Define the categories dictionary:

categories = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".mp3": "Audio", ".wav": "Audio",
    ".mp4": "Videos", ".mkv": "Videos", ".avi" : "Videos",
    ".zip": "Archives", ".rar": "Archives"
}


folder_path = input("Enter the folder path you want to organize: ")

# Check if that folder actually exists on the computer

if not Path(folder_path).exists():
    print("The specified folder does not exist.")
    exit()

if not Path(folder_path).is_dir():
    print("That is a file, not a folder. Please enter a folder path.")
    exit()

print("Organizing files in:", folder_path)

# GET the list of every item inside that folder

all_items = list(Path(folder_path).iterdir())
if len(all_items) == 0:
    print("This folder is already empty, nothing to organize.")

print(f"Found {len(all_items)} items. Starting to organize......")

# SET three counters at zero:

moved = 0
skipped = 0
duplicates = 0

# LOOP through every item in all_items one by one:

for item in all_items:
    print(item)
    
    if item.is_dir():
        skipped += 1
        continue
    extension = item.suffix.lower()
    category = categories.get(extension, "Others")
    
    destination_folder = Path(folder_path) / category
    destination_folder.mkdir(exist_ok=True)
    destination = destination_folder / item.name
    
    if not destination.exists():
        shutil.move(str(item), str(destination))
        print(f" Moved {item.name} to {category}")
        moved += 1
    else:
        counter = 1
        while True:
            new_name = f"{item.stem}_{counter}{item.suffix}"
            new_destination = destination_folder / new_name
            if not new_destination.exists():
                shutil.move(str(item), str(new_destination))
                print(f"Moved {new_name} to {category} (renamed)")
                duplicates += 1
                break
            counter += 1

print(f"/Done!")
print(f"Files moved: {moved}")
print(f"Duplicates renamed: {duplicates}")
print(f"Folders skipped: {skipped}")
                                                                                        



