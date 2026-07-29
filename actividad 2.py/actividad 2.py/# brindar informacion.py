# Brindar informacion
consulta = input("Ingresar nombre de artista pelicula o serie:")
match consulta:
    case "bad bunny":
        info = "Cantante y compositor puertorriqueño de musica urbana y trap latino."
    case "spider man":
        info = "Pelicula de superheroe basada en el personaje de marvel comics." 
    case "harry potter":
        info = "Saga de peliculas basadas en la serie de libros de fantasia escritas por la autora britanica J:K Rowling."
    case "Jhon Wick":
        info = "Saga de peliculas de accion protagonizadas por el actor Keanu Reeves."
    case "Robert Dawny Jr":
        info = "Actor estadounidense conocido por interpretar a Iron Man en el universo cinematografico de Marvel."
    case _:
        info = "No se encontro informacion sobre el artista, pelicula o serie ingresada."
print("Informacion sobre", consulta, ":", info)