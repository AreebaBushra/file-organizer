
import shutil
import hashlib
from pathlib import Path

# CATEGORY MAPPING
# Add new extensions here to support more file types

categories = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".mp3": "Audio", ".wav": "Audio",
    ".mp4": "Videos", ".mkv": "Videos", ".avi": "Videos",
    ".zip": "Archives", ".rar": "Archives"
}

# --------------------------------------------------------------------------------
# ORGANIZE FOLDER
folder_path = input("Enter the folder path you want to organize: ")

# Validate the path before doing anything 

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

# Counters to track what happened during organizing

moved = 0
skipped = 0
duplicates = 0

# LOOP through every item in all_items one by one:

for item in all_items:
    print(item)
    
    # Skip subfolders — as we want to move files
    if item.is_dir():
        skipped += 1
        continue
    extension = item.suffix.lower()
    # If extension not in dictionary, send to Others 
    category = categories.get(extension, "Others")
    
    destination_folder = Path(folder_path) / category
    destination_folder.mkdir(exist_ok=True)
    destination = destination_folder / item.name
    
    if not destination.exists():
        shutil.move(str(item), str(destination))
        print(f" Moved {item.name} to {category}")
        moved += 1
    else:
        # File with same name exists — add a number to avoid overwriting
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

# -----------------------------------------------------------------------
# FIND DUPLICATES ACROSS TWO FOLDERS

# get_file_hash    → gives every file a unique fingerprint
 
def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()
 
# scan_folder      → builds a dictionary of fingerprints for a whole folder
 
def scan_folder(folder_path):
    hash_map = {}
    for item in Path(folder_path).iterdir():
        if item.is_file():
            file_hash = get_file_hash(item)
            hash_map[file_hash] = item
    return hash_map
    
# find_duplicates  → compares two dictionaries, finds matching fingerprints
#                  = files with identical content across two folders
 
def find_duplicates(folder_a, folder_b):
    print(f"Scanning {folder_a}....")
    hashes_a = scan_folder(folder_a)
    
    print(f"Scanning {folder_b}....")
    hashes_b = scan_folder(folder_b)
    
    duplicates = []
    # Check each file in folder B against folder A's hash dictionary
    # If the same hash exists in both — identical file found
    for hash_val, filepath_b in hashes_b.items():
        if hash_val in hashes_a:
            duplicates.append({
                "folder_a_file" : hashes_a[hash_val],
                "folder_b_file" : filepath_b
                })
    return duplicates
    
# ------------------------------------------------------------
# USAGE

folder_a = input("Enter first folder path:")
folder_b = input("Enter second folder path:")
 
duplicates = find_duplicates(folder_a, folder_b)
 
if len (duplicates) == 0:
    print("No duplicates found!")
else:
    print(f"\n Found {len(duplicates)} duplicates file:\n")
    for d in duplicates:
        print(f" {d['folder_a_file'].name}")
        print(f" → same as: {d['folder_b_file']}\n")
 
    choice = input("Delete duplicates from second folder? (yes/no): ")
    if choice.lower() == "yes":
        for d in duplicates:
            d["folder_b_file"].unlink() # unlink() = pathlib's way to delete a file
            print(f"Deleted: {d['folder_b_file'].name}")
 
                                                                                        



