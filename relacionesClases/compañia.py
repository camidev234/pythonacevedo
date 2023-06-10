from Cliente import *

class Empresa(Cliente):
    def __init__(self, nombre, id_cliente,numCel):
        Cliente.__init__(self, nombre, id_cliente)
        self.__numCel = numCel

    def getNumCel(self):
        return self.__numCel
    
    def setNumCel(self, num):
        self.__numCel = num