import random
dice_roll = random.randrange(1,6)
players_guess = int(input("Enter the number between 1 and 6: "))
the_player_won = dice_roll == players_guess
print(f"U won gz: {the_player_won}")