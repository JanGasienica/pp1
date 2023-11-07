def sum_of_devide_6(x,y):
    sum = 0
    for (i) in range(y+1-x):
        if x % 6 == 0 and x % 4 != 0:
            sum = sum + x
        x = x +1
    return sum