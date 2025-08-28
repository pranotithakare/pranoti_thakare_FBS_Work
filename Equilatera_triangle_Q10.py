###10. Write a program to calculate area of an equilateral triangle.
import math

l = float(input("Enter the length of a side: "))

area = (math.sqrt(3) / 4) * (l ** 2)

print(f'Area of equilateral triangle is {area:.2f}')
