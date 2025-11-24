###9. WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
divisor = int(input("Enter the number to divide by: "))

print(f"Numbers between {start} and {end} divisible by {divisor}:")

for num in range(start, end + 1):
    if num % divisor == 0:
        print(num, end=' ')
