m = int(input("Escriba un primer numero: "))
n = int(input("Escriba el segundo numero: "))
mod=0
while m % n !=0:
    mod = m % n
    m = n
    n = mod
    
print(f"El minimo comun divisor es {n}")