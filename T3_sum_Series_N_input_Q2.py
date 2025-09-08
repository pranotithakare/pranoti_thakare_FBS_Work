n = int(input("Enter the value of N: "))
sum_series = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum_series += i / fact
print(f"Sum of the series is: {sum_series:}")

