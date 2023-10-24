import random
for i in range (10):
    print(i)
    random_number = random.randrange(1,30)
    if random_number % 5 ==0:
      print("FIVE")
    if random_number % 3 ==0:
      print("THREE")
    if random_number % 5 ==0 and random_number%3==0:
      print("BINGO")
