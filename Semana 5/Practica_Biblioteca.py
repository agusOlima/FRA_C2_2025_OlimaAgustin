titulos = [""] * 20
ejemplares = [0] * 20
opcion = 0

while opcion != 7:

    print("Elegir una opción dentro del menu.")
    print("Opción (1) Cargar titulos y ejemplares")
    print("Opción (2) Mostrar catalogo completo")
    print("Opción (3) Consultar disponibilidad")
    print("Opción (4) Listar titulos agotados")
    print("Opción (5) Agregar titulo nuevo")
    print("Opción (6) Actualizar ejemplares")
    print("Opción (7) Salir")

    opcion = int(input("Ingrese el numero de opción: "))

    if opcion == 1 :
        cargar_titulos_y_ejemplares(titulos, ejemplares)
    elif opcion == 2 :
        mostrar_catalogo(titulos, ejemplares)
    elif opcion == 3 :
        
    
        


