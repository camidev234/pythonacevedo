#ejercicio 3, serie de fibonnacci

def serie(tamaño):
    listado=[]
    num1=0
    num2=1
    resultado=0
    for i in range(tamaño):
        resultado=num1+num2
        listado.append(resultado)
        num1=num2
        num2=resultado
    return listado
    
print(serie(int(input("Escriba hasta que numero quiere la serie: "))))
    
    