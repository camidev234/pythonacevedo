num=1
cont=0
sum=0
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1
    sum+=num
print(f'fueron ingresados {cont-1} numeros')
print(f"la suma de los numeros es: {sum}")
print(f"El promedio es {sum/(cont-1)}")

      
