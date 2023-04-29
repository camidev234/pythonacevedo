numero = int (input("ingrese bun numero"))
i=0
while True:
    i+=1
    if numero % i ==0:
        print(f"El numero {i} es divisor de {numero}")
        
    if numero==i:
        break