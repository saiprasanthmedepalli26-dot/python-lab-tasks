n = int(input("How many numbers? "))
if n > 0:
    largest = float(input("Enter number 1: "))
    for i in range(2, n + 1):
        num = float(input("Enter number: "))
        if num > largest:
            largest = num
    print("Largest number =", largest)
else:
    print("Please enter at least one number.")
