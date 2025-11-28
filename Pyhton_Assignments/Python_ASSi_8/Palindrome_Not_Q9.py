###9. Write a program to check if entered number is a palindrome or not.
#Using Type 4
def palindromeNo(num):
    temp = num
    rev = 0
    while(temp > 0):
        rem = temp % 10
        rev = (rev * 10) + rem
        temp = temp // 10
    return num == rev
num = int(input("Enter a number:"))
if(palindromeNo(num)):
    print(f'{num} is a palindrome number.')
else:
    print(f'{num} is not palindrome number.')
