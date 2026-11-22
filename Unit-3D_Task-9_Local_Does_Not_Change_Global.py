# Unit 3D - Task 9: Local Variable Does Not Change Global Variable
value = 100

def show_value():
    value = 50
    print("Local value:", value)

show_value()
print("Global value:", value)
