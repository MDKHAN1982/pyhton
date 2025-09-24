import shutil
import os

folder_path = "E:/JKHAN-DOC/01 PROGRAMMING LANGUAGES/PYTHON/.vscode"

if os.path.exists(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and its contents deleted successfully.")
    except OSError as e:
        print(f"Error deleting folder '{folder_path}': {e}")
else:
    print(f"Error: Folder '{folder_path}' not found.")