# Define the number of rows and columns in the lottery coupon
rows = 7
columns = 7
number = 1

# Create a 2D list to store the numbers
lottery_coupon = [[0] * columns for _ in range(rows)]

# Fill in the lottery numbers
for col in range(columns):
    for row in range(rows):
        lottery_coupon[row][col] = number
        number += 1
        if number > 49:
            break

# Print the lottery coupon
for row in lottery_coupon:
    for num in row:
        print(f"{num:2}", end=" ")
    print()
