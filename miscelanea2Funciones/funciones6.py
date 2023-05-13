# #ejercicio7

import random
def llenarLista():
    lista =[]
    tam = random.randint(5, 20)
    for i in range(tam):
    # print(f"decena de  {numero} es {dec}")
        numero = random.randrange(30)
        lista.append(numero)
    return lista

listado = llenarLista()
print(listado)

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

print(primos(listado))