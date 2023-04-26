paises = [input("Escriba un pais: "), input("Escriba otro pais: "), input("Escriba el ultimo pais: ")]

for pais in paises:
    if pais == paises[1]:
        continue
    print(pais)

palabra = input("Escriba una palabra")
palabra = palabra.upper()

for letra in palabra:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    print(letra)
