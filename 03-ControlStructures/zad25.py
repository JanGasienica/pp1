Number_of_products_purchased = int(input("Number of products purchased: "))
Product_price = int(input("Product price: "))
if(Number_of_products_purchased<=2):
    print(f"Amount to pay: {Number_of_products_purchased*Product_price}")
else:
    print(f"Amount to pay: {Number_of_products_purchased*2+(Number_of_products_purchased-2)*(Product_price/75)*100}")