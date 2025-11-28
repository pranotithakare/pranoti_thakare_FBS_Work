###10. Write a program to reverse a number using recursion.
def rev_No(n, rev=0):
    if n == 0:
        return rev
    else:
        return rev_No(n // 10,rev * 10 + n % 10)
num = int(input("Enter a number:"))
rev_num = rev_No(num)
print("Reversed number is :", rev_num)
