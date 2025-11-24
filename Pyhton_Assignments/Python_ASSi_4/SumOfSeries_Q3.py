###3. WAP to print sum of series upto n.
n = int(input("Enter value of n numbers:"))
sum = 0
i = 1
while(i <= n):
    sum = sum + i
    i += 1
print(f'sum of series upto n numbers is :{sum}')