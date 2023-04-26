numUno = int(input("Escriba el numero uno: "))
numDos = int(input("Escriba el numero dos: "))

while numUno % numDos == 1 or numDos % numUno == 1:
    numUno = int(input("Escriba el numero uno: "))
    numDos = int(input("Escriba el numero dos: "))
