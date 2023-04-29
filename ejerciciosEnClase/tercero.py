numero = int (input("ingrese un numero"))
suma = 0

for i in range (1,numero + 1): 
    if numero %  i ==0:
        print("el numero ", i , "es divisor de",numero   )
        suma+=i
        
resta = suma -numero
if resta == numero:
    print(f"el numero {numero} es perfecto") 
else:
    print(f"El numero {numero} no es perfecto")