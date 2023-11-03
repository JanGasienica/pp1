def fibonacci_sequence(number):
    x=0
    y=1
    for i in range(number):
        while x>y:
            x=x+y
        while y>=x:
            y=x+y
    if x>y:
        return x
    else:
        return y