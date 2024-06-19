import os
import shutil
from collections import defaultdict

# Mapping file extensions to categories
FILE_CATEGORIES = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'ico', 'webp'],
    'documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'ods', 'odp', 'rtf', 'md'],
    'videos': ['mp4', 'mov', 'avi', 'mkv', 'flv', 'wmv', 'webm', 'mpg', 'mpeg', '3gp'],
    'audio': ['mp3', 'wav', 'aac', 'flac', 'ogg', 'm4a', 'wma', 'alac'],
    'archives': ['zip', 'rar', 'tar', 'gz', '7z', 'bz2', 'xz', 'iso'],
    'scripts': ['py', 'js', 'html', 'css', 'sh', 'bat', 'php', 'rb', 'pl', 'java', 'cpp', 'c', 'cs'],
    'others': []
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return 'others'

def organize_files_by_category(directory):
    # Dictionary to hold category as key and list of files as value
    file_dict = defaultdict(list)
    
    # Scan the directory and classify files by their category
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            file_extension = item.split('.')[-1]
            category = get_category(file_extension)
            file_dict[category].append(item_path)

    # Create folders and move files
    for category, files in file_dict.items():
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
        
        for file in files:
            try:
                shutil.move(file, os.path.join(folder_path, os.path.basename(file)))
            except shutil.Error:
                # In case of conflict, e.g., a file with the same name already exists in the destination
                print(f"File {file} already exists in {folder_path}. Skipping.")

if __name__ == "__main__":
    # Take directory path as input from the user
    target_directory = input("Enter the path of the directory to organize: ")
    # Ensure the path is valid
    if os.path.isdir(target_directory):
        organize_files_by_category(target_directory)
        print(f"Files in {target_directory} have been organized by category.")
    else:
        print("The provided path is not a valid directory.")
