# Unit 3D - Task 10: Global Counter Increment (Optional)
counter = 0

def increment():
    global counter
    counter = counter + 1

increment()
increment()
increment()
print("Counter:", counter)
