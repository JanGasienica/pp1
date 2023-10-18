first_person_name  = input("Enter first persons name:" )
first_person_age = int(input("Enter first persons age:" ))
secound_person_name = input("Enter second persons name: ")
secound_person_age = int(input("Enter secound persons age:" ))
if(first_person_age>=18 and secound_person_age>=18):
    print(f"Both {first_person_name} and {secound_person_name} are adults")