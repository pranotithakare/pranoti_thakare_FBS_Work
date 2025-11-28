###11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def digit_cnt(num):
    cnt = 0
    while(num != 0):
        num = num // 10
        cnt += 1
    return cnt
def sum_of_pow(num,cnt):
    sum = 0
    while(num != 0):
        rem = num % 10
        sum = sum+(rem**cnt)
        num = num // 10
    return sum
def is_armstrong(num):
    cnt = digit_cnt(num)
    sum = sum_of_pow(num,cnt)
    if(sum == num):
        print(f'{num} is a armstrong number.')
    else:
        print(f'{num} is not armstrong number.')

num = int(input("Enter a number:"))
is_armstrong(num)
