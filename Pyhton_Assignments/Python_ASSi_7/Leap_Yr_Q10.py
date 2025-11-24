###10. Write a program to check if entered year is a leap year or not.
def leap_Yr_Or_Not(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")
year = int(input("Enter year: "))
leap_Yr_Or_Not(year)

