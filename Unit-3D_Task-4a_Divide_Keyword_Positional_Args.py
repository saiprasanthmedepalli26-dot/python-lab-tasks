# Unit 3D - Task 4a: Keyword and Positional Arguments
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Using keyword arguments:", divide(b=10, a=20))
print("Using positional arguments:", divide(10, 20))
