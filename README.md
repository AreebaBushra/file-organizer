# Automatic File Organizer

A command-line tool that automatically organizes messy folders by sorting files into categorized subfolders — and finds duplicate files across two folders using MD5 hashing.

## Before

Downloads/
```
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mkv
└── notes.txt
```

## After

Downloads/
```
├── Images/
│   └── photo.jpg
├── Documents/
│   ├── resume.pdf
│   └── notes.txt
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mkv
```
## Features

- Automatically detects file types by extension
- Creates subfolders only when needed
- Handles duplicate filenames by renaming them
- Skips subfolders safely
- Shows a summary after organizing
- Finds duplicate files across two folders using MD5 fingerprinting
- Optionally deletes duplicates found in the second folder
  
## How to run

Make sure you have Python 3 installed. Then:

```bash
git clone https://github.com/AreebaBushra/file-organizer.git
cd file-organizer
python file_organizer.py
```

Enter your folder path when prompted — or it auto-detects
your Downloads folder.

## Supported file types

| Category  | Extensions                    |
|-----------|-------------------------------|
| Images    | .jpg .jpeg .png               |
| Documents | .pdf .docx .txt               |
| Audio     | .mp3 .wav                     |
| Videos    | .mp4 .mkv .avi                |
| Archives  | .zip .rar                     |
| Others    | anything not listed above     |

## Built with

- Python 3
- pathlib
- shutil
- hashlib



## What I learned

- Working with file systems using pathlib and shutil
- Generating MD5 file hashes to detect identical content
- Handling edge cases like duplicates and empty folders
- Building CLI tools with clean user feedback

## Concepts practiced
- File I/O
- Pathlib and shutil
- Dictionary lookups
- Loops and conditionals
- Duplicate file handling
- MD5 hashing for content comparison
- Comparing files across directories
