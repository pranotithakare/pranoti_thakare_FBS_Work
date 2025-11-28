###7. Write a program to find sum of digits using recursion.
def sum_Of_digits(n):
    if n == 0:
        return 0
    else:
        return( n % 10) + sum_Of_digits(n // 10)
num = int(input("Enter a number: "))
res = sum_Of_digits(num)
print(f"sum of digits is:",res)
