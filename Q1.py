###Q1.Write a program to find the area and perimeter of following figure (Accept thelength, breadth and radius from user)

length = int(input("Enter the Length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))
area_rectangle = length * breadth
perimeter_rectangle = 2 * (length * breadth)

area_circle = 3.14 * radius ** 2
circumference_circle = 2 * 3.14 * radius

print(f'Area of rectangle: ', area_rectangle)
print(f'perimeter of rectangle: ', perimeter_rectangle)

print(f'Area of circle :', area_circle)
print(f'Circumference of circle :', circumference_circle)

