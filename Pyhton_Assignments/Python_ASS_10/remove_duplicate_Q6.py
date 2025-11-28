###6. Write a program to remove duplicates from the list.
# li = [10,20,90,45,90,34]
def newList(original_li):
    new_li=[]
    for i in original_li:
        if i not in new_li:
            new_li.append(i)  ##Add unique element in list
            
    return new_li    
li=[10,10,20,20,30,40,50]       
res=newList(li)
print("orignal list:",li)
print("list after removing dublicate",res)