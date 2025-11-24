###4. Sum of all odd numbers between 1 to n.
def sumOfOddNo(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    print(f"Sum is {total}")

n = int(input("Enter the value of n: "))
sumOfOddNo(n)
