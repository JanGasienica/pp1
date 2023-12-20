speed = [48,47,54,50,42,68,39,46]

max_speed = list(filter(lambda x:x>50,speed))

for x in max_speed:
    print(x)