# Unit 3D - Task 5: Sum Using *args
def find_sum(*args):
    total = 0
    for value in args:
        total = total + value
    return total

print("Sum:", find_sum(10, 20, 30, 40))
