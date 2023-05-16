import random
lon = random.randrange(30, 35)
def llenarLista(tamaño):
    lista=[]
    lista=[random.randint(100, 500) for i in range(tamaño)]
    return lista

listado = llenarLista(lon)
print(listado)

listado = [1,2,3,4,5,6,7,7,8,8,10,11]


def ordenAsc(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return f"la lista ordenada en orden ascendente: {lista}"

print(ordenAsc(listado))

def Cuartil(lista):
    listaCuartil=[]
    cuart2=0
    cuart=0
    posicion=0
    op=0
    op2=0
    n=len(lista)
    for m in range(1,4):
        posicion=op2
        cuart= (m * (n+1))/4
        print(cuart)
        cuart2=int(cuart)
        o=cuart2+1
        op=(cuart+o)/2
        op2=int(op)
        print(op2)
        if m == 1:
            listaCuartil=lista[ :op2]
            print(f"Cuartil {m} {listaCuartil}")
        else:
            listaCuartil=lista[posicion:op2]
            print(f"Cuartil {m} {listaCuartil}")

Cuartil(listado)