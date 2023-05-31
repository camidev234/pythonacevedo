#llenar diccionario
dict1={}

def completeDict(diccionario):
    reps = int(input("Escriba cuantas veces quiere llenar el diccionario: "))
    for h in range(1, reps+1):
        clave = input("Escriba la clave: ")
        valor= input("Escriba un valor: ")
        diccionario.update({clave:valor})

    return diccionario


# separar diccionario en dos tuplas una de claves y otra de valores


def sepDic(diccionario):
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
    tv=()
    for j in valores:
        tv+=(j,)
    
    return tc, tv


def deleteKv(diccionario, claveOvalor):
    del diccionario[claveOvalor]
    return claveOvalor





