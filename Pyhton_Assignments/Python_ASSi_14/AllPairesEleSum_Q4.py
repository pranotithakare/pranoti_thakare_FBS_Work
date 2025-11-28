###4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
def find_pairs_with_sum(numbers, sum):
    pairs = []  # to store result
    seen = set()  # to track visited numbers

    for num in numbers:
        complement = sum - num
        if complement in seen:
            pairs.append((complement, num))  # found a valid pair
        seen.add(num)  # add current number to seen set

    return pairs

num_list = [1, 3, 2, 2, 4, 5, -1, 6]
value = 5

res = find_pairs_with_sum(num_list, value)
print(f"Pairs with sum {value}:", res)
