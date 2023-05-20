españolIngles={}
inglesEspañol={}

def spen(reps, clave, valor, diccionario):
    c=1
    diccionario.update({clave:valor})
    while True:
        c+=1
        clave = input("Escriba la clave: ")
        valor= input("Escriba un valor: ")
        diccionario.update({clave:valor})
        if c == reps:
            break

    return diccionario

print(spen(int(input("Escriba cuantas veces quiere llenar el diccionario: ")), input("Escriba la clave: "), input("Escriba el valor: "), españolIngles))

def enes(reps, clave, valor, diccionario):
    diccionario.update({clave:valor})

    for h in range(1, reps):
        clave = input("Escriba la clave: ")
        valor= input("Escriba un valor: ")
        diccionario.update({clave:valor})

    return diccionario

print(enes(int(input("Escriba cuantas veces quiere llenar el diccionario: ")), input("Escriba la clave: "), input("Escriba el valor: "), inglesEspañol))

def sepDic(diccionario):
    # t= diccionario.items()
    # return t
    print(f"Tuplas del diccionario {diccionario}")
    for k in diccionario.items():
        t = k
        print(t)
    print()
    return True
sepDic(españolIngles)
sepDic(inglesEspañol)
