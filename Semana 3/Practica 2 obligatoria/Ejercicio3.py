#Promedio de valores:
#Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
#de los valores.

arreglos = [0] * 6

for j in range(len(arreglos)):
    arreglos[j] = float(input(f"ingrese un numero para la posición {j}: "))

acumulador_suma = 0

for h in range(len(arreglos)):
    acumulador_suma = acumulador_suma + arreglos[h]

def promedio (num1, num2) :
    resultado = num1 / num2
    return resultado

cantidad_arreglos = len(arreglos)

print(f"El promedio del arreglo {arreglos} es de {promedio (acumulador_suma, cantidad_arreglos)}")
