###5. Write a program to find factorial using recursion.
def recursiveFactNo(n):
    if n == 0:
        return 1
    else:
        return n * recursiveFactNo(n - 1)
n = 5
res = recursiveFactNo(n)
print(res)