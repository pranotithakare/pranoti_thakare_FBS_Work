###7. Find the sum of three-digit number.
num = int(input("Enter a three-digit number: "))

hundreds = num // 100              # Get the first digit
tens = (num // 10) % 10            # Get the second digit
units = num % 10                   # Get the third digit

digit_sum = hundreds + tens + units

print(f"Sum of digits = {hundreds} + {tens} + {units} = {digit_sum}")
