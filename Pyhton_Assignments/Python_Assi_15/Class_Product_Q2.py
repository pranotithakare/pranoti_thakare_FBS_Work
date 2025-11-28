###2. Create a class Product with members as pid,pname,price and quantity .Add following
#  methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook

class Product:
    def __init__(self,pid,pname,price,quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def ShowProduct(self):
        return f'PID:{self.pid}\nPNAME:{self.pname}\nPRICE:{self.price}\nQUANTITY:{self.quantity}'
    
    def __del__(self):
        (f"Destructor is called")
p1 = Product(1, 'pen', 10, 2)
print(p1.ShowProduct())

