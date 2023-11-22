user_input = input("Enter name of the file: ")
counter = 0
with open(user_input,'r') as file:
    for value in file:
        counter += 1
print(user_input)
print(counter)