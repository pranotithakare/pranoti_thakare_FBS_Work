###2. WAP to print all odd numbers until n.
n = int(input("Enter a number:"))
print(f'print all odd numbers up to n:')
i = 1
while(i <= n):
    if(i % 2 != 0):
        print(i, end = ' ')
    i += 1