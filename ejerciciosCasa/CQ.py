import random
lon = random.randrange(200, 2500)
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

def cuartil(lista):
    formula=0
    n = len(lista)
    listaCuartil=[]
    conv=0
    # posicionInicial=0
    for k in range(1, 4):
        if len(lista) % 2!=0 or len(lista) % 2 == 0:
            # posicionInicial=conv
            formula=k*(n+1) / 4
            conv=round(formula)
            pos=lista[conv-1]
            print(f"Q{k} = {formula} valor en lista {pos}")
            listaCuartil.append(formula)
            print(listaCuartil)
            # if k == 1:
            #     listaCuartil=lista[ :conv-1]
            #     listaCuartil.append(formula)
            #     print(f"Cuartil {k} {listaCuartil}")
            # elif k == 2:
            #     listaCuartil = lista[posicionInicial-1:conv]
            #     print(f"Cuartil {k} {listaCuartil}")
            # else:
            #     listaCuartil = lista[posicionInicial:conv]
            #     print(f"Cuartil {k} {listaCuartil}")
            
    return "Fin de procedimiento de cuartiles"
            
print(cuartil(listado))

def quintil(lista):
    formula=0
    n = len(lista)
    listaCuartil=[]
    conv=0
    # posicionInicial=0
    for k in range(1, 5):
        if len(lista) % 2!=0 or len(lista) % 2 == 0:
            # posicionInicial=conv
            formula=(k*(n+1)) / 5
            conv=round(formula)
            pos=lista[conv-1]
            print(f"k{k} = {formula} valor en lista {pos}")
            listaCuartil.append(formula)
            print(listaCuartil)

    return "Fin de procedimiento de quintiles"
print(quintil(listado))
        