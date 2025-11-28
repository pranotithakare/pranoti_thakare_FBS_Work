###4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
def generate_square_dict(n):
    square_dict = {}
    for x in range(1, n+1):
        square_dict[x] = x * x
    return square_dict
n = 5
res = generate_square_dict(n)
print("Generated Dictionary:", res)
