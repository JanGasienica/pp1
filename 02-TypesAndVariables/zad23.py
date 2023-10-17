import math
n1 = int(input("Enter a: "))
n2 = int(input("Enter b: "))
n3 = int(input("Enter c: "))
s=(n1+n2+n3)/2
herons_formula_for_triangle_area = math.sqrt(s*(s-n1)*(s-n2)*(s-n3))
triangle_circumference = n1+n2+n3
print(f"Triangle area: {herons_formula_for_triangle_area}")
print(f"Triangle circumference: {triangle_circumference}")