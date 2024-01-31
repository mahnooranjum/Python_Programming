

import os
import shutil




# Set the directory path you want to extract files from
source_directory = "./testfolder"

# Set the directory where you want to extract the files
destination_directory = "./testoutput"

# Create the destination directory if it doesn't exist
# if not os.path.exists(destination_directory):
#     os.makedirs(destination_directory)


import datetime

def get_date_modified(filepath):
    try:
        # Get the date modified in a human-readable format
        date_modified = os.path.getmtime(filepath)
        date_modified = datetime.datetime.fromtimestamp(date_modified).strftime('%Y_%m')

        return date_modified
    except FileNotFoundError:
        return None

from collections import defaultdict
# Function to extract files from the source directory and its subfolders
def extract_files(source_dir):
    dict_date_path = defaultdict(list)
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            # print(source_path)
            dict_date_path[get_date_modified(source_path)].append(source_path)
            # destination_path = os.path.join(dest_dir, file)
            
            # Copy the file to the destination directory

            # shutil.copy2(source_path, destination_path)
            # print(f"Extracted: {source_path} to {destination_path}")
            
    return dict_date_path


import shutil

def organize_files(destination_folder, file_dict):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for key, files in file_dict.items():
        # Create a directory with the key as the folder name
        folder_path = os.path.join(destination_folder, key)
        os.makedirs(folder_path, exist_ok=True)
        
        # Copy files to the corresponding folder
        for file_path in files:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(folder_path, file_name)
            shutil.copy(file_path, destination_path)





returner = extract_files(source_directory)
organize_files(destination_directory, returner)
