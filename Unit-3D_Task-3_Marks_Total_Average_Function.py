# Unit 3D - Task 3: Total and Average of Three Subjects
def calculate_marks(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return total, average

m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))
total, average = calculate_marks(m1, m2, m3)
print("Total marks:", total)
print("Average marks:", average)
