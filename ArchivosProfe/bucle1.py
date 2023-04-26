#Se definnen las variables
i=1
sum=0
#Bucle (Mientras que i sea menor o igual que 5)
while i<=5:
    #Se imprime el numero (i)
    print(i)
    #Se reasigna la variable sum para que sirva como acumulador entre cada vuelta
    sum=sum+i
    #La variable i en cada vuelta va a valer 1 mas que en la anterior
    i+=1 #i=i+1 
    #Se imprime el resultado de la variable acumuladora
print(f'la suma es ={sum}')