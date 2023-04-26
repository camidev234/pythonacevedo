# num=1
# print(type(num))
# num="sena"
# print(type(num))
#Se definen las variables
num=1
cont=0
sum=0
menor=1000000
mayor=0
#Mientras que numero sea distinto a 0
while num!=0:
    #Solicita el numero
    num=int(input('ingrese numero'))
    #El contador aumentara en uno con cada vuelta
    cont=cont+1
    #Tras cada vuelta los numeros se van a sumar
    sum=sum+num
    if num>mayor:
        #Se asigna al numero como el numero mayor
        mayor=num
    if num<menor and num!=0:
        menor=num

#Se imprime la contidad de numeros ingresados
print(f'fueron ingresados {cont-1} numeros')
#Se imprime la suma de los numeros
print(f'La suma es {sum}')
#El promedio de los numeros
print(f'El promedio es {sum/(cont-1)}')
#Numero mayor y numero menor
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')