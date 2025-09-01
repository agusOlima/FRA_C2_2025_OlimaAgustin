#2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
#resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la función.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2

print(f"El resultado de la suma es {suma}. de la resta es {resta}, y de la multiplicación es {multiplicación}")