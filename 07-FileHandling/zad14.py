file = open("shopping_list.txt",'w')

end_program = False
counter = 1

while end_program != True:
    product = input("Enter product to shopping list: ")
    if product != "":
        file.write(f"{counter}. {product}"+'\n')
        counter +=1
    else:
        end_program = True
file.close()
