class Persona:
    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__curso = []


    def addCursos(self, curso):
        self.__curso += [curso]

    def getCursos(self):
        return self.__curso
                 

    def getDocumento(self):
        return self.__documento
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDocumento(self, documento):
        self.__documento = documento
        
    def getValues(self):
        return f"{self.__nombre}, {self.__documento}"
    
    def buscarCurso(self, curso):
        if curso in self.__curso:
            return f"El curso {curso} esta en la lista."
        else:
            return f"El curso {curso} no esta en la lista de cursos."
        
    def deleteCurso(self, cursoo):
        if cursoo in self.__curso:
            self.__curso.remove(cursoo)
        else:
            return f"El curso {cursoo} no se puede eliminar ya que no esta en la lista."
        
    
    def updateCurso(self, curso, nuevocurso):
        for i in range(len(self.__curso)):
            if self.__curso[i] == curso:
                self.__curso[i] = nuevocurso
    
        

personaUno = Persona("Camilo", 300330)
print(personaUno.getCursos())
personaUno.addCursos("matematicas")
personaUno.addCursos("ingles")
personaUno.addCursos("Geografia")
personaUno.addCursos("español")
personaUno.addCursos("trigonometria")
personaUno.addCursos("fisica")
personaUno.addCursos("Geometria")
print(personaUno.getCursos())
print(personaUno.buscarCurso("Geografia"))
personaUno.deleteCurso("español")
print(personaUno.getCursos())
personaUno.updateCurso("ingles", "sistemas")
print(personaUno.getCursos())
print(personaUno.getValues())





