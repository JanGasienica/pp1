def f(bin_number):
    for digit in bin_number:
        if digit != '0' and digit != '1':
            return False
    return True

if __name__ == "__main__":  
    print(f("101101"))
    print(f("1311a10100"))