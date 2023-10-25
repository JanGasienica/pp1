def numbers(n):
    i = 1
    while i < n+1:
        print(i, end = " ")
        i = i +1
number = int(input("Enter a number: "))
print(f"Numbers <1,{number}>: ") 
numbers(number)

