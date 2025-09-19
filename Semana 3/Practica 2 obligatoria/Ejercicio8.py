# Comparar dos arrays:
#Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
#y mostrar un mensaje indicando si son o no iguales.

array_1 = [0] * 5

for j in range(len(array_1)):
    array_1[j] = float(input(f"ingrese un numero, para el primer array, para la posición {j}: "))

array_2 = [0] * 5

for y in range(len(array_2)):
    array_2[j] = float(input(f"ingrese un numero, para el segundo array, para la posición {y}: "))

def losArraySonIguales():
    if (array_1[0] == array_2[0]) and (array_1[1] == array_2[1]) and (array_1[2] == array_2[2]) and (array_1[3] == array_2[3]) and (array_1[4] == array_2[4]):
        resultado = True
    else:
        resultado = False
    return resultado


if losArraySonIguales() == True:
    print("Ambos arrays son iguales.")
else: 
    print("Los arrays no son iguales")




