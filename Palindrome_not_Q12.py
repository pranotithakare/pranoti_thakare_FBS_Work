###12. Write a program to check if given 3 digit number is a palindrome or not.
# Input
num = int(input("Enter a 3-digit number: "))
if 100 <= num <= 999:
    digit1 = num // 100          # First digit
    digit3 = num % 10            # Last digit
    
    if digit1 == digit3:
        print(f"{num} is a palindrome number.")
    else:
        print(f"{num} is not a palindrome number.")
else:
    print("Please enter a valid 3-digit number.")
