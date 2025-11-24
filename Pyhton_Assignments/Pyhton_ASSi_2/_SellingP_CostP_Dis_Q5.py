###5. WAP to calculate selling price of book based on cost price and discount.
cost_price = float(input("Enter cost price of the book: "))
discount_percent = float(input("Enter discount percentage: "))

discount_amount = (discount_percent * cost_price) / 100
selling_price = cost_price - discount_amount

print(f"Discount Amount: {discount_amount:}")
print(f"Selling Price of the book: {selling_price:}")

