import os
import shutil

def organize_files(path):
    if not os.path.isdir(path):
        print(f"The provided path: {path} is not a directory.")
        return
    
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff','.webp','.svg'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv','.webm'],
        'Documents': ['.xls', '.xlsx', '.doc', '.docx', '.pdf', '.ppt', '.pptx','.csv'],
        'XML': ['.xml'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Applications': ['.deb', '.tar'],
        'Zip': ['.zip'],
        'Pem': ['.pem'],
    }
    
    for folder in folders:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            for folder, extensions in folders.items():
                if file_ext in extensions:
                    shutil.copy(file_path, os.path.join(path, folder, file_name))
                    break

    print(f"Files in {path} have been organized.")

if __name__ == "__main__":
    input_path = input("Enter the path to organize: ")
    organize_files(input_path)
