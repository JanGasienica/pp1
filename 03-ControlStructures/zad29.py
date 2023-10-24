washing_product = input("Enter washing product: ")
washing_time = 0
if washing_product == 'shoes':
    washing_time = washing_time + 20
if washing_product == 'jacket':
    washing_time = washing_time + 40
if washing_product == 'underwhear':
    washing_time = washing_time + 70
rinse = input("If u want rinse type 'y' if not type 'n'")
spin = input("If u want spin type 'y' if not type 'n'")
if rinse == 'y':
    washing_time = washing_time + 15
if spin == 'y':
    washing_time = washing_time + 9
print(f"Washing product = {washing_product}")
if rinse == 'y':
    print("rinse = True")
else:
    print("rinse = false")
if spin == 'y':
    print("spin = True")
else:
    print("spin = false")
print(f"Total washing time: {washing_time} minutes")