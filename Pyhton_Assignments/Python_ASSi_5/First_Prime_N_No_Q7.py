###7. Write a program to print first n prime numbers

# Accept how many prime numbers to print
n = int(input("Enter how many prime numbers to print: "))

count = 0       # To count how many primes we have printed
num = 2         # Number to check for prime

print(f"First {n} prime numbers:")

while count < n:
    is_prime = True
    
    # Check if num is prime
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
        count += 1
    
    num += 1

