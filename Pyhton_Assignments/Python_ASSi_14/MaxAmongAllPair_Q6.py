###6. Write a Python program to find the two numbers whose product is maximum among all the pairs 
# in a given list of numbers. Use the Python set.
def max_product_pair(numbers):
    max_product = float('-inf')  # Start with smallest value
    pair = ()
    unique_pairs = set()  # Using set to avoid repeating same pairs

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            a, b = numbers[i], numbers[j]
            if frozenset((a, b)) not in unique_pairs:
                unique_pairs.add(frozenset((a, b)))
                product = a * b
                if product > max_product:
                    max_product = product
                    pair = (a, b)

    return pair, max_product
num_li = [-25, -10, 5, -20, 3]

res_pair, max_prod = max_product_pair(num_li)

print("Pair with maximum product:", res_pair)
print("Maximum product:", max_prod)
