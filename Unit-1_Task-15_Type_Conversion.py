# Unit 1 - Task 15
# Demonstrate type conversion: int, float, and string

integer_value = 25
float_value = 12.75
string_value = "100"

converted_float = float(integer_value)
converted_int = int(float_value)
converted_int_from_string = int(string_value)
converted_string = str(integer_value)

print("Integer value:", integer_value)
print("Integer to float:", converted_float)

print("Float value:", float_value)
print("Float to int:", converted_int)

print("String value:", string_value)
print("String to int:", converted_int_from_string)

print("Integer to string:", converted_string)
print("Type of converted string:", type(converted_string))
