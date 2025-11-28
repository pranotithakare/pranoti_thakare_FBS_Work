#8. Write a program find reverse of a number.
def revNo(num):
    rev = 0
    while num > 0:
        rem = num % 10         # Get last digit
        rev = rev * 10 + rem   # Build reversed number
        num = num // 10        # Remove last digit
    print("Reversed number is:", rev)

num = int(input("Enter a number: "))
revNo(num)

