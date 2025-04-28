#3. Implementar una función para calcular el producto de dos números enteros dados.

def prod (num, num1):
    if num1 == 1:
        return num
    else:
        return num * prod(num1 - 1)

print (prod(5,3))