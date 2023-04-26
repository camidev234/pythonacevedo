#Se declaran las variables
n=int(input('ingrese numero'))
i=1
#Mientras i sea menor a n
while i<n:
    #Si el modulo de i para 7 es 0 el numero es multiplo de 7
    if i%7==0:
        print(f'{i} es multiplo de 7')
    else:
        print(i)
    #Tras cada vuelta se incrementa la i en uno
    i+=1

    