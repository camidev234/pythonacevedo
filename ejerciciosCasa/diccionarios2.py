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
    return True

def enes(reps, clave, valor, diccionario):
    diccionario.update({clave:valor})

    for h in range(1, reps):
        clave = input("Escriba la clave: ")
        valor= input("Escriba un valor: ")
        diccionario.update({clave:valor})
        
    return True

def impresionDict(diccionario):
    print()
    print("Diccionario:")
    for k in diccionario:
        claves = diccionario[k]
        print(f"{k} --> {claves}") 

print("Escoga cual de los dos diccionarios desea llenar: ")
print("1. Español a ingles")
print("2. Ingles a español")

pregunta= int(input("Escriba la opcion que desea (solo numeros): "))

match pregunta:
    #Se escriben los casos con su respectiva operacion segun el mismo
    case 1:
        print("Escriba la palabra en español, y el significado en ingles")
        spen(int(input("Escriba cuantas veces quiere llenar el diccionario: ")), input("Escriba la clave: "), input("Escriba el valor: "), españolIngles)
        impresionDict(españolIngles)
    case 2:
        print("Escriba la palabra en ingles, y el significado en español")
        enes(int(input("Escriba cuantas veces quiere llenar el diccionario: ")), input("Escriba la clave: "), input("Escriba el valor: "), inglesEspañol)
        impresionDict(inglesEspañol)