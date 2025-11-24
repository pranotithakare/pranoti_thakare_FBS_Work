###1. WAP to print all even numbers until n.

n = int(input("Enter the value of n: "))
print(f"Even numbers from 1 to {n} are:")
i = 1
while i <= n:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1
