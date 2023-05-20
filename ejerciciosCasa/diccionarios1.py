dictionary = {
    'perro': 'dog',
    'gato': 'cat',
    'caballo':'horse',
    'Numero Telefono': 3003130618
}

def searchKey(key, diction):
    if key not in diction:
        return f"La clave {key} no existe en el diccionario"
    else:
        s = diction[key]
        t = type(s)
        if t is str:
            t = "Cadena"
        elif t is int:
            t = "Entero"
        else:
            t = "Flotante"
        return f"El valor asociado a {key} es --> {s} y es de tipo {t}"
    
print(searchKey(input("Escriba la clave a buscar: "), dictionary))
