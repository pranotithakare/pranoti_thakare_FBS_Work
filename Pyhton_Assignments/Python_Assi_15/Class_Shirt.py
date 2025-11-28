###3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .
# Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook

class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
    def ShowShirt(self):
        return f'SID:{self.sid}\nSNAME:{self.sname}\nTYPE:{self.type}\nPRICE:{self.price}\nSIZE:{self.size}'
    def __del__(self):
        print("Destructor is called")
s1 = Shirt(1,'Pranu','formal',500,'L')
print(s1.ShowShirt())
