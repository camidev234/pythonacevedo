import random

aleatorio = random.randrange(1, 50, 1)
print(
    "------------------"
    "Adivine el numero"
    "------------------"
)
numero = int(input("Escriba el numero: "))

while numero!=aleatorio:
    numero = int(input("Escriba el numero: "))
    if numero < aleatorio:
        print("El numero que usted introdujo es menor al numero aleatorio")
    elif numero > aleatorio:
        print("El numero aleatorio es menor")
    else:
        print("¡El numero es correcto!")