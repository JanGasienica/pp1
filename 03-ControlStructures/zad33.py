# Step 1: Read a decimal number from the user
decimal_number = int(input("Enter a decimal number: "))

# Initialize an empty string to store the binary representation
binary_representation = ""

# Step 2-4: Convert decimal to binary
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_representation = str(remainder) + binary_representation
    decimal_number = decimal_number // 2

# Step 5: Display the binary representation
print(f"Binary representation: {binary_representation}")
