import os
import shutil

# Define the directories to organize the files into
directories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".pdf", ".txt"],
    "Music": [".mp3", ".wav", ".wma"],
    "Videos": [".mp4", ".avi", ".mov"],
}

# Define the source directory to organize files from
src_dir = "C:/Users/YourName/Downloads"

# Create the destination directories if they do not exist
for dirname in directories.keys():
    if not os.path.exists(dirname):
        os.mkdir(dirname)

# Organize the files in the source directory into the destination directories
for filename in os.listdir(src_dir):
    if os.path.isfile(os.path.join(src_dir, filename)):
        file_ext = os.path.splitext(filename)[1]
        for dirname, extensions in directories.items():
            if file_ext in extensions:
                shutil.move(os.path.join(src_dir, filename), os.path.join(dirname, filename))
                break
