###8. Write a program to swap two numbers using third variable.

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

temp = a
a = b
b = temp

print("After swapping:")
print(f"a = {a}")
print(f"b = {b}")
