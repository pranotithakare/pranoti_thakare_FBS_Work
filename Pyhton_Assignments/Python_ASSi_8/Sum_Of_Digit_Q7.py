#7. Write a program to find sum of digits of a number.
def sumOfDigits(num):
    sum = 0
    while num > 0:
        rem = num % 10      
        sum += rem          
        num = num // 10     
    print("Sum of digits is:", sum)

num = int(input("Enter any number: "))
sumOfDigits(num)
