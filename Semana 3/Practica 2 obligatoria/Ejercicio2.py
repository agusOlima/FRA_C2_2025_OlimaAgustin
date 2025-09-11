#Sumar todos los elementos:
#Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
#elementos.

numeros_ent = [0] * 10

for j in range(len(numeros_ent)):
    numeros_ent[j] = int(input(f"ingrese un numero para la posición {j}: "))

acumulador_suma = 0

for g in range(len(numeros_ent)):
    acumulador_suma = acumulador_suma + numeros_ent[g]

print(f"La suma total del arreglo {numeros_ent} es de {acumulador_suma}")

