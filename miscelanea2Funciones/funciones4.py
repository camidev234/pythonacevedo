
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
    dec=numero+10
    if numero > mayor:
        mayor= numero
        lista.append(numero)
    else:
        print(f"El numero {numero} es menor a {mayor}")
    # if numero > dec:
    #     print(f"El numero {numero} es mayor a la decena {dec}")
    # else:
    #     print(f"El numero no cumple las dos condiciones {numero}")
    # if numero < mayor:
    #     print(f"El numero {numero} es menor a {mayor}")
        
print(lista)