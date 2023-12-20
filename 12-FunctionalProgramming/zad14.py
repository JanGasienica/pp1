exchange_rate = 4.5
eur = [15.90, 38.47, 4.07, 132.70, 9.15]
pln = list(map(lambda x: x * exchange_rate, eur))

for amount_pln in pln:
    print(round(amount_pln, 2))
