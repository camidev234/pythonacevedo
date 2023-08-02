contLines = 0
with open('C:\\repoSena\\pythonacevedo\\archivos\\himno.txt', 'r', encoding='utf-8') as file:
    reader = file.read()
    for char in reader:
        if char == '\n':
            contLines+=1
    contLines+=1
    print(contLines)
with open('C:\\repoSena\\pythonacevedo\\archivos\\himno.txt', 'rt', encoding='utf-8') as stream:
    cont = 1
    row = stream.readline()
    while True:
        print(cont, row)
        row = stream.readline()
        cont += 1
        if cont == contLines+1:
            break


with open('C:\\repoSena\\pythonacevedo\\archivos\\himno.txt', 'rt', encoding='utf-8')as file:
    for row in file.readlines():
        print(row)

 
        