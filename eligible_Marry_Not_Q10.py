###10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)gender = input("Enter gender (M/F):")
gender = input("Enter gender M/F:")
age = int(input("Enter age:"))
if(gender == 'M'):
    if(age >= 21):
       print(f'eligible for marrige.')
    else:
        print(f'Not eligible for marrige.')
else:
    if(age > 17):
        print("Eligible for marrige.")
    else:
        print(f"Not eligible for marrige.")
