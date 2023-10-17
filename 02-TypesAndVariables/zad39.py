starting_price = float(input("Enter starting price of the item: "))
discount = int(input("Enter the discount in %: "))
reduction=(starting_price/100)*discount
print(f"Price with discount: {starting_price-reduction}")
print(f"Reduction: {round(reduction,2)}")
