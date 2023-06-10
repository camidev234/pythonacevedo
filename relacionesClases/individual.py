from Cliente import *

class Individual(Cliente):
    def __init__(self, nombre, id_cliente, apellido, email, numeroCel):
        Cliente.__init__(self, nombre, id_cliente)
        self.__apellido  = apellido
        self.__email = email
        self.__numCel = numeroCel

    def getApellido(self):
        return self.__apellido
    
    def getEmail(self):
        return self.__email
    
    def getnumCel(self):
        return self.__numCel
    
    def setApellido(self, apellido):
        self.__apellido = apellido

    def setEmail(self, email):
        self.__email = email

    def setnumCel(self, numCel):
        self.__numCel = numCel