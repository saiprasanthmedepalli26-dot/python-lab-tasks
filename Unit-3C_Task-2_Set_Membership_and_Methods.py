numbers = {10, 20, 30, 40}
print("Set:", numbers)
print("Is 20 present?", 20 in numbers)
numbers.discard(50)
print("After discard:", numbers)
numbers.update([50, 60])
print("After update:", numbers)
