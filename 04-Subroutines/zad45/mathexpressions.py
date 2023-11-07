def expressions(expression):
    a=[]
    sum = 0
    for i in expression:
        a.append(i)
        if i in '+-':
            operator = i
            if operator == '+':
                sum += int(a[-2]) + int(a[-1])
            elif operator == '-':
                sum += int(a[-2]) - int(a[-1])
    return sum
    