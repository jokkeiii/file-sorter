import os
import shutil

# Set the directory where the files are located
dir_path = 'C:/Users/zucc/Downloads'

# Set the directories for each file type
img_dir = 'C:/Users/zucc/Pictures/Saved Pictures/Downloaded'
doc_dir = 'C:/Users/zucc/Documents/Downloaded'
audio_dir = 'C:/Users/zucc/Music/Downloaded'
video_dir = 'C:/Users/zucc/Videos/Downloaded'
archive_dir = 'C:/Users/zucc/Downloads/Archives'
exe_dir = 'C:/Users/zucc/Downloads/Executables'
disc_dir = 'C:/Users/zucc/Downloads/ISOs'
ebook_dir = 'C:/Users/zucc/OneDrive/Tiedostot/Kirjat/Downloaded'
misc_dir = 'C:/Users/zucc/Downloads/miscellaneous'

# Loop through the files in the directory
for file in os.listdir(dir_path):

    # Skip directories
    if os.path.isdir(os.path.join(dir_path, file)):
        continue

    # Get the file extension
    extension = file.split('.')[-1]

    # Move the file to the appropriate directory
    if extension in ['jpg', 'jpeg', 'png', 'gif']:
        shutil.move(os.path.join(dir_path, file), img_dir)
    elif extension in ['doc', 'docx', 'pdf']:
        shutil.move(os.path.join(dir_path, file), doc_dir)
    elif extension in ['mp3', 'wav', 'm4a']:
        shutil.move(os.path.join(dir_path, file), audio_dir)
    elif extension in ['mp4', 'avi', 'mkv']:
        shutil.move(os.path.join(dir_path, file), video_dir)
    elif extension in ['zip', 'rar', '7z']:
        shutil.move(os.path.join(dir_path, file), archive_dir)
    elif extension in ['exe', 'msi']:
        shutil.move(os.path.join(dir_path, file), exe_dir)
    elif extension in ['iso', 'img']:
        shutil.move(os.path.join(dir_path, file), disc_dir)
    elif extension in ['epub', 'mobi']:
        shutil.move(os.path.join(dir_path, file), ebook_dir)
    else:
        shutil.move(os.path.join(dir_path, file), misc_dir)
        