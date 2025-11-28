###1. Python Program to Put Even and Odd elements of a List into two Different lists

def separate_even_odd(numbers):
    even_ele = []
    odd_ele = []
    for num in numbers:
        if num % 2 == 0:
            even_ele.append(num)
        else:
            odd_ele.append(num)
    return even_ele, odd_ele
li = [4, 3, 5, 2, 90]
even_list, odd_list = separate_even_odd(li)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
