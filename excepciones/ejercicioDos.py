#While
try:
    numUno = int(input("Escriba el primer numero: "))
    numDos = int(input("Escriba el segundo numero: "))

    div = numUno / numDos

except ValueError:
    print("Solo numeros")
except ZeroDivisionError:
    print("No se puede dividir entre 0")