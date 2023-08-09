from bdproy import *

def insertarPersona():
    nombre=input("Escriba su nombre: ")
    email=input("Escriba su email: ")
    telefono=input("Escriba su telefono: ")
    celular=input("Escriba su celular: ")
    consulta="insert into persona (nombre,email,telefono,celular)values(%s, %s, %s, %s)"
    values=(nombre,email,telefono,celular) 
    cursor.execute(consulta,values)
    db.commit()
    print("se ejecuto con exito")

while True:
    p = input("Desea agregar otro registro y/n: ")
    if p == "y" or p == "Y":
        insertarPersona()
    else:
        break

def verDatos():
    id = int(input("Digite el id del cual desea ver la informacion: "))
    consulta = "SELECT * FROM persona WHERE id_persona = %s"
    valor = (id, )
    cursor.execute(consulta, valor)
    print("Consulta realizada con exito")
    for dato in cursor:
        print(f"el id es: {dato[0]} \nel nombre es: {dato[1]} \nel email es: {dato[2]} \nel numero telefonico es: {dato[3]} \nel numero de celular es: {dato[4]}")

while True:
    p = input("Desea ver la informacion de algun registro y/n: ")
    if p == "y" or p == "Y":
        verDatos()
    else:
        break

def actualizarDatos():
    
    persona = int(input("Escriba el id del usuario al cual quiere actualizarle datos: "))
    
    print("1.Dato individual.")
    print("2.Registro completo.")
    
    o = input("Escoja de que manera desea actualizar datos: ")
    
    if o == "1":
        cont = 0
        cursor.execute("describe Persona")
        camposDict = {}
        for columna in cursor:
            cont+=1
            if cont == 1:
                continue
            else:
                camposDict.update({columna[0]: cont-1})
                print(f"{cont-1}. {columna[0]}")
                    
        campo = int(input("Escriba el numero de campo que desea actualizar: "))
        print(camposDict)
        for column in camposDict.keys():
            if campo == camposDict[column]:
                campoUso = column
                    
        nuevoValor = input(f"Escriba el nuevo {campoUso} de la persona: ")
            
        if campoUso == 'nombre':
            consulta = "UPDATE persona SET nombre=%s WHERE id_persona=%s"
            valores =(nuevoValor, persona)
            cursor.execute(consulta, valores)
            db.commit()
            print("Datos actualizados con exito.")
        elif campoUso == 'email':
            consulta = "UPDATE Persona SET email=%s WHERE id_persona=%s"
            valores =(nuevoValor, persona)
            cursor.execute(consulta, valores)
            db.commit()
            print("Datos actualizados con exito.")
        elif campoUso == 'telefono':
            consulta = "UPDATE Persona SET telefono=%s WHERE id_persona=%s"
            valores =(nuevoValor, persona)
            cursor.execute(consulta, valores)
            db.commit()
            print("Datos actualizados con exito.")
        else:
            consulta = "UPDATE Persona SET celular=%s WHERE id_persona=%s"
            valores =(nuevoValor, persona)
            cursor.execute(consulta, valores)
            db.commit()
            print("Datos actualizados con exito.")
    else:
        nombre = input("Escriba el nuevo nombre de la persona: ")
        email = input("Escriba el nuevo email: ")
        tel = input("Escriba el nuevo telefono: ")
        celular = input("Digite el nuevo numero de celular: ")
            
        query = "UPDATE Persona SET nombre=%s, email=%s, telefono=%s, celular=%s WHERE id_persona=%s"
        vals =(nombre, email, tel, celular, persona)
        cursor.execute(query, vals)
        db.commit()
        print("Datos actualizados con exito.")
while True:
    p = input("Desea actualizar datos: y/n: ")
    if p == "y" or p =="Y":
        actualizarDatos()
    else:
        break

def borrarDatos():
    id = int(input("Digite el id de la persona que desea eliminar de la BD: "))
    consulta = "DELETE FROM persona WHERE id_persona = %s"
    vls = (id,)
    cursor.execute(consulta, vls)
    db.commit()
    print(cursor)
    print("Eliminado con exito.")
                
while True:
    p = input("Desea borrar datos: y/n: ")
    if p == "y" or p =="Y":
        borrarDatos()
    else:
        break
