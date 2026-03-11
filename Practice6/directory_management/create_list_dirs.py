import os

os.makedirs("folder1/folder2/folder3", exist_ok=True)

print("Directories created")

files = os.listdir(".")

for f in files:
    print(f)

for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)