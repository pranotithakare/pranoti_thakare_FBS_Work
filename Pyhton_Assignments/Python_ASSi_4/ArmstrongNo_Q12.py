###12. WAP to print Armstrong number within a given range
num = int(input("Enter number:"))
temp = num
sum = 0
while(temp>0):
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if(num == sum):
    print(f'Armstrong number.')
else:
    print(f'Is not armstrong number.')