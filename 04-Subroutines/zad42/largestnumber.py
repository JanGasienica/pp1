def find_highest_number(a, b, c):
    if a >= b and a >= c:
        highest =  a
    elif b >= a and b >= c:
        highest = b
    else:
        highest = c
    if a <= b and a <= c:
        lowest =  a
    elif b <= a and b <= c:
        lowest = b
    else:
        lowest = c
    return highest - lowest