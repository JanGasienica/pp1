father_income = int(input("father income: "))
mother_income = int(input("mother income:  "))
number_of_family_members= int(input("number of  family members: "))
totalincome = mother_income + father_income
income_per_person = totalincome/number_of_family_members
print(income_per_person)