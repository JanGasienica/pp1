# Define the correct PIN code
correct_pin = "0805"

# Initialize the number of allowed attempts
attempts = 3

# Create a loop to handle PIN entry
while attempts > 0:
    # Read the PIN code from the user
    entered_pin = input("Enter the PIN code: ")
    
    # Check if the entered PIN is correct
    if entered_pin == correct_pin:
        print("PIN code is correct. Access granted.")
        break
    else:
        print("Incorrect...")
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} {'attempts' if attempts > 1 else 'attempt'} remaining.")
        else:
            print("Sorry, your payment card has been blocked.")
