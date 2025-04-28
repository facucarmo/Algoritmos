def usar_la_fuerza(mochila, cantidad=0):
    """
    Función recursiva que saca objetos de la mochila hasta encontrar un sable de luz,
    o hasta que no haya más objetos. Devuelve una tupla (encontrado, cantidad de objetos sacados).
    """
    if len(mochila) == 0:
        # Caso base: mochila vacía, no se encontró el sable
        return False, cantidad

    objeto = mochila[0]
    cantidad += 1

    if objeto == "sable de luz":
        # Se encontró el sable
        return True, cantidad
    else:
        # No es el sable, seguir buscando
        return usar_la_fuerza(mochila[1:], cantidad)
    
    # Mochila con varios objetos
mochila = ["cuerda", "comunicador", "bláster", "sable de luz", "comida", "medpack"]

# Usar la fuerza para encontrar el sable
encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"¡Sable de luz encontrado después de sacar {objetos_sacados} objetos!")
else:
    print("No se encontró un sable de luz en la mochila.")