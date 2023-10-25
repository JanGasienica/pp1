def different(n1,n2,n3):
    if n1 == n2 == n3:
        return True

number1 = int(input("Enter first number: "))
number2 = int(input("Enter secound number: "))
number3 = int(input("Enter third number: "))

result = different(number2 , number1, number3)
if True:
    print(f"Numbers {number1}, {number2}, and {number3} are same")
else:
    print(f"Numbers {number1}, {number2}, and {number3} are diferent")
