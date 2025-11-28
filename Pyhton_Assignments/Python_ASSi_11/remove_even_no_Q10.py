###10. Write a program to print list after removing even numbers.

def removeNo(li):
    for num in li[:]:  
       if num % 2 == 0:    
          li.remove(num)
    return li
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print("List after removing even numbers:", removeNo(li))
