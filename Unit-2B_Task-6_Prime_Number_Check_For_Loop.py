n = int(input("Enter a number: "))
is_prime = n > 1
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
