#Intercambiar elementos pares por ceros:
#Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
#resultante.
array_1 = [0] * 10

for j in range(len(array_1)):
    array_1[j] = int(input(f"ingrese un numero para la posición {j}: "))


def esPar(numero):
    if numero % 2 == 0:
        resultado = True   
    else:
        resultado = False  
    return resultado

for s in range(len(array_1)):
    if esPar(array_1[s]) == True:
        array_1[s] = 0

print(f"La lista de arrays con los pares reemplazados es: {array_1}")
