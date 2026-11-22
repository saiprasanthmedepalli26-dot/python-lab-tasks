# Unit 3D - Task 6: Print Details Using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(name="Krishna", age=26, city="Guntur")
