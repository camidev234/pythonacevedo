# con el ciclo while

sumPares = 0
sumImpares = 0
numero = 0
while numero < 100:
    numero+=1
    if numero % 2 == 0:
        sumPares+=numero
    else:
        sumImpares+=numero
        
print(f"la suma de los impares hasta el 50 es {sumImpares}")        
print(f"La suma de los pares hasta el 50 es {sumPares}")