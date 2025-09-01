#3. Definir una función area_triangulo que reciba la base y la altura de un triángulo
#devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
#Fórmula: area = (b * h) / 2

baseTriangulo = float(input("Ingrese la base del triangulo: "))
alturaTriangulo = float(input("Ingrese la altura del triangulo: "))

area_triangulo = ((baseTriangulo * alturaTriangulo)) / 2

print(f"El area de un triangulo es {area_triangulo}")