#Invertir orden:
#Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.
numeros = []
for i in range(6):
    valor = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(valor)

print("Array original:", numeros)


invertido = [0] * len(numeros)  

for i in range(len(numeros)):
    invertido[i] = numeros[len(numeros) - 1 - i]

print("Array invertido:", invertido)
