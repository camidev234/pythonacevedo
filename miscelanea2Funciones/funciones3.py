#ejercicio 4
import random
def llenarLista(lon):
    lista=[]
    lista=[random.randrange(30) for i in range(lon)]
    return lista

listado= llenarLista(int(input("Escriba la longitud de la lista:")))
print(listado)

def addElement(elemento):
    while elemento not in listado:
        listado.append(elemento)
        elemento = int(input("Escriba el numero que desea agregar: "))
        
    if elemento in listado:
        print(f"El numero {elemento} ya esta en la lista.")
    return f" lista nueva {listado}"

print(addElement(int(input("Escriba el numero que desea agregar: "))))

    