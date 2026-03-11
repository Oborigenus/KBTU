import shutil

shutil.copy("sample.txt", "sample_backup.txt")

print("File copied successfully")

import os

file_name = "sample_backup.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File deleted")
else:
    print("File not found")