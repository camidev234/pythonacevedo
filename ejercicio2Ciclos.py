#Escriba un programa que solicite un nombre, una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan. Se limitara solo a 3 intentos despues de confirmar 
# la contraseña por primera vez, si se agotan los intentos el programa terminara de lo contrario 
# si las contraseñas coinciden dara un mensaje de bienvenida.

nombre = input("Digite su nombre: ")

contraseña = input("Establezca su contraseña: ")
confContraseña = input("Digite su contraseña: ")
if confContraseña == contraseña:
    print(f"Contraseña correcta bienvenido {nombre}")
intentos = 4

while confContraseña != contraseña:
    intentos -=1
    print(f"La contraseña no coincide solo posee {intentos} intentos")
    confContraseña = input("Digite su contraseña: ")
    if intentos < 1:
        print("Haz agotado todos los intentos")
        break
    if confContraseña == contraseña:
        print(f"Contraseña correcta bienvenido {nombre}")
        break
    
    
    
