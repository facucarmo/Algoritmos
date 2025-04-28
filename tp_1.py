#5. Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano):
  
    numeros = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return numeros[romano[0]]

    actual = numeros[romano[0]]
    siguiente = numeros[romano[1]]

    if actual < siguiente:
        return (siguiente - actual) + romano_a_decimal(romano[2:])
    else:
        return actual + romano_a_decimal(romano[1:])

print (romano_a_decimal("CMXCIX"))


#22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:

#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#car para encontrarlo;

#c. Utilizar un vector para representar la mochila.

def usar_la_fuerza (mochila, cantidad=0):    

    if len (mochila) == 0:
        return False, cantidad
    
    objeto = mochila[0]
    cantidad += 1

    if objeto == "sable de luz":
        return True, cantidad
    else:
        return usar_la_fuerza(mochila[1:], cantidad)
    
mochila  = ["arma", "casco", "comida","capa", "sable de luz"]

encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"El sable de luz se encontró despues de sacar {objetos_sacados} objetos!")
else:
    print("No se encontró un sable de luz en la mochila.")