telephone_number = input("Enter a 9-digit telephone number: ")
formatted_number = f"{telephone_number[:3]}-{telephone_number[3:6]}-{telephone_number[6:]}"
print(f"Formatted Telephone Number: {formatted_number}")