numUno = int(input("Escriba el numero uno: "))
numDos = int(input("Escriba el numero dos: "))

while numUno % numDos == 1 or numDos % numUno == 1:
    print(f"{numUno} y {numDos} no son factor")
    numUno = int(input("Escriba el numero uno: "))
    numDos = int(input("Escriba el numero dos: "))

print(f"{numUno} y {numDos} si son factor")