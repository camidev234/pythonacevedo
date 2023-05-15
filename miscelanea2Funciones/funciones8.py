#ejercicio2
import random
def llenarLista(tam):
    lista=[]
    lista=[random.randint(2, 50) for i in range(tam)]
    return lista

lista1=llenarLista(random.randrange(5, 20))
print(lista1)
lista2=llenarLista(random.randrange(5, 20))
print(lista2)

def suma(lista):
    sum=0
    for x in lista:
        sum += x
    return sum

sumaL1=suma(lista1)
print("la suma de la lista uno", sumaL1)
sumaL2=suma(lista2)
print("la suma de la lista dos es.",sumaL2)

def maxSuma(listaUno,listaDos):
    if listaUno > listaDos:
        return f"La suma mas alta la tiene la lista uno porque fue {listaUno}"
    else:
        return f"La suma mas alta la tiene la lista Dos porque fue {listaDos}"
    
print(maxSuma(sumaL1, sumaL2))

def numMayor(mayorlistaUno, mayorlistaDos):
    if mayorlistaUno > mayorlistaDos:
        return f"El mayor lo tiene la lista Uno y es {mayorlistaUno}"
    elif mayorlistaUno == mayorlistaDos:
        return f"El mayor lo tiene la listas es el mismo {mayorlistaUno}, {mayorlistaDos}"
    else:
        return f"el mayor lo tiene la lista Dos y es {mayorlistaDos}"
    
def mayor(lista_Uno, lista_Dos):
    mayorll1=0
    mayorll2=0
    for h in lista_Uno:
        if h > mayorll1:
            mayorll1 = h
    for g in lista_Dos:
        if g > mayorll2:
            mayorll2 = g

    numeroMayor= numMayor(mayorll1, mayorll2)

    return f"{numeroMayor}"

print(mayor(lista1, lista2))

def numMenor(menorlista1, menorlista2):
    if menorlista1 > menorlista2:
        return f"El menor de las doa listas lo tiene la lista dos y es {menorlista2}"
    elif menorlista1 == menorlista2:
        return f"las dos listas tienen el mismo numero menor {menorlista1}, {menorlista2}"
    else:
        return f"el menor de las dos listas lo tine la lista uno y es {menorlista1}"

def menor(lista_uno, lista_dos):
    menorl1=1000000
    menorl2=1000000
    for j in lista_uno:
        if j < menorl1:
            menorl1 = j
    for k in lista_dos:
        if k < menorl2:
            menorl2 = k

    numeroMenor= numMenor(menorl1, menorl2)

    return f"{numeroMenor}"

print(menor(lista1, lista2))


def prom(lista):
    sum=0
    for k in lista:
        sum+=k
    promedio= sum/ len(lista)
    return promedio

promListaUno = prom(lista1)
print("el promedio de la lista uno",promListaUno)
promListaDos = prom(lista2)
print("el promedio de la lista dos es:",promListaDos)

def promConj(listaUno, listaDos):
    
    sumaElementos= sumaL1 + sumaL2
    sumaLong = len(listaUno) + len(listaDos)
    op = sumaElementos / sumaLong

    print(f"el promedio conjunto es : {op}")

    if promListaUno < op:
        return "El promedio de la lista Uno esta por debajo del promedio conjunto"
    elif promListaUno == op or promListaDos == op:
        return "El promedio de la lista y el conjunto son iguales"
    elif promListaDos < op:
        return "El promedio de la lista dos esta por debajo de el conjunto"
    elif promListaUno > op:
        return "El promedio de la lista uno esta por encima del conjunto"
    else:
        return "El promedio de la lista dos esta por encima del promedio conjunto"
    
print(promConj(lista1, lista2))

def pares(lista):
    paresCont=0
    for l in lista:
        if l % 2 == 0:
            paresCont+=1
    return paresCont

paresl1 = pares(lista1)
print(f"La lista uno tiene {paresl1} pares")
paresl2 = pares(lista2)
print(f"La lista dos tiene {paresl2} pares")

def maxPares(pares1, pares2):
    if pares1 < pares2:
        return "La lista dos tiene mas pares que la lista uno"
    elif pares1 > pares2:
        return "La lista uno tiene mas pares que lista dos"
    else:
        return "Ambos tienen la misma cantidad de pares" 

print(maxPares(paresl1, paresl2))   

def impares(lista):
    imparesCont=0
    for h in lista:
        if h % 2 !=0:
            imparesCont+=1
    return imparesCont
imparesl1 = impares(lista1)
print(f"La lista uno tiene {imparesl1} impares")
imparesl2 = impares(lista2)
print(f"La lista dos tiene {imparesl2} impares")

def maxImpares(impares1, impares2):
    if impares1 < impares2:
        return "La lista dos tiene mas impares que la lista uno"
    elif impares1 > impares2:
        return "La lista uno tiene mas impares que lista dos"
    else:
        return "Ambos tienen la misma cantidad de impares" 
    
print(maxImpares(imparesl1, imparesl2))
    