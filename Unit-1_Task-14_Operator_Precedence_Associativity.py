# Unit 1 - Task 14
# Demonstrate operator precedence and associativity

a = 10
b = 5
c = 2

result1 = a + b * c
result2 = (a + b) * c
result3 = a ** b ** c

print("a + b * c =", result1)
print("(a + b) * c =", result2)
print("a ** b ** c =", result3)

# Multiplication has higher precedence than addition.
# Exponentiation is evaluated right-to-left.
