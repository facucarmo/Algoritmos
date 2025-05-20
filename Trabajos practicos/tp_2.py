#13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe (MCU) de los cuales se conoce 
#el nombre del modelo, nombre de la película en la que se usó y el estado en que quedó al final de la película (Dañado, Impecable, 
#Destruido), resolver las siguientes actividades:

#a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas películas;
#b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
#c. eliminar los modelos de los trajes destruidos mostrando su nombre;
#d. un modelo de traje puede usarse en más de una película y en una película se pueden usar más de un modelo de traje, estos deben 
#cargarse por separado;
#e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
#f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
#“Capitan America: Civil War”.

pila_trajes = [
    {"modelo": "mark III", "pelicula": "iron man", "estado": "dañado"},
    {"modelo": "mark XLIV", "pelicula": "avengers: age of ultron", "estado": "dañado"},
    {"modelo": "mark XLVII", "pelicula": "spider-man: homecoming", "estado": "impecable"},
    {"modelo": "mark XLIV", "pelicula": "capitan america: civil war", "estado": "destruido"},
    {"modelo": "mark L", "pelicula": "avengers: infinity war", "estado": "dañado"},
    {"modelo": "mark LXXXV", "pelicula": "avengers: endgame", "estado": "destruido"}
]

def buscar_hulkbuster(pila):
    peliculas = []
    for traje in pila:
        if traje["modelo"] == "mark XLIV":
            peliculas.append(traje["pelicula"])
    if peliculas:
        print("mark XLIV fue usado en:", peliculas)
    else:
        print("mark XLIV no fue utilizado.")


def mostrar_daniados(pila):
    for traje in pila:
        if traje["estado"] == "Dañado":
            print(f"modelo: {traje['modelo']} - pelicula: {traje['pelicula']}")


def eliminar_destruidos(pila):
    nueva_pila = []
    for traje in pila:
        if traje["estado"] == "destruido":
            print(f"el modelo destruido: {traje['modelo']} de {traje['pelicula']} fue eliminado")
        else:
            nueva_pila.append(traje)
    return nueva_pila


def agregar_modelo(pila, modelo, pelicula, estado):
    for traje in pila:
        if traje["modelo"] == modelo and traje["pelicula"] == pelicula:
            print(f"el modelo {modelo} ya fue cargado para la película '{pelicula}'.")
            return
    pila.append({"modelo": modelo, "pelicula": pelicula, "estado": estado})
    print(f"modelo {modelo} agregado para la película '{pelicula}'.")


def mostrar_por_peliculas(pila, peliculas_buscadas):
    for traje in pila:
        if traje["pelicula"] in peliculas_buscadas:
            print(f"modelo: {traje['modelo']} - pelicula: {traje['pelicula']}")


buscar_hulkbuster(pila_trajes)
print("\nmodelos dañados:")
mostrar_daniados(pila_trajes)

print("\neliminando modelos destruidos...")
pila_trajes = eliminar_destruidos(pila_trajes)

print("\nagregando nuevo modelo:")
agregar_modelo(pila_trajes, "mark LXXXV", "spider-man: no way home", "impecable")

print("\nmodelos en spider-man: homecoming y civil War:")
mostrar_por_peliculas(pila_trajes, ["spider-man: homecoming", "capitan america: civil war"])




#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas
#de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la 
#que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.


pila = [
    {"nombre": "iron man", "peliculas": 10},
    {"nombre": "groot", "peliculas": 5},
    {"nombre": "black widow", "peliculas": 7},
    {"nombre": "captain america", "peliculas": 9},
    {"nombre": "rocket raccoon", "peliculas": 6},
    {"nombre": "doctor strange", "peliculas": 4},
    {"nombre": "gamora", "peliculas": 6}
]


def buscar_posiciones(pila, nombres):
    posiciones = {}
    temp_pila = pila.copy()
    pos = 1
    while temp_pila:
        personaje = temp_pila.pop()
        if personaje["nombre"] in nombres:
            posiciones[personaje["nombre"]] = pos
        pos += 1
    return posiciones

posiciones = buscar_posiciones(pila, ["rocket raccoon", "groot"])
print("posiciones:", posiciones)


def personajes_mas_de_5(pila):
    for personaje in reversed(pila):
        if personaje["peliculas"] > 5:
            print(f"{personaje['nombre']} participó en {personaje['peliculas']} películas.")


personajes_mas_de_5(pila)



def peliculas_black_widow(pila):
    for personaje in pila:
        if personaje["nombre"] == "black widow":
            return personaje["peliculas"]
    return 0

def personajes_por_letras(pila, letras):
    for personaje in reversed(pila):
        if personaje["nombre"][0] in letras:
            print(personaje["nombre"])



personajes_por_letras(pila, {"c", "d", "g"})