amount = int(input("Enter the amount in PLN: "))
amount5 = 0
amount2 = 0
amount1 = 0

while amount > 0:
    while amount>=5:
        amount = amount-5
        amount5 = amount5+1
    while amount>=2:
        amount = amount-2
        amount2 = amount2+1
    while amount>=1:
        amount = amount - 1
        amount1 = amount1+1
print(f"The amount of PLN {amount} in coins:")
print(f"5 zł - {amount5}")
print(f"2 zł - {amount2}")
print(f"1 zł - {amount1}")