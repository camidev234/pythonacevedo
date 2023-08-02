class Persona:
    def __init__(self, tipoDocumento, codDepartamento, cuartosHogar, perclectura, genero):
        self.__tipoDocumento = tipoDocumento
        self.__codDepartamento = codDepartamento
        self.__cuartosHogar = cuartosHogar
        self.__perclectura = perclectura
        self.__genero = genero


    def getTipoDocumento(self):
        return self.__tipoDocumento
    
    def getCodDepartamento(self):
        return self.__codDepartamento
    
    def getPerclectura(self):
        return self.__perclectura
    
    def getGenero(self):
        return self.__genero
    
    def cuartosHogar(self):
        return self.__cuartosHogar
    
    