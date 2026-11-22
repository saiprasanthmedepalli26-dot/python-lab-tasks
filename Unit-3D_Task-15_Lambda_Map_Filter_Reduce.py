# Unit 3D - Task 15: Lambda with map(), filter() and reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x * x, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda x, y: x + y, numbers)

print("Original numbers:", numbers)
print("Squares using map():", squares)
print("Even numbers using filter():", even_numbers)
print("Sum using reduce():", total)
