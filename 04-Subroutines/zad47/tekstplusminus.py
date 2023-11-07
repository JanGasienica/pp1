def tekst_plus_minus(expression):
    a=[]
    for i in expression:
        a.append(i)
        if a.index(i) % 2 == 1:
            a.insert(i)
    return a