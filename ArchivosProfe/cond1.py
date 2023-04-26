#Se definen las variables y se asignan como datos de entrada enteros
x=int(input('ingrese numero'))
y=int(input('ingrese numero'))
z=int(input('ingrese numero'))
#indentación
#Se evaluan las condiciones
if x>y:
    if x>z:
        #Se imprime el resultado en caso de que la condicion sea verdadera
        print(f'el mayor es {x}')
    #Sino imprime el resultado en caso de que x no sea mayor que z
    else:
        print(f'el mayor es {z}')
#En caso de que x no sea mayor que z:
else:
    if y>z:
        #Si y es mayor que z se imprimira:
        print(f'el mayor es {y}')
        #Sino se imprimira: 
    else:
        print(f'el mayor es {z}')