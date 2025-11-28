# 7. Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit.

numbers = [num for num in range(1, 1001) if any(num % d == 0 for d in range(1, 10))]
print(numbers)
