###5. Sum of all prime numbers between 1 to n.
def sum_Of_All_prime_No(n):
    sum = 0
    for i in range(2, n+1):          # Loop through 2 to n
        for j in range(2, i):        # Check if i is divisible by any number before it
            if i % j == 0:
                break                # If divisible, break → not a prime
        else:
            sum += i                # If loop wasn't broken, i is prime → add to sum
    print("Sum of all prime numbers is", sum)

n = int(input("Enter a number: "))  # User input
sum_Of_All_prime_No(n)