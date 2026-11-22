# Unit 3D - Task 2: Celsius to Fahrenheit Using Function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
