###1. Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!
#Note : For fact and sum two recursive functions
# Recursive function to calculate factorial
def factNo(n):
    if n == 0:
        return 1
    else:
        return n * factNo(n - 1)

# Recursive function to calculate sum of series
def sumOfSeries(n):
    if n == 0:
        return 0
    else:
        return factNo(n) + sumOfSeries(n - 1)

# Main program
num = int(input("Enter a number: "))
res = sumOfSeries(num)
print(f"Sum of {num} number of series is: {res}")


