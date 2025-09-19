#Mayor y su posición:
#Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
#encuentra.

arreglos = [0] * 7

for j in range(len(arreglos)):
    arreglos[j] = float(input(f"ingrese un numero para la posición {j}: "))

mayor = arreglos[0]
num_posición = 0
num_posición_mayor = 0

for i in range(len(arreglos)):
    if arreglos[i] > mayor:
        mayor = arreglos[i]
        num_posición = num_posición + 1
        num_posición_mayor = num_posición
    else: 
        num_posición = num_posición + 1

print(f"El numero mas grande del arreglos es {mayor}, en la posición {num_posición_mayor}.")