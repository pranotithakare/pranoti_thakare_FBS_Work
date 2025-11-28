###1. Create a class Book with members as bid,bname,price and author.Add following
#methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook

class Book:
    def __init__(self,bid,bname,price,author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
    def ShowBook(self):
        return f'BID:{self.bid}\nBNAME:{self.bname}\nPRICE:{self.price}\nAUTHOR:{self.author}'
    def __del__(self):
        print("Destructor is called")
b1 = Book(1,'wings of fire',100,'abdul kalam')
print(b1.ShowBook())

