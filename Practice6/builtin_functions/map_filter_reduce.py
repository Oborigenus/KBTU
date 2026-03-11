numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x**2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))

print("Squared:", squared)
print("Even:", even)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print("Sum:", total)