###1. Write a program to calculate area of rectangle.
def areaOfRect():
    length = int(input("Enter a length: "))
    breadth = int(input("Enter a breadth:"))
    area = length * breadth
    print(f'area of rectangle is', area)
areaOfRect()