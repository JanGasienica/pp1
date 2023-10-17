buying_rate = float(input("Enter the Euro buying rate: "))
selling_rate = float(input("Enter the Euro selling rate: "))
spread = selling_rate - buying_rate
print(f"Spread: {round(spread,5)}")
