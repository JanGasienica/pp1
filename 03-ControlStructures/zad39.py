# Define the dimensions of the rectangle
a = 4  # Height
b = 15  # Width

# Create the top side of the rectangle
top_side = "*" * b

# Create the sides of the rectangle
side = "*" + " " * (b - 2) + "*"

# Print the rectangle
print(top_side)
for _ in range(a - 2):
    print(side)
print(top_side)
