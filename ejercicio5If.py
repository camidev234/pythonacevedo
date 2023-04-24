nombre = input("Escriba su nombre: ")
sexo = input("Escriba su sexo M Para masculino o F para femenino: ")
nombre.lower()
sexo.lower()

if sexo == "f":
    if nombre < 'm':
        print("Grupo A")
elif sexo == "m":
    if nombre > 'b':
        print("Grupo A")
else:
    print("Grupo B")

    
        