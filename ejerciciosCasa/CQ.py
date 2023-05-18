import random
lon = random.randrange(50,99)                            
def llenarLista(tamaño):
    lista=[]
    lista=[random.randint(100, 500) for i in range(tamaño)]
    return lista

listado = llenarLista(lon)
print(listado)

# listado=[1,2,3,4,5,6,7,8,9,10,11,12,13]

def ordenAsc(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return f"la lista ordenada en orden ascendente: {lista}"

print(ordenAsc(listado))
def cuartil(lista, lista1, lista2,lista3,lista4):
    formula=0
    n = len(lista)
    listaCuartil=[]
    redondeo=0
    for k in range(1, 4):
        if len(lista) % 2!=0 or len(lista) % 2 == 0:
            pos2=redondeo
            formula=k*(n+1) / 4
            redondeo= round(formula)
            r2=redondeo+1
            promedio= (redondeo+r2)/2 
            posicion=lista[redondeo-1]           
            if k == 1:
                listaCuartil=lista[ :redondeo]
                print(f"cuartil {k} {listaCuartil}")
                lista1= listaCuartil
            elif k == 2:
                listaCuartil=lista[pos2:redondeo]
                lista2=listaCuartil
                print(f"cuartil {k} {listaCuartil}")
            elif k == 3:
                listaCuartil=lista[pos2:redondeo]
                lista3=listaCuartil
                print(f"cuartil {k} {listaCuartil}")
                lista4=lista[redondeo: ]
            
            print(f"Q{k} = {formula} valor: {posicion}")
            
    return lista1,lista2,lista3,lista4
cuartil1=[]
cuartil2=[]
cuartil3=[]
cuartil4=[]            
c1,c2,c3,c4= cuartil(listado,cuartil1,cuartil2,cuartil3,cuartil4)

print(f"Ultima {c4}")

def prom(lista):
    sum=0
    long = len(lista)
    for h in lista:
        sum+=h
    promedio= sum/long
    return promedio

print(f"El promedio de la primera parte de la lista es:", prom(c1))
print(f"El promedio de la segunda parte de la lista es:", prom(c2))
print(f"El promedio de la tercera parte de la lista es:", prom(c3))
print(f"El promedio de la cuarta parte de la lista es:", prom(c4))



def quintil(lista, lista1, lista2, lista3,lista4, lista5):
    formula=0
    n = len(lista)
    listaQuintil=[]
    redondeo=0
    for k in range(1, 5):
        if len(lista) % 2!=0 or len(lista) % 2 == 0:
            pos2=redondeo
            formula=(k*(n+1)) / 5
            redondeo= round(formula)
            r2=redondeo+1
            promedio= (redondeo+r2)/2
            posicion=lista[redondeo-1]  
            if k == 1:
                listaQuintil=lista[ :redondeo]
                print(f"k {k} {listaQuintil}")
                lista1=listaQuintil
            elif k == 2:
                listaQuintil=lista[pos2:redondeo]
                print(f"k {k} {listaQuintil}")
                lista2=listaQuintil
            elif k == 3:
                listaQuintil=lista[pos2:redondeo]
                print(f"k {k} {listaQuintil}")
                lista3=listaQuintil
            elif k == 4:
                listaQuintil=lista[pos2:redondeo]
                print(f"k {k} {listaQuintil}")
                lista4=listaQuintil
                lista5=lista[redondeo:]
                
            print(f"k{k} = {formula} valor: {posicion}")
                
    return lista1,lista2,lista3,lista4,lista5

quintil1=[]
quintil2=[]
quintil3=[]
quintil4=[]
quintil5=[]

k1,k2,k3,k4,k5 = quintil(listado, quintil1,quintil2,quintil3,quintil4,quintil5)
print(f"K5 {k5}")

print(f"El promedio de la primera parte de la lista es:", prom(k1))
print(f"El promedio de la segunda parte de la lista es:", prom(k2))
print(f"El promedio de la tercera parte de la lista es:", prom(k3))
print(f"El promedio de la cuarta parte de la lista es:", prom(k4))
print(f"El promedio de la quinta parte de la lista es: ",prom(k5) )


def buscarCuartil(cuartil, lista):
    formula=0
    posicion=0
    n = len(lista)
    if cuartil > 3:
        return f"El cuartil {cuartil} no existe"
    else:
        formula = cuartil*(n+1)/4
        redondeo= round(formula)
        r2=redondeo+1
        promedio= (redondeo+r2)/2 
        posicion=lista[redondeo-1]   

    return f"El cuartil {cuartil} es {formula} valor: {posicion}"

print(buscarCuartil(int(input("Escriba el cuartil que desea buscar: ")), listado))
        