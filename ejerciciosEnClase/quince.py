#15. Diseñar e implementar un programa que solicite a su
#usuario un valor no negativo n y visualice la siguiente salida:
#1 2 3 ........ n-1 n
#1 2 3 ........ n-1
#.........
#1 2 3
#1 2
#1

n = int(input("Escriba un numero positivo"))
fila = 0

for i in range(n, 0, -1):
    for h in range(1, i+1, +1):
        print(h, end="")
    print()