import random #se importa la clase random
lista=[] #se crea una lista vacia
cuadrado=[]
tam=random.randint(5,10) #se asigna a tam como un numero aleatorio entre 5 y 10
print(tam) #se imprime tam
for i in range(tam): #ciclo desde uno hasta el numero aleatorio que genero tam
    num=random.randrange(100) #se asigna a num numero aleatorio en un rango de 100
    lista.append(num) #se agrega num a la lista con cada iteracion.
print(lista)

for i in range(len(lista)): #for hasta la longitud de la lista
    cuadrado.append(lista[i]**2) #se agrega el cuadrado de cada indice de lista a la lista cuadrado
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)#se imprime la lista cuadrado
print(sum(lista))#se imprime la suma de los elementos de la lista usando la funcion num