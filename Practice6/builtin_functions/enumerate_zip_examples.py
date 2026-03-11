names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for i, name in enumerate(names):
    print(i, name)

for name, score in zip(names, scores):
    print(name, score)

value = "123"

print(type(value))

num = int(value)
print(num, type(num))

float_num = float(num)
print(float_num, type(float_num))