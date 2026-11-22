# Unit 3D - Task 13: Fibonacci Series Using Recursion
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

terms = int(input("Enter number of terms: "))
if terms <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
