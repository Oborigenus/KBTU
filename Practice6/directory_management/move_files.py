import shutil

shutil.copy("sample.txt", "folder1/sample.txt")

shutil.move("sample.txt", "folder1/sample_moved.txt")

print("File copied and moved")