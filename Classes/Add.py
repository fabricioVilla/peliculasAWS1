def crearPelis(pelis):
    opcion3 = "S"
    while opcion3 == "S":
        nombre = input('Nombre de la pelicula: ')
        generos = input("Ingrese el genero: ")
        duracion = input("Ingrese la duración: ")
        en_exposicion = input("Está disponible?: ")
        fecha_de_estreno = input("Fecha de estrno:")
        Data = {'nompre': nombre, "generos": generos, "duracion": duracion,
                "en_exposicion": en_exposicion, "fecha_de_estreno": fecha_de_estreno}
        pelis.append(Data)
        #print(pelis)
        opcion3 = input(" Deseas agregar otro? S/N > ")
        opcion3.upper()
        print("Regresa pronto")
