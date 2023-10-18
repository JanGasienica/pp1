Current_product_price = 140.00
Previous_product_price = 200.00
discount_10 = (Previous_product_price/100)*10
discount = (Current_product_price/Previous_product_price)*100
discount = 100 - discount
if(Previous_product_price - Current_product_price >= discount_10):
    print("Buy the product!!")
    print(f"Product price reduced by {discount}")

