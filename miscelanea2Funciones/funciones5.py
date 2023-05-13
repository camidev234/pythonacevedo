#ejercicio 8

import random
def llenarLista():
    lista =[]
    tam = random.randint(5, 20)
    for i in range(tam):
    # print(f"decena de  {numero} es {dec}")
        numero = random.randrange(30)
        lista.append(numero)
    return lista

listado = llenarLista()
print(listado)

def sumaPares(lista):
    sum=0
    for n in lista:
        if n %2 ==0:
            sum+=n
    return f"la suma de los pares es: {sum}"

print(sumaPares(listado))

def promImpares(lista):
    sumIm=0
    prom=0
    cont=0
    for j in lista:
        if j %2 !=0:
            cont+=1
            sumIm+=j
    prom=sumIm/cont
    
    return f"el promedio de los impares de la lista es: {prom}"

print(promImpares(listado))
    


