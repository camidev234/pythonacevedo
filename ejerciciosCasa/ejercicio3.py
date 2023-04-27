inicio = int(input("Escriba desde que numero quiere que inicie la serie: "))
fin = int(input("Escriba en que numero quiere que termine la serie: "))
cantidad = int(input("Ecriba el incremento decremento de la serie: "))
e=0
for i in range(inicio, fin + 1, cantidad):
    e+=1
    print(f"serie {e} es igual a: {i}")