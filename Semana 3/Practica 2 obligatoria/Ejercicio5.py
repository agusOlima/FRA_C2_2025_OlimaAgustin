#Buscar un valor:
#Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
#Informar la posición en caso afirmativo, o indicar que no se encuentra.

arrgelos = [0] * 10

num_verificar = float(input(f"Ingrese un numero a verificar en el arreglos: "))

for j in range(len(arrgelos)):
    arrgelos[j] = float(input(f"ingrese un numero para la posición {j}: "))

num_posición = 1
 
for j in range(len(arrgelos)):
    if num_verificar == arrgelos[j]:
        print(f"El numero a verificar con el {num_verificar} esta en la posicisión {num_posición}")
    elif num_verificar == arrgelos[j]:
         num_posición = num_posición + 1
    else:
        print(f"No existe el numero indicado en el arreglo.")
        

        

