numUno = int(input("Escriba un numero: "))
numDos = int(input("Escriba otro numero: "))

while numUno == numDos:
    numUno = int(input("Escriba un numero: "))
    numDos = int(input("Escriba otro numero: "))
    
if numDos > numUno:
    print(f"EL numero mayor es : {numDos}")
else:
    print(f"El numero mayor es {numUno}")
