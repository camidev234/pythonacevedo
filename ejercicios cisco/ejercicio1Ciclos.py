#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí, 
#adicional que muestre en que iteración esta.#

pregunta = input("Desea continuar con el programa")
vuelta = 0

while pregunta == "si" or pregunta == "SI":
    pregunta = input("Desea continuar con el programa")
    vuelta +=1
    
print("El ciclo se ha ejecutado", vuelta, "Veces")