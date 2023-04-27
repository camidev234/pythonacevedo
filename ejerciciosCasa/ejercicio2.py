numUno = int(input("Escriba un numero: "))
numDos = int(input("Escriba un numero: "))
restaUno = 0
restaDos = 0
if numUno < numDos:
    resta = numDos - numUno
    print(f"El resultado de la resta entre el mayor y el menor es: {resta}")
else:
    resta = numUno- numDos
    print(f"El resultado de la resta entre el mayor y el menor es: {resta}")
    
while resta != 0:
    if numDos < numUno:
        resta = resta - numDos
        print("El residuo es : ", resta)
    else:
        resta= resta - numUno
        print("El residuo es : ", resta)
    if resta < 0:
        break 