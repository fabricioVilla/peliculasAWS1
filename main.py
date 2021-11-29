from objetos.peliculas import Peliculas
from Classes.Busqueda import consultar 
from Classes.Add import crearPelis

ciclo=1
while ciclo==1:
    print("\n\n¿Que operacion deseas realizar?")
    print("Buscar pelicula ingresa 1")
    print("Agregar pelicula ingresa 2")
    print("Buscar pelicula preciona cualquier tecla")
    opcion = input()



    try:
        opcion=int(opcion)
    except :
        print("salir")
        ciclo=2

    if opcion==1:
        consultar(Peliculas)
    elif opcion==2:
        crearPelis(Peliculas)
    





