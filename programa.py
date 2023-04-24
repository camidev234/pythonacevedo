numero1 = int(input("Escriba el numero 1: "))
numero2 = int(input("Escriba el numero 2: "))
numero3 = int(input("Escriba el numero 3: "))
numeromax =0

if numero1 > numero2:
    if numero1 > numero3:
        print(f"El numero mayor es {numero1}")
    else:
        print(f"El numero mayor es {numero3}")
else:
    print(f"El numero mayor {numero2}")