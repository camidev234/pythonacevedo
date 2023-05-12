#ejercicio 4
import random
def llenarLista(lon):
    lista=[]
    for j in range(lon):
        numero= random.randrange(30)
        if numero not in lista:
           lista.append(numero)
        else:
           print(f"El numero {numero} ya esta en la lista") 
    return lista

listado= llenarLista(int(input("Escriba la longitud de la lista:")))
print(listado)


    