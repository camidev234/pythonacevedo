import random
cont=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0
sumap=0
sumdes=0

lon = random.randrange(20, 30)

lista = [round(random.random()*5,1)   for i in range(lon)]
print(lista)
for n in range(lon):
    for j in range(n+1, lon):
        if lista[n] > lista[j]:
            aux=lista[n]
            lista[n] = lista[j]
            lista[j] = aux

print(lista)
lista2 = [x for x in lista if x >= 3]
print("lista de buenos", lista2)
lista3= [j for j in lista if j < 3]
print("lista de reprobados", lista3)

for k in range(lon):
    if lista[k] <1:
        cont+=1
        cont-1
    if lista[k] <=2:
        cont2+=1
        cont2-1
    if lista[k]<=3:
        cont3+=1
        cont3-1
    if lista[k] <=4:
        cont4+=1
        cont4-1
    if lista[k]<=5:
        cont5+=1
        cont-1
print(cont, cont2, cont3, cont4, cont5)
listag1=lista[:cont] 
print("grupo de 0 a 1", listag1)
listag2=lista[cont:cont2]      
print("grupo de 1 a 2", listag2)
listag3=lista[cont2:cont3]
print("grupo de 2 a 3",listag3)  
listag4=lista[cont3:cont4]
print("grupo de 3 a 4",listag4)
listag5=lista[cont4:cont5]
print("grupo de 4 a 5",listag5)

for l in lista2:
    sumap+=l
    
for o in lista3:
    sumdes+=o

promAprobados= sumap/len(lista2)
promdesa= sumdes/len(lista3)
print("prmedio de los aprobados", promAprobados)
print("promedio de los desparobados",  promdesa)




#este es todo el mismo ejercicio pero con comprension de listas
    
# sumap=0
# sumdes=0
# listag1=[m for m in lista if m <1]
# print("grupo de 0 a 1", listag1)            
# listag2= [f for f in lista if f >=1 and f <2]
# print("grupo de 1 a 2", listag2)
# listag3= [o for o in lista if o >=2 and o <3]
# print("grupo de 2 a 3",listag3)
# listag4= [p for p in lista if p if p >=3 and p <4]
# print("grupo de 3 a 4",listag4)
# listag5=[a for a in lista if a >=4 and a<=5]
# print("grupo de 4 a 5",listag5)
# for l in lista2:
#     sumap+=l
    
# for o in lista3:
#     sumdes+=o
    
# promAprobados= sumap/len(lista2)
# promdesa= sumdes/len(lista3)
# print("prmedio de los aprobados", promAprobados)
# print("promedio de los desparobados",  promdesa)