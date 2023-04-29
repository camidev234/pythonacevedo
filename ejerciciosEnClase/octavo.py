#Determinar cuales son los múltiplos de 5 comprendidos entre 1 y n
n=int(input("Escriba un numero: "))
for i in range(1, n+1):
    if i%5==0:
        print(f"el numero {i} es multiplo de 5")