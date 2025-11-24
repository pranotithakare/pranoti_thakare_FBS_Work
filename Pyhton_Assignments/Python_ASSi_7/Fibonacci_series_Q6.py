###6. Write a program to find print the following Fibonacci series using functions:
#1 1 2 3 5 8 n terms
###Using Type 2 
def fibonacciSeries(n):
    a = 1
    b = 1
    print(a, b, end=' ')
    for i in range(n - 2):
        c = a + b
        print(c, end=' ')
        a = b
        b = c

n = int(input("Enter how many fibonacci numbers you want: "))
fibonacciSeries(n)
