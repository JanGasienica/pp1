credit_card_nr = input("Enter credit card number: ")
formatted_number = f"{credit_card_nr[:4]} {credit_card_nr[4:8]} {credit_card_nr[8:12]} {credit_card_nr[12:]}"
print(f"Card number: {formatted_number}")