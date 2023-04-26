#se declaran y se asignan las variables
x,y=3,5
cont=1
#Se usa el operador logico not para negar la condicion 
while not(x%y==0 or y%x==0):
    #Si la condicion del while es verdadera se imprime los intentos
    print(f'intento numero {cont}')
    #Se solicitan los datos de entrada
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))
    #Tras cada vuelta el contador de intentos aumenta en uno
    cont+=1

print(f'{x} y {y} son factor')