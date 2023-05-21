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
    #FORMA 1
    """print()
    print(f"Tuplas del diccionario {diccionario}")
    t= diccionario.items()
    return t"""
    #FORMA 2
    """print(f"Tuplas del diccionario {diccionario}")
    for k in diccionario.items():
        t = k
        print(t)
    print()
    return True"""
    #FORMA 3
    #.
    valores=[]
    claves=[]
    print("---------------------------------------------------------------")
    for h in diccionario:
        claves.append(h)
        c = diccionario[h]
        valores.append(c)
    tc=()
    for h in claves:
        if h in diccionario:
            tc+=(h,)
    print(f"Tupla de claves {tc}")
    tv=()
    for j in valores:
        tv+=(j,)
    print(f"Tupla de valores {tv}")
    
    return True
        
                   
    
sepDic(españolIngles)
sepDic(inglesEspañol)



