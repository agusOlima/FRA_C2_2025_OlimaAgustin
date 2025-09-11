#Cargar y mostrar array:
#Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
#ciclo for.

numeros = [0] * 5

for j in range(5):
    numeros[j] = int(input(f"ingrese un numero para la posición {j}: "))

print (f"Los numeros del arreglo son: {numeros}")