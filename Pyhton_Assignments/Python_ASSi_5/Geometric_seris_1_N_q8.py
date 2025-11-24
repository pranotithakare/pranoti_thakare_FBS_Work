###8. Write a program to solve the following series : 
# a. 1! + 2! + 3! + 4! + …..n! 
# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent) 
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2. 
# d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10
#  e. x - x2/3 + x3/5 - x4/7 + …. to n terms


#a) 1! + 2! + 3! + ... + n!
# Accept n
n = int(input("Enter n for factorial series: "))

sum_fact = 0
fact = 1

for i in range(1, n+1):
    fact *= i        # calculate i!
    sum_fact += fact

print(f"Sum of factorial series 1!+2!+...+{n}! = {sum_fact}")

#(b) N + N^2 + N^3 + ... + N^N
# Accept N
N = int(input("Enter N for N + N^2 + ... + N^N: "))

sum_power = 0

for i in range(1, N+1):
    sum_power += N**i

print(f"Sum of series N + N^2 + ... + N^{N} = {sum_power}")

#(c) Geometric series 1 + 2 + 2^2 + ... + 2^(n-1)

#Common ratio = 2, first term = 1

# Accept n
n = int(input("Enter n for geometric series: "))

sum_geo = 0
term = 1

for i in range(n):
    sum_geo += term
    term *= 2  # multiply by common ratio

print(f"Sum of geometric series 1 + 2 + 4 + ... up to {n} terms = {sum_geo}")
#(d) S = a + a^2 / 2 + a^3 / 3 + ... + a^10 / 10
# Accept a
a = float(input("Enter a for series S = a + a^2/2 + ... + a^10/10: "))

sum_series = 0

for i in range(1, 11):
    sum_series += a**i / i

print(f"Sum of series = {sum_series}")

#(e) x - x^2/3 + x^3/5 - x^4/7 + ... up to n terms
# Accept x and n
x = float(input("Enter x for series x - x^2/3 + ... : "))
n = int(input("Enter number of terms n: "))

sum_alt = 0

for i in range(1, n+1):
    term = x**i / (2*i - 1)  # denominator: 1, 3, 5, 7...
    if i % 2 == 0:            # even term → negative
        term = -term
    sum_alt += term

print(f"Sum of series up to {n} terms = {sum_alt}")
