serie = []
n = int(input("Escriba hasta que numero quiere que vaya la secuencia"))
numUno=0
numDos =1
res=0

for h in range(n):
    res = numUno+numDos
    serie.append(res)
    numUno=numDos
    numDos=res
print(serie)

