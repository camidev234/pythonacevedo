#Se declaran y se asignan las variables
num1,num2=100,50
#Se imprime las posibles opciones
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
#Se asigna la varible op como una entrada de tipo entero
op=int(input('que operacion?'))
#Match evaluara las condiciones para la variable op
match op:
    #Se escriben los casos con su respectiva operacion segun el mismo
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)# //  /
    case 5:    
        print(num1%num2)