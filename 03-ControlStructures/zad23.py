dogs_age_human_years = float(input("Enter the dog's age in human years: "))
if(dogs_age_human_years<=2):
    print(f"The dog's age in dog’s years is {dogs_age_human_years*10.5} years")
else:
    print(f"The dog's age in dog’s years is {(dogs_age_human_years-2)*4+21} years")