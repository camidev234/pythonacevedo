import random
#Primer punto
def llenarLista(tam, rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=llenarLista(random.randint(10, 20), 30)
#Punto A
print(l1)

#PUNTO B
def sumar(lista):
    import random
    suma=0
    for x in lista:
        suma+=x
    return suma

print("la suma de los elementos de la lista es: ", sumar(l1))

#PUNTO C
def promedio(lista):
    promedio= sumar(lista)/len(lista)
    return promedio

print("el promedio de los elementos de la lista es: ", promedio(l1))

#PUNTO D
def mayor(lista):
    mayor=0
    for t in lista:
        if t > mayor:
            mayor=t
    return f"El mayor de la lista es: {mayor}"

print(mayor(l1))

#PUNTO E
def Menor(lista):
    menor=1000000
    for t in lista:
        if t < menor:
            menor=t
    return f"El menor de la lista es: {menor}"

print(Menor(l1))

#PUNTO F
def ordenAsc(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return f"la lista ordenada en orden ascendente: {lista}"

print(ordenAsc(l1))


#PUNTO G
def ordenDesc(lista):
    for j in range(len(lista)):
        for h in range(j+1, len(lista)):
            if lista[j] < lista[h]:
                aux= lista[j]
                lista[j]=lista[h]
                lista[h]=aux
    return f"lA Lista en orden descendente: {lista}"

print(ordenDesc(l1))
    
#PUNTO H
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
    return f"La moda es {moda1} por que se repitito {max} veces"

print(moda(l1))

#PUNTO I
def mediana(lista):
    if len(lista) %2!=0:
        pos = (len(lista)+1)//2
        return f"La mediana de la lista es: {lista[pos-1]}"
    else:
        pos = (len(lista) - 1) // 2
        pos1 = (lista [pos])
        pos2 = (lista[pos + 1])
        pos = pos1 + pos2
        pos = pos / 2
        return f"La mediana de la lista es {pos}"

print(mediana(l1))

#PUNTO J
def posicion(numero):
    listaIndices=[]
    cont=0
    veces=0
    for m in l1:
        if numero in l1:
            True
        else:
            return f"El numero {numero} no esta en la lista"
        cont+=1
        if numero == m:
            veces+=1
            posicion = cont-1
            listaIndices.append(posicion)
    return f"El numero {numero} si esta en la lista, esta {veces} veces, y fue encontrado en la(s) posicion {listaIndices}"
        
print(posicion(int(input("Escriba el numero que quiere buscar: "))))