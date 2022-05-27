numeros = [12, 84, 13, 20, 33, 101, 9, 2, 15, 21]

def separarlistas(lista):
    numeros.sort(reverse=True)
    pares = []
    impares = []
    for n in numeros:
       
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separarlistas(numeros)

print(impares)
print( pares)
