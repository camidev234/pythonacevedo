#tabla de multiplicar

pregunta = int(input("Escriba la tabla que desea conocer"))
preguntaDos = int(input("Escriba hasta que numero desea conocer la tabla"))  

for i in range(1, preguntaDos + 1):
    resultado = pregunta * i
    print(f"{pregunta} x {i} = {resultado}")   