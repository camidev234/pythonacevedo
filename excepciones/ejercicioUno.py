
# #Funcion cuadratica con try except
import math
try:
    print("""
    1. Suma
    2. Resta
    """)
    op = float(input("Ingrese la operacion que desea realizar: "))
    a = float(input("Digite el numero a: "))
    b = float(input("Digite el numero b: "))
    c = float(input("Digite el numero c: "))
    operacionUno  = b ** 2 - (4*a*c)
    if operacionUno < 0.0:
        raise Exception("Indeterminacion")
    rc = math.sqrt(operacionUno) 
    match op:
        case 1:
            opDos = -b + rc
            opTres = opDos / (2*a)
            print(f"El resultado de la funcion cuadratica: {opTres}")
        case 2:
            opDos = -b - rc
            opTres = opDos / (2*a)
            print(f"El resultado de la funcion cuadratica: {opTres}")
except ValueError:
    print("Solo numeros")
except Exception as e:
    print(f"Error: {e}")
except:
    print("Hubo un error durante la ejecucion.")




#FUNCION CUADRATICA SIN EXCEPCIONES
while True:
    print("""
    1. Suma
    2. Resta
    3. Salir
    """)
    op = float(input("Ingrese la operacion que desea realizar: "))
    a = float(input("Digite el numero a: "))
    b = float(input("Digite el numero b: "))
    c = float(input("Digite el numero c: "))

    operacionUno  = b ** 2 - (4*a*c)
    if operacionUno < 0.0:
        print("indeterminacion")
        break
    rc = math.sqrt(operacionUno) 
    match op:
        case 1:
            opDos = -b + rc
            opTres = opDos / (2*a)
            print(f"El resultado de la funcion cuadratica: {opTres}")
        case 2:
            opDos = -b - rc
            opTres = opDos / (2*a)
            print(f"El resultado de la funcion cuadratica: {opTres}")
        case 3:
            break
        






