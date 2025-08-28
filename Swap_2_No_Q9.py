###9. Write a program to swap two numbers without using third variable.
print(f"a = {a}")
print(f"b = {b}")

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

a = a + b
b = a - b
a = a - b
print("After swapping:")
print(f"a = {a}")
print(f"b = {b}")
