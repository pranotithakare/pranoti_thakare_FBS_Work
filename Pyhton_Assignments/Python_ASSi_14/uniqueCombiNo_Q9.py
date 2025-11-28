###9. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers,
#  adding up to a target number.
def findUni3No(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    print(nums[i], nums[j], nums[k])

numbers = [1, 2, 3, 4, 5, 6]
target = 15

print("Uniqe Combination of 3 numbers that add up to", target, ":")
findUni3No(numbers, target)
