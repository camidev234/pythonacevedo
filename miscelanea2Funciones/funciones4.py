
import random


lista =[]
mayor=0
numero=1
dec=0
tam = random.randint(5, 20)
print(tam)

for i in range(tam):
    # print(f"decena de  {numero} es {dec}")
    numero = random.randrange(30)
    if i ==0:
        mayor=numero
        dec = mayor + 10
        lista.append(numero)
    print(numero)
    if numero > mayor and numero <=dec:
        lista.append(numero)
    
    

    # if numero > dec:
    #     print(f"El numero {numero} es mayor a la decena {dec}")
    # else:
    #     print(f"El numero no cumple las dos condiciones {numero}")
    # if numero < mayor:
    #     print(f"El numero {numero} es menor a {mayor}")
        
print(lista)