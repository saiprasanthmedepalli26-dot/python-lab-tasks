# Unit 3D - Task 8: Student Details Using **kwargs
def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

student_details(name="Anu", Mathematics=85, Physics=90, Python=95)
