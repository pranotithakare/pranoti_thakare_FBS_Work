###1. Write a program to check if the given number is positive or negative.

num = int(input("Enter number:"))
if(num > 0):
    print(f"{num} number is positive.")
elif(num < 0):
    print(f'{num} number is negative.')
else:
    print(f'{num} number is zero')