# 1. Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper


@memoize
def add(a, b):
    print(f"Computing {a} + {b}")
    return a + b

print(add(2, 3))  # Computes and caches
print(add(2, 3))  # Returns cached result
print(add(4, 5))  # Computes and caches



