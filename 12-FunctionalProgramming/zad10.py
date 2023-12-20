def avg_speed(distance,hours,minutes):
    avg_speed = distance/(hours+minutes/60)
    round(avg_speed,1)
    return avg_speed

distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))
print(avg_speed(distance,hours,minutes))