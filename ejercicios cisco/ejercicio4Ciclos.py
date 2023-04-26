#Escriba un programa que imprima los numeros del 1 al 100 e 
#imprima cuales de ellos son pares e impares 


i = 0

for i in range(1, 101):
     if i%2==0:
         print(f"El numero {i} es par")
     else:
         print(f"El numero {i} es impar")