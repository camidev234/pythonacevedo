#[], {}, (), {()}
x=100 #se define la variable x
print(type(x)) #se imprime el tipo de dato usando la funcion type
x='Soacha' #se redefine x como una cadena
print(type(x)) 
lista=['python',100,[1,2,3,[]],'a'] #se crea una lista
print(type(lista))
print(len(lista)) #se  imprime la longitud de la lista
print(lista[0]) #se imprime la posicion [x] de la lista
print(lista[1]) #""
print(lista[3]) #""
print(lista[-4]) #""

del lista[-2] #se elimina el penultimo elemento de la lista
print(lista) #se imprime la lista

"""
cuenta1=cuenta()
cuenta2=cuenta()
cuenta3=cuenta()
cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""