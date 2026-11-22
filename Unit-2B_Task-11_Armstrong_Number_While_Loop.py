n = int(input("Enter a number: "))
temp = abs(n)
digits = len(str(temp))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
if n >= 0 and total == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
