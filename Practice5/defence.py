import re
with open("raw.txt", encoding="utf-8") as f:
    text = f.read()



pattern = r"\d+,\d+"
find = re.findall(pattern , text)
print(*find)


pattern2 = r"\d/.\n.\n"
find2 = re.findall(pattern2 , text)
print(*find2)

