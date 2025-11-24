###4. WAP to calculate area of triangle and rectangle

base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))

triangle_area = 0.5 * base * height
rectangle_area = length * breadth

print(f"Area of Triangle = {triangle_area:.2f} square units")
print(f"Area of Rectangle = {rectangle_area:.2f} square units")

