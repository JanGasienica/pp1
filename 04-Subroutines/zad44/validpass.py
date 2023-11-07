def validpass(password):
    a =[]
    b=0
    for i in password:
        a.append(i)
        if(a.count(i)>=2 or len(password) == 0):
            b=1
            return("False")
            break
    if(b!=1):
        return("True")