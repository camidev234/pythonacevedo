import random
lon = random.randrange(30, 35)
def llenarLista(tamaño):
    lista=[]
    lista=[random.randint(100, 500) for i in range(tamaño)]
    return lista

listado = llenarLista(lon)
print(listado)




def ordenAsc(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return f"la lista ordenada en orden ascendente: {lista}"

print(ordenAsc(listado))


def mediana(lista):
    listamed1=[]
    listamed2=[]
    if len(lista) %2!=0:
        pos = (len(lista)+1)//2
        listamed1=lista[ :pos]
        listamed2=lista[pos: ]
        print(listamed1)
        print(listamed2)
        return f"La mediana de la lista es: {lista[pos-1]}"
    else:
        pos = (len(lista) - 1) // 2
        pos1 = (lista [pos])
        pos2 = (lista[pos + 1])
        pos = pos1 + pos2
        pos = pos / 2
        return pos
    
media = mediana(listado)
print(f"La mediana de la lista es: {media}")



# def Cuartil(lista):
#     i=1
#     listaCuartil=[]
#     cuart2=0
#     cuart=0
#     posicion=0
#     op=0
#     n=len(lista)
#     for m in range(1,4):
#         posicion=cuart2
#         cuart= (i * (n+1))/4
#         cuart2=int(cuart)
#         print(cuart, cuart2)
        
              
#         i+=1

# Cuartil(listado)