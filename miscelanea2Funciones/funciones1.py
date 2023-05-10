import random
def llenarLista(tam, rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=llenarLista(10, 30)
print(l1)

def sumar(lista):
    import random
    suma=0
    for x in lista:
        suma+=x
    return suma

print("la suma de los elementos de la lista es: ", sumar(l1))

def promedio(lista):
    promedio= sumar(lista)/len(lista)
    return promedio

print("el promedio de los elementos de la lista es: ", promedio(l1))

def mayor(lista):
    mayor=0
    for t in lista:
        if t > mayor:
            mayor=t
    return f"El mayor de la lista es: {mayor}"

print(mayor(l1))

def Menor(lista):
    menor=1000000
    for t in lista:
        if t < menor:
            menor=t
    return f"El menor de la lista es: {menor}"

print(Menor(l1))

def ordenAsc(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return f"la lista ordenada en orden ascendente: {lista}"

print(ordenAsc(l1))


def ordenDesc(lista):
    for j in range(len(lista)):
        for h in range(j+1, len(lista)):
            if lista[j] < lista[h]:
                aux= lista[j]
                lista[j]=lista[h]
                lista[h]=aux
    return f"lA Lista en orden descendente: {lista}"

print(ordenDesc(l1))
    

def moda(lista):
    max=0
    for n in lista:
        cont=0
        for o in lista:
            if n == o:
                cont+=1
        if cont > max:
            max = cont
            moda1= n
    if cont == max:
        return "no hay moda"
    return f"La moda es {moda1} por que se repitito {max} veces"

print(moda(l1))
