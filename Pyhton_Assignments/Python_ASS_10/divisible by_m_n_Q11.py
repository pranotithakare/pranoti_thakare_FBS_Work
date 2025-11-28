####11. Write a program to print all numbers which are divisible by m and n in the list.
li = [10, 34, 56, 78, 56]

m = int(input("Enter value for m: "))
n = int(input("Enter value for n: "))
if m == 0 or n == 0:
    print("Division by zero is not allowed!")
else:
    print(f"Numbers divisible by both {m} and {n} are:")
    for ele in li:
        if ele % m == 0 and ele % n == 0:
            print(ele)
