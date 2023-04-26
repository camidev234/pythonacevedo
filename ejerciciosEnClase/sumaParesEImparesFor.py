#con el ciclo for
sum = 0
sumImpares = 0

for i in range(1, 100 + 1):
    if i % 2==0:
        sum+=i
    else:
        sumImpares+=i
        
print(f"La suma de los numeros pares hasta el 100 es: {sum}")
print(f"La suma de los numeros impares hasta el 100 es: {sumImpares}")


    
        
