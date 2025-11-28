###6. Write a program to print Fibonacci series using recursion.
def fibo(n,a,b):
    if(n>0):
        c = a+b
        print(c, end = " ")
        fibo(n-1,b,c)
n = 5
fibo(n,-1,1)