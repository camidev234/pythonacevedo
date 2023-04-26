#ciclo for
#Ciclo for puede recibir 3 argumentos (el primero es el valor inicial el segundo el final menos uno y el 3 el incremento)
#Cuando es solo un argumento es el valor final
for i in range(11):
    #Si el modulo de i en 3 es 0 por lo tanto sera multiplo del 3
    if i%3==0:
        print(f'{i} es multiplo de 3')
    else:
        print(i)

for j in range(1,11):
    #SE IMPRIME LA J HASTA EL 10 EMPEZANDO DESDE 1
    print(j)

for k in range(0,11,2):
    #se imprime la k empezando desde 0 hasta 10 de dos en dos
    print(k)

for i in range(20,0,-2):
    #Se imprime i desde 20 hasta 0 en decremento de uno en uno
    print(i)