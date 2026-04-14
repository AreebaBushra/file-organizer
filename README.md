# Automatic File Organizer

A Python CLI tool that automatically organizes a messy 
folder by sorting files into subfolders by type.

## What it does
- Moves images into /Images
- Moves documents into /Documents  
- Moves videos into /Videos
- Moves audio into /Audio
- Moves archives into /Archives
- Handles duplicate filenames automatically by renaming them
- Skips subfolders safely

## Example output
<img width="1366" height="727" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/a7a88477-4e0a-4842-bb41-b42c3d01f85d" />


## How to run

python file_organizer.py

Then enter your folder path when asked. 
Or it auto-detects your Downloads folder.

## Libraries used
- pathlib — for file path handling
- shutil  — for moving files
- os      — built in, no install needed

## Concepts practiced
- File I/O
- Pathlib and shutil
- Dictionary lookups
- Exception handling
- Loops and conditionals
- Duplicate file handling
