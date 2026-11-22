# Unit 3D - Task 14: GCD Using Recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD:", gcd(abs(num1), abs(num2)))
