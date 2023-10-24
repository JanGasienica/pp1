time = float(input("Enter what time is it: "))
if time >12:
    print(f"Time in 12-hour format: {time - 12}pm")
else:
    print(time)