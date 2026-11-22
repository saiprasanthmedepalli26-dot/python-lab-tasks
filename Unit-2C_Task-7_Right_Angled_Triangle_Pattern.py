rows = int(input("Enter number of rows: "))
for row in range(1, rows + 1):
    for col in range(row):
        print("*", end=" ")
    print()
