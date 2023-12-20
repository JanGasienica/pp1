distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

mean = lambda x,y,z: x/(hours+minutes/60)
result = mean(distance,hours,minutes)
print(result)