# 
from os import strerror
listaArchivos = []
archivo = ""
try:
    while True:
        print("""
        1. Crear archivo
        2. Insertar informacion
        3. Ver caracteres del archivo
        """)
        o = int(input("Que opcion desea relaizar: "))
        match o:
            case 1:
                nombreArchivo = input("Escriba el nombre del archivo: ")
                archivo = nombreArchivo
                def crearArchivo(filename):
                    if filename not in listaArchivos:
                        listaArchivos.append(filename)
                        stream = open(filename, 'wt')
                        with open(filename, 'rt')as stream:
                            lineas = []
                            l = stream.readlines()
                            for i in l:
                                lineas.append(i)
                            print("Su archivo tiene:", len(l), "lineas")
                    else:
                        with open(filename, 'rt') as file:
                            lineas = []
                            l = file.readlines()
                            for i in l:
                                lineas.append(i)
                            print("Su archivo tiene:", len(l), "lineas")
                    
                    

                    return archivo
                crearArchivo(nombreArchivo)
            case 2:
                if len(listaArchivos) == 0:
                    print("No hay archivos creados.")
                else:
                    def insertarContenido(archivo):
                        nombre = input("Escriba su nombre: \n")
                        documento = input("Digite su numero de documento: \n")
                        residencia = input("Escriba su residencia: ")

                        with open(archivo, 'a') as file:

                            cadena = nombre + "\n" + documento + "\n" + residencia + "\n"
                            file.write(cadena)
                            file.close()

                            print("Contenido insertado con exito.")
                        
                    insertarContenido(archivo)

            case 3:
                if len(listaArchivos) == 0:
                    print("No hay archivos creados.")
                else:
                    contChar = 0
                    with open(archivo, 'r')as file:
                        for char in file.read():
                            if char == "\n":
                                continue
                            else:
                                contChar +=1

                        print(f"Su archivo tiene {contChar} caracteres")
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))