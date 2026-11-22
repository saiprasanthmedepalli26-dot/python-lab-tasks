# Unit 1 - Task 5
# Swap two numbers without using a third variable

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
