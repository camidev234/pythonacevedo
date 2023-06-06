class Empleado:
    contador = 0
    sumaSalarios = 0
    def __init__(self, nombre, salario, cargo):
        self.__nombre = nombre
        self.__salario = salario
        self.__cargo = cargo
        Empleado.contador +=1
        Empleado.sumaSalarios += self.__salario
    
    def getName(self):
        return self.__nombre
    
    def getProfession(self):
        return self.__cargo
    
    def getSalary(self):
        return self.__salario
    
    def setCargo(self, cargo):
        self.__cargo = cargo

    def setSalario(self, salario):
        self.__salario = salario

    def setNombre(self, nombre):
        self.__nombre = nombre


    def calcularHoras(self):
        salarioDia = self.__salario / 30
        salarioHora = salarioDia / 8

        return salarioHora

    def incrementoSalario(self):
        if self.__salario > 1160000:
            ipc = self.__salario * 13.12 / 100
            incremento = self.__salario + ipc
            self.__salario = incremento
            return ipc
        else:
            ipc = self.__salario * 16.12 / 100
            incremento = self.__salario + ipc
            self.__salario = incremento
            return ipc
            

    
    def getSuma(self):
        return Empleado.sumaSalarios
    
    def promedioSalarios(self):
        promSalarios = Empleado.sumaSalarios / Empleado.contador
        return promSalarios
    
    def horasExtras(self, horas):
        if horas > 40:
            return f"No se admiten mas de 2 horas diarias"
        else:
            suma = 4833 * horas
            self.__salario = self.__salario + suma
            return suma


# uno = Empleado("Juan", 1162000, "dd")
# uno.incrementoSalario()
# uno.horasExtras(9)
# print(uno.getSalary())
# dos = Empleado("Juan", 1160000, "dd")
# print(dos.horasExtras(9))
# print(dos.incrementoSalario())
# print(dos.getSalary())
# print(dos.getSuma())
# print(uno.promedioSalarios())

