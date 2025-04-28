# 1- Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
#número dado.

#f(n)= f(n-1) + f(n-2)

def fib (number):
    if number == 0 or number == 1:
        return number
    else:
        return fib(number - 1 ) + fib(number - 2)

print (fib(10))

# 2- Implementar una función que calcule la suma de todos los números enteros comprendidos
#entre cero y un número entero positivo dado.
    
# suma(n) = n + suma(n-1)  -> suma(0) = 0

def suma (num):
    if num == 1:
        return num
    else: 
        return (num + suma(num - 1))
    
print (suma(5))

# 3-Implementar una función para calcular el producto de dos números enteros dados.

# prod (n,m) = n * prod (n,m) -----> prod (n,m) m == 1 = n

def prod (num,num1):

    if num1 == 1:
        return num
    else:
        return (num + prod (num, num1 - 1))
    
print (prod(2,8))

# 4- Implementar una función para calcular la potencia dado dos números enteros, el primero 
#representa la base y segundo el exponente.

#pot (n,m) = n * pot (n, m-1) --> pot (n,m) m == 1 = n

def potencia(number,number1):
    if number1 == 1:
        return number
    else:
        return number * potencia(number, number1 - 1)

print(potencia(2,10))


#5. Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano):

    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    # Caso base
    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return valores[romano[0]]

    # Obtener el valor del primer y segundo carácter
    primero = valores[romano[0]]
    segundo = valores[romano[1]]

    if primero < segundo:
        # Resta si el primero es menor que el segundo
        return segundo - primero + romano_a_decimal(romano[2:])
    else:
        # Suma si el primero es mayor o igual
        return primero + romano_a_decimal(romano[1:])
    
    print (romano_a_decimal("MCLI"))


#10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def digitos (num):

    if num <= 9:
        return 1
    else:
        return 1 + digitos(num // 10)

print (digitos(15150))


#6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invert (word):

    if word == '':
        return ''
    else: 
        return word [-1] + invert(word[:-1])
        
print (invert("BOLIVIANO"))


#11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.

def invert_number (num,inverted=0):

    if num == 0:
        return inverted
    else:
        inverted = inverted * 10 + num % 10
        return invert_number(num//10,inverted) 
    
print (invert_number(123456789))

#12. Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos números enteros.

def euclides(num,num1):

    if num % num1 == 0:
        return num1
    else: 
        return euclides (num1, num % num1) 


print (euclides(54,3))  
