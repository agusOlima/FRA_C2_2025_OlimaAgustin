#Función para buscar la primera aparición de un valor:
#Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
#la posición de la primera aparición de ese número o -1 si no se encuentra

cantidadDeElementos = int(input("Ingrese la cantidad de elemntos que tendra el array: "))

array = [0] * cantidadDeElementos

for j in range(len(array)):
    array[j] = int(input(f"ingrese un numero para la posición {j}: "))

numABuscar = int(input("Ingrese un numero entero para buscarlo en el arreglo: "))

posiciónDeAparición = -1

for g in range(len(array)):
    if array[g] == numABuscar:
        posiciónDeAparición == array[g]

print(f"la primera aparición de {numABuscar} es en {posiciónDeAparición}")




