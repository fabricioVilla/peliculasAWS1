from peliculas import Peliculas


Peliculas
def obtener_peliculas(Peliculas2):
    Peliculas = Peliculas2

def consultar(Pelicula):
    opcion = input("Consultar por \n(1) nombre \n(2) año\n(3) Ver todo\n")
    try:
        opcion=int(opcion)
    except :
        print("salir")
    if opcion == 1:
        nombre = str(input("Nombre:\n"))
        buscar('nompre',nombre)
    elif opcion == 2:
        genero = input("año:\n")
        buscar('fecha_de_estreno',genero)
    elif opcion ==3:
        for i in Pelicula:
            print(i,"\n\n")
    else:
        print("Incorrecto")


def buscar(opcion, valor):
    for v in Peliculas:
        if v[opcion]==valor:
            print(v)

consultar(Peliculas)