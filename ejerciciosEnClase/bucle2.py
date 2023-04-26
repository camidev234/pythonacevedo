#imprimir una serie de nuemeros n, cada vez que encuentre un multiplo de 7 debe indicar

i = int(input("Escriba hasta que numero quiere la serie:"))
numActual= 0

while numActual < i:
    numActual+=1
    print(numActual)
    if numActual % 7 == 0:
        print(f"{numActual} es multiplo de 7")
