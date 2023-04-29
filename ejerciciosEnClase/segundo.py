i=0
cont=0
num = int(input("Escriba un numero: "))
while num <=0:
    num = int(input("Escriba un numero: "))
while num > 1:
    i+=1
    if num % i==0:
        cont+=1
        
    if num == i:
        if cont == 2:
            print(f"El numero {num} es primo")
        else:
            print(f"El numero {num} no es primo")
        break

    