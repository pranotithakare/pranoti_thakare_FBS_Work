# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.
def my_range(start, stop, step=1):
    if step == 0:
        raise ValueError("step argument must not be zero")
    
    num = start
    if step > 0:
        while num < stop:
            yield num
            num += step
    else:  # step < 0
        while num > stop:
            yield num
            num += step

# Example usage
for i in my_range(1, 10, 2):
    print(i, end=' ')
