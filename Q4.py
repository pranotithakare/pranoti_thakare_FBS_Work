###Q4.Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior andexterior wall.

interior_area = float(input("Enter total area of interior walls in sq.m: "))
interior_cost = float(input("Enter cost per sq.m interior painting: "))

exterior_area = float(input("Enter total area of exterior walls in sq.m: "))
exterior_cost = float(input("Enter cost per sq.m exterior painting: "))

total_interior_cost = interior_area * interior_cost
total_exterior_cost = exterior_area * exterior_cost

total_cost = total_interior_cost + total_exterior_cost 

print(f'Interior painting cost: ', total_interior_cost)
print(f'Exteerior painting cost: ', total_exterior_cost)
print('Total Painting cost: ', total_cost )

