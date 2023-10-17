height_cm = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
height_m=height_cm/100
bmi = weight/height_m**2
print(f"Your BMI index: {bmi}")
correct_bmi = bmi>=18.5 and bmi < 25
print(f"Correct weight: {correct_bmi}")