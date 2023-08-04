# aplicacion personas
"""
Se analizaran los datos con las siguientes operaciones:

1.Moda de tipos de documento (mayor o menor de edad)
2.Desviacion estandar de puntaje Global
3.Moda de mujeres o hombres que presentaron la prueba
4.Promedio de habitaciones por persona
5.Moda de ubicaciones por departamento

"""
import math
import csv
from Persona import *
personas = []

with open('archivos/saber_11__2019-2.csv', 'rt', newline='', encoding='utf-8') as fileCsv:
    countObjects = 0
    csvReader = csv.reader(fileCsv)
    for row in csvReader:
        countObjects+=1
        # print(f"tipo{row[0]}, cod{row[11]}, cuartos{row[16]}, puntGLB{row[-7]}, genero{row[2]}")
        newPerson = Persona(row[0], row[11], row[16], row[-7], row[2])
        personas.append(newPerson)
    print(f"Ejecucion finalizada con exito se crearon: {countObjects} objetos")
        
def modaTiposDocumento():
    #Se establecen los tipos de documentos siendo TI:1, CC:2, CE:3, PEP:4, NES:5, PE:6, CR:7
    listaDocumentos = []
    tiposDocumento = {
        'ti': 1,
        'cc': 2,
        'ce': 3,
        'pep': 4,
        'nes': 5,
        'pe': 6,
        'cr': 7
    }
    masRepetido = 0
    moda = ""
    countVeces = 0
    tipoPersona = ""
    for persona in personas:
        if persona.getTipoDocumento() == 'ESTU_TIPODOCUMENTO':
            continue
        elif persona.getTipoDocumento() == 'TI':
            listaDocumentos.append(1)
        elif persona.getTipoDocumento() == 'CC':
            listaDocumentos.append(2)
        elif persona.getTipoDocumento() == 'CE':
            listaDocumentos.append(3)
        elif persona.getTipoDocumento() == 'PEP':
            listaDocumentos.append(4)
        elif persona.getTipoDocumento() == 'NES':
            listaDocumentos.append(5)   
        elif persona.getTipoDocumento() == 'PE':
            listaDocumentos.append(6)
        else:
            listaDocumentos.append(persona.getTipoDocumento())
        
    for i in listaDocumentos:
        for h in listaDocumentos:
            if i == h:
                countVeces+=1
            if countVeces > masRepetido:
                masRepetido = countVeces
                moda = h
        countVeces = 0
        
    for value in tiposDocumento.keys():
        if tiposDocumento[value] == moda:
            moda = value
    
    if moda =='ti':
        tipoPersona = "Menores de edad"
    else:
        tipoPersona = "Mayores de edad"
        
    return f"El tipo de documento que mas veces se repitio es {moda}, Por ende hay mas {tipoPersona}"
            
resultadoUno = modaTiposDocumento()
            
def modaGen():
    generos = []
    for persona in personas:
        generos.append(persona.getGenero())
        
    ch = 0
    cm = 0
    
    for persona in generos:
        if persona == 'M':
            ch+=1
        else:
            cm+=1
            
    if cm > ch:
        return f"En los primeros 100 registros presentaron la prueba mas mujeres con un total de: {cm}"
    else:
        return f"En los primeros 100 registros presentaron la prueba mas hombres con un total de: {ch}"

resultadoDos = modaGen()

def modaUbicacionDept():
    with open('archivos\\departamentos.csv', 'rt', newline='', encoding='utf-8') as deptos:
        departamentos = {}
        read = csv.reader(deptos)
        for row in read:
            departamentos.update({row[0]:row[1]})
    
    codigos = []
    masRepeticiones = 0
    moda = ""
    count = 0
    for persona in personas:
        count+=1
        if count == 1:
            continue
            # c = int(persona.getCodDepartamento())
        else:
            c = int(persona.getCodDepartamento())
            codigos.append(c)
    
    count = 0
    
    for cod in codigos:
        for n in codigos:
            if cod == n:
                count+=1
            if count > masRepeticiones:
                masRepeticiones = count
                moda = cod
        count = 0       
    
    connv = str(moda)
    moda = connv

    for departamento in departamentos.keys():
        if departamentos[departamento] == moda:
            moda = departamento
            
    return f"El departamento con mas estudiantes que presentaron la prueba fue: {moda}"
    
    
resultadoTres = modaUbicacionDept()

def promCuartos():
    prom = 0
    sumatoria = 0
    promedio = 0
    cuartosList = []
    cuartosListDos = []
    cuartosDict = {
        'uno':1,
        'dos':2,
        'tres':3,
        'cuatro':4,
        'cinco':5
    }
    
    for persona in personas: 
        cuartosList.append(persona.cuartosHogar().lower())
        
    for i in cuartosList:
        for key in cuartosDict.keys():
            if i == key:
                cuartosListDos.append(cuartosDict[key])
    
    for cuarto in cuartosListDos:
        sumatoria+=cuarto
        
    promedio = sumatoria / len(cuartosListDos)
    prom = round(promedio)
    
    return f"El promedio de habitaciones por familia de un estudiante es de: {prom}"
    
resultadoCuatro = promCuartos()

def desviacionEstandar():
    puntajes = []
    sumaCuadrados = 0
    sumatoria = 0
    cont = 0
    for persona in personas:
        cont+=1
        if cont == 1:
            continue
        else:
            puntaje = int(persona.getPuntaje())
            puntajes.append(puntaje)
    
    cont = 0
    for p in puntajes:
        cont +=1
        sumatoria+=p
    
    prom = sumatoria//cont
    
    for j in puntajes:
        resta = j - (sumatoria/cont)
        cuadrado = resta **2
        sumaCuadrados+=cuadrado
        division = sumaCuadrados // cont
        raiz = math.sqrt(division)
    
    print(f"El promedio en puntaje global en los primeros 100 registros es de: {prom}")
    
    return f"La desviacion estandar es: {raiz}"
    
resultadoCinco = desviacionEstandar()

#Agregando resultados a un archivo externo

with open('archivos\\resultadosAnalisisIcfes.txt', 'a+', encoding='utf-8') as resultado:
    resultado.write(f"------------------------------------" + '\n')
    resultado.write(resultadoUno + '\n')
    resultado.write(resultadoDos + '\n')
    resultado.write(resultadoTres + '\n')
    resultado.write(resultadoCuatro + '\n')
    resultado.write(resultadoCinco + '\n')
    resultado.write(f"------------------------------------" + '\n')