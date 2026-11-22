# Unit 3D - Task 11: Bank Balance Using Global and Local Variables (Optional)
balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print("After deposit, balance:", balance)

def show_local_balance():
    balance = 500
    print("Local balance:", balance)

deposit(500)
show_local_balance()
print("Actual account balance:", balance)
