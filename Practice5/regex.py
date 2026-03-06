import re

text = input()
print(re.findall(r"ab*", text))


text = input()
print(re.findall(r"ab{2,3}", text))


text = input()
print(re.findall(r"[a-z]+_[a-z]+", text))


text = input()
print(re.findall(r"[A-Z][a-z]+", text))


text = input()
print(re.findall(r"a.*b", text))


text = input()
print(re.sub(r"[ ,\.]", ":", text))


text = input()
print(re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text))


text = input()
print(re.split(r"(?=[A-Z])", text))


text = input()
print((re.sub(r"([A-Z])", r" \1", text)).strip())


text = input()
print(re.sub(r'([A-Z])', r'_\1', text).lower())