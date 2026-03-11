with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

with open("sample.txt", "a") as f:
    f.write("New line added\n")
    f.write("Another line\n")

with open("sample.txt", "r") as f:
    print(f.read())