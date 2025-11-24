###5. WAP to print Fibonacci series upto n.
n = int(input("Enter how many fibonacci number you want: "))
a = -1
b = 1
for i in range(n):
    c = a + b
    print(c, end = ' ')
    a = b
    b = c #a,b = b,c
    