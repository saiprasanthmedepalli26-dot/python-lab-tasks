n = int(input("Enter a number: "))
temp = abs(n)
original = temp
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if n >= 0 and original == reverse:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
