registration_number = input("Enter ur registration number: ")
is_from_krakow = registration_number.startswith('KR') or registration_number.startswith('KK')
print(f"Car from Kraków: {is_from_krakow}")
