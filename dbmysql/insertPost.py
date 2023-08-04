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

# insertarPersona()


def verDatos():
    id = int(input("Digite el id del cual desea ver la informacion: "))
    consulta = "SELECT * FROM persona WHERE id_persona = %s"
    valor = (id, )
    cursor.execute(consulta, valor)
    print("Consulta realizada con exito")
    for dato in cursor:
        print(f"el id es {dato[0]}, el nombre es {dato[1]},el email es {dato[2]}, el numero telefonico es {dato[3]}, el numero de celular es {dato[4]}")


verDatos()

