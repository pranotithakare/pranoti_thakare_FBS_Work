###7.Write a program to find the Roots of Quadratic Equation.

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c

Root1 = (-b + math.sqrt(D)) / (2 * a)
Root2 = (-b - math.sqrt(D)) / (2 * a)

print(f"Roots of the quadratic equation are: {Root1} and {Root2}")
