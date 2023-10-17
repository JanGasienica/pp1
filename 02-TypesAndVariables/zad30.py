import random
dice_roll = random.randrange(1,6)
print(f"Dice rolled: {dice_roll}")
if_special_number = dice_roll==1 or dice_roll==6
print(f"Special number: {if_special_number}")
