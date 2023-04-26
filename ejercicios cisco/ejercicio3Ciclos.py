#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar 
# la sumatoria de todos los números ingresados.

suma = 0
while True:
    numero = int(input("Ingrese un numero: "))
    suma += numero
    if numero == 0:
        break
    
print("La suma de los numeros es: ", suma)
    
    
    
    
   