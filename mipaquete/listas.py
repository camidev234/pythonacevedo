# sumar Lista
import random

# llenado


def completeListRandom(tamaño, r1, r2):
    l = []
    l = [random.randint(r1, r2) for num in range(tamaño)]
    return l

lista1 = completeListRandom(15, 10, 50)
print(lista1)


def sumar(lista):
    suma=0
    for x in lista:
        suma+=x
    return suma


#pares

def countPares(lista):
    cont = 0
    for k in lista:
        if k % 2 == 0:
            cont+=1

    return cont

def countImpares(lista):
    cont = 0
    for h in lista:
        if h % 2 != 0:
            cont+=1

    return cont
# mayor

def mayor(lista):
    mayor=0
    for t in lista:
        if t > mayor:
            mayor=t
    return mayor

#menor

def Menor(lista):
    menor=1000000
    for t in lista:
        if t < menor:
            menor=t
    return menor

#orden ascendente

def ordenAscendente(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return lista


# orden descedente

def ordenDescendente(lista):
    for j in range(len(lista)):
        for h in range(j+1, len(lista)):
            if lista[j] < lista[h]:
                aux= lista[j]
                lista[j]=lista[h]
                lista[h]=aux
    return lista

#moda

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
    return moda1


# mediana

def mediana(lista):
    if len(lista) %2!=0:
        pos = (len(lista)+1)//2
        return lista[pos-1]
    else:
        pos = (len(lista) - 1) // 2
        pos1 = (lista [pos])
        pos2 = (lista[pos + 1])
        pos = pos1 + pos2
        pos = pos / 2
        return pos
    

# hallar elemento y su indice

def posicion(numero, listado):
    listaIndices=[]
    cont=0
    veces=0
    for m in listado:
        if numero in listado:
            True
        else:
            return f"El numero {numero} no esta en la lista"
        cont+=1
        if numero == m:
            veces+=1
            posicion = cont-1
            listaIndices.append(posicion)
    return f"El numero {numero} si esta en la lista, esta {veces} veces, y fue encontrado en la(s) posicion {listaIndices}"


# promedio

def promedio(lista):
    promedio= sumar(lista)/len(lista)
    return promedio

# hallar factorial de cada elememto de la lista

def hallarFactoriales(lista):
    operacion=0
    for j in lista:
        numero=j
        operacion=0
        for k in range(j-1, 0, -1):
            operacion=j*k
            j=operacion
        j=numero
        print(f"El factorial de {j} es {operacion}")

#numeros primos

def primos(lista):
    listaPrimos=[]
    contPrimos =0
    cont=0
    for i in lista:
        cont=0
        for h in range(1, i+1):
            if i % h == 0:
                cont+=1
        if cont == 2:
            contPrimos+=1
            listaPrimos.append(i)
    return f"Hubieron {contPrimos} numeros primos y son: {listaPrimos}"


# suma pares

def sumaPares(lista):
    sum=0
    for n in lista:
        if n %2 ==0:
            sum+=n
    return sum


# suma impares

def promImpares(lista):
    sumIm=0
    prom=0
    cont=0
    for j in lista:
        if j %2 !=0:
            cont+=1
            sumIm+=j
    prom=sumIm/cont
    
    return prom


def buscarPares(lista):
    listaPares = []
    for g in lista:
        if g %2 ==0:
            listaPares.append(g)

    return listaPares

def buscaImpares(lista):
    listaImpares = []
    for g in lista:
        if g %2 != 0:
            listaImpares.append(g)

    return listaImpares





