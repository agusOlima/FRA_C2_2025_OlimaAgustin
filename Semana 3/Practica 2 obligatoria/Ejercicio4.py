#Contar mayores a un valor:
#Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado

arrgelos = [0] * 8

for j in range(len(arrgelos)):
    arrgelos[j] = float(input(f"ingrese un numero para la posición {j}: "))

contador = 0

for i in range(len(arrgelos)):
    if arrgelos[i] > 100:
         contador = contador + 1
        
print(f"La cantidad de numeros que superan el 100 del arreglo son {contador}")


