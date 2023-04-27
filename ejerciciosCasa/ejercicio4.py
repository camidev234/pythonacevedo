numero = int(input("Escriba un numero: "))
n = int(input("Escriba el numero que desea hallar multiplos: "))
cont=0
for i in range(0, numero + 1, 1):
    if i % n == 0:
        cont+=1
        print(f"El numero {i}, es multiplo de {n}")

print(f"Hubieron {cont} numero multiplos de {n}")    