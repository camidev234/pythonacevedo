class Empleado:
    def __init__(self, nombre, salario, cargo):
          self.__nombre = nombre
          self.__salario = salario
          self.__cargo = cargo

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
        else:
            ipc = self.__salario * 16.12 / 100
            incremento = self.__salario + ipc

        return incremento


empleado = Empleado("Juan", 1200000,"ñero")
print(empleado.incrementoSalario())