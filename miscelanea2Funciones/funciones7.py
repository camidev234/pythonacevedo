#ejercicio 11

import random
def llenar(tamaño):
    lista=[]
    lista=[random.randrange(2, 15) for i in range(tamaño)]
    return lista
tam= random.randint(1, 20)
listado= llenar(tam)
print(listado)

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
        
            
hallarFactoriales(listado)