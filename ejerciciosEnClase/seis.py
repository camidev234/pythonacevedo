numero = int(input("Introdusca un numero positivo: "))
numeromax = 0
while numero >= 0:
    if numero > numeromax:
        numeromax = numero
    numero = int(input("Introduca un numero positivo: "))

print(f"{numeromax} es el maximo:")