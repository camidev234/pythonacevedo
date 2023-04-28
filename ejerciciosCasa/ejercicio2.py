numUno = int(input("Escriba un numero: "))
numDos = int(input("Escriba un numero: "))
if numUno < numDos:
    resta = numDos - numUno
    print(f"El resultado de la resta entre el mayor y el menor es: {resta}")
else:
    resta = numUno- numDos
    print(f"El resultado de la resta entre el mayor y el menor es: {resta}")
    
while resta != 0:
    if numDos < numUno:
        resta = resta - numDos
        print("El resultado de la resta es: ", resta)
    else:
        resta= resta - numUno
        print("El resultado de la resta es: ", resta)
    if resta < 0:
        print(f"El residuo es {resta}")
        break 