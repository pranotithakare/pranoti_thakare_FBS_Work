###5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("Enter equilateral triangle:"))
b = int(input("Enter isosceles triangle:"))
c = int(input("Enter scalene triangle:"))
if(a + b > c and a + c > b and b + c > a):
    if(a == b == c ):
        print(f'Equilateral triangle.')##3 sides are equal
    elif(a == b or a == c or c == b):
        print(f'isosceles triangle.')##2 sides are equal
    else:
        print(f'scalene triangle.')##1 side are equal
else:
    print(f'Not a valid triangle.')