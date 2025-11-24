###4. WAP to print factorial of a number .
num = int(input("Enter a number: "))
i = 1
fact = 1

while i <= num:
    fact *= i
    i += 1

print("The factorial of", num, "is", fact)
