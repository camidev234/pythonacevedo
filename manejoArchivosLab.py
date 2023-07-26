from os import strerror

contadorLetras = 0
contadorNumeros = 0
contadorCs = 0

# Inicializa 26 contadores para cada letra latina.
# Nota: hemos usado una comprensión para esto.
"""
la comprension hace uso de un diccionario, usando la funcion chr recibe cada letra del abecedario las cuales
las cuales mediante un for van en un rango de la a la z ordenadamente, es decir, la variable iteradora ch es cada letra del
alfabeto y se inicializa con un valor de 0 por defecto

Hay que tener en cuenta que la variable ch tomara un entero, el cual sera el valor unicode para cada letra

"""
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
"""
re realiza un diccionario mediante compresion en donde se agrega cada elemento i que es la variable
que itera sobre el for, se convierte a string para mas adelante poder hacer uso de la funcion
iddigit()

"""
numbers = {str(i): 0 for i in range(10)}
# se crea un diccionario para los caracteres especiales sin ninguna valor inicial
special = {}
# se ingresa mediante teclado el nombre del archivo
file_name = input("Ingresa el nombre del archivo a analizar: ")
# se inicializa la estructura try-except
try:
    # se realiza la apertura del archivo en modo de lectura
    file = open(file_name, "rt")
    # se hace un bucle for que recorrera el archivo (variable file) linea por linea
    for line in file:
        # se anida un for que para cada linea (variable line) recorrera los caracteres
        for char in line:
            l = char.lower()
            char = l
            # Si el caracter es una letra:
            if char.isalpha():
                """
                Esa letra se convierte a minuscula y en el diccionaro counters para la clave 
                cuyo valor sea igual al caracter que es alfabetico (char), para esa letra se aumenta su
                contador en uno, es decir, su aparicion en el archivo incrementara en uno.
                
                """
                counters[char.lower()] += 1
                # se cuentan las letras en general
                contadorLetras +=1
            # si el caracter es un digito
            if char.isdigit():
                # a esa clave se le amenta su frecuencia en el texto una vez
                numbers[char]+=1
                contadorNumeros+=1
            # si el caracter no esta en como letra o como numero y ademas no es un salto de linea:
            if char not in counters and char not in numbers and char != ' ' and char != '\n':
                # si el caracter no esta como clave en el diccionario special:
                if char not in special:
                    # se agrega al diccionario con un valor inicial de 0
                    special.update({char:0})
                    # se incrementa el contador de caracteres especiales
                    contadorCs+=1
                    # y se incrementa la frecuencia del caracter especial en uno
                    special[char]+=1
                # si el caracter SI esta en el diccionario:
                else:
                    # se aumenta su frecuencia en uno
                    special[char]+=1
                    contadorCs+=1
    # se cierra el archivo
    file.close()
    # Ahora se recorre el diccionario 
    print("LETRAS")
    for char in counters.keys():
        # se asigna a la variable c el valor de cada clave, es decir el valor que tiene char (variable iteradora) 
        c = counters[char]
        # if esa letra tiene un VALOR mayor a 0 osea aparecio al menos una vez:
        if c > 0: 
            # se imprime la clave asociando su valor osea la cantidad de veces que aparecio.
            print(char, '->', c)
    print("NUMEROS")
    for h in numbers.keys():
        n = numbers[h]
        if n > 0:
            print(f"{h} -> {n}")
    print("CARACTERES ESPECIALES")
    for b in special.keys():
        g = special[b]
        if g > 0:
            print(f"{b} -> {g}")
    
    # se imprimen cuantos caracteres de cada tipo hubieron en total.
    print(f"Hubieron {contadorLetras} letras en total en su archivo.")
    print(f"Hubieron {contadorNumeros} numeros en su archivo")
    print(f"Hubieron {contadorCs} caracteres especiales")
# en el bloque except se evalua la excepcion de tipo IOError y se almacena en la variable e
except IOError as e:
    # en caso de que se produzca el error se imprime el mensaje junto con el error 
    # la variable e tiene la expcepcion y con el metodo errno arroja especificamente cual es el numero de error.
    # se usa la funcion str error para describir con exactitud el error.
    print("Se produjo un error de E/S: ", strerror(e.errno))