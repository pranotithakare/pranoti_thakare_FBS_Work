###4.Write a program to input all sides of a triangle and check whether triangle is valid or not.
a = int(input("Enter First side:"))
b = int(input("Enter Second side:"))
c = int(input("Enter Third side:"))
if(a > 0 and b > 0 and c > 0):
    if(a + b > c) and (a + c > b) and (b + c > a):
        print(f'Triangle is valid.')
    else:
        print(f'Triangle is not valid.')
else:
    print(f'Invalid triangle.')