rows = int(input("Enter number of rows for upper half: "))
for row in range(1, rows + 1):
    print(" " * (rows - row) + "* " * row)
for row in range(rows - 1, 0, -1):
    print(" " * (rows - row) + "* " * row)
