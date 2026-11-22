# Unit 3D - Task 4: Simple Interest Using Default Arguments
def simple_interest(principal, time, rate=5):
    return (principal * time * rate) / 100

principal = float(input("Enter principal amount: "))
time = float(input("Enter time in years: "))
print("Simple interest with default rate (5%):", simple_interest(principal, time))
rate = float(input("Enter another rate: "))
print("Simple interest with given rate:", simple_interest(principal, time, rate))
