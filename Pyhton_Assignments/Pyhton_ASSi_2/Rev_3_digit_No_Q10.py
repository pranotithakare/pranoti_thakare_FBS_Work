###10. Write a program to reverse three-digit number.
num = int(input("Enter a three-digit number: "))

hundreds = num // 100        # First digit
tens = (num // 10) % 10      # Second digit
units = num % 10             # Third digit

reversed_num = (units * 100) + (tens * 10) + hundreds
print(f"Reversed Number: {reversed_num}")
