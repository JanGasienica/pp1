stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

sum_stock = list(map(lambda x:round(x[0]*x[1],2),stock))
sum_e = round(sum(sum_stock),2)

print(sum_e)