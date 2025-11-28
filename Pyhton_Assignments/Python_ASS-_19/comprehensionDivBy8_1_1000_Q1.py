#______________Assignment on Comprehension_________________
#1. Find all of the numbers from 1–1000 that are divisible by 8
numbers = [ele for ele in range(1, 1001) if ele % 8 == 0]
print(numbers)