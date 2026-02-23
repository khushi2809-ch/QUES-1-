# Taking input from user
n = int(input("Enter number of rows: "))

# Check if number is positive
if n > 0:

    # 🔺 Upper part of diamond
    for rows in range(1, n + 1):
        # Print spaces first -> (n - rows)
        # Then print stars -> (2*rows - 1)
        print(" " * (n - rows) + "*" * (2 * rows - 1))

    # 🔻 Lower part of diamond
    for rows in range(n - 1, 0, -1):
        # Same logic as above
        print(" " * (n - rows) + "*" * (2 * rows - 1))

# If user enters 0 or negative number
else:
    print("Not possible")