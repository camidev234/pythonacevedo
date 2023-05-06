import random
lista = []
tam = random.randint(15, 20)
cont1 = 0
lista2 = []   

for i in range(tam):
    num= random.randrange(0,9)
    lista.append(num)    
print(lista)

numero = int(input("Ingrese un numero: "))
while numero not in lista:
    numero = int(input("Ingrese un numero: "))

if numero in lista:
    print(f"El numero {numero} si esta")    


for n in lista:
    cont=0
    for j in lista:
        posicion = cont1
        if numero == j:
            lista2.append(posicion)
        cont1 += 1
        if posicion > tam:
            break     

for n in lista:
    cont=0
    for j in lista:
        posicion = cont1
        if numero == j:
            cont+=1
if cont == 1:
    print(f"El numero {numero} no se repite")            
print(f"El numero {numero} esta {cont} veces")

for s in lista2:
    indice = s
    print(f" el numero {numero} se encontro en la posicion {indice}")