with open('C:\\repoSena\\pythonacevedo\\archivos\\himno.txt', 'rt', encoding='utf-8') as file:
    l = []
    contChar = 0
    for line in file:
        for char in line:
            if char != ' ' and char != '\n':
                contChar+=1
            else:
                continue
        l.append(contChar)
        contChar = 0 
print(l)
with open('archivos/resultado.txt', 'a', encoding='utf-8') as stream:
#with open('C:\\repoSena\\pythonacevedo\\archivos\\resultadoHimno.txt', 'w', encoding='utf-8') as stream:
    cont=0
    for i in l:
        cont+=1
        cadena = f"En el verso {cont} hubo {i} caracteres \n"
        stream.write(str(cadena))
