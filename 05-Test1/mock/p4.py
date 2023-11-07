def f(card_number):
    a=[]
    card_number_str = str(card_number)
    for i in card_number_str:
        a.append(i)
    for j in range(10):
        a[j+2]= "*"

    return "".join(a)

if __name__ == "__main__":
    print(f("5290312400019022")) 