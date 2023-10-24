# Define the number of rows
n = 5

# Create the top half of the pattern
for i in range(1, n + 1):
    for j in range(i):
        print("* ", end="")
    print()

# Create the bottom half of the pattern
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()
