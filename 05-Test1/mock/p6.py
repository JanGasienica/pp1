def f(number,even):
    number_str = str(number)
    a=[]
    sum = 0
    for i in number_str:
        a.append(i)
        if even == True:
            for j in number_str:
                if int(a.index(i)) % 2 == 0:
                    sum = sum + int(a.index(i))
        if even == False:
            for l in number_str:
                if int(a.index(i)) % 2 == 1:
                    sum = sum + int(a.index(i))
    return sum


if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))
