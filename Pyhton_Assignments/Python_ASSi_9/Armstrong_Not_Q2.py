###2. Write a program to check if given number is Armstrong or not using recursive function.
def digit_cnt(n):
    if n == 0:
        return 0
    return 1 + digit_cnt(n // 10)
def armstrongNORecursive(n,power):
    if n == 0:
        return 0
    digit = n % 10
    return(digit ** power) + armstrongNORecursive(n // 10,power)
num = int(input("Enter a number:"))
num_digits = digit_cnt(num)
res = armstrongNORecursive(num, num_digits)
if(res == num):
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not armstrong number.")
