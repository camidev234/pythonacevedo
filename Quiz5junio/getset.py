class Persona:
    listaCursos = []
    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__curso = []


    def addCursos(self, curso):
        self.__curso += [curso]

        for i in self.__curso:
            if i not in Persona.listaCursos:
                Persona.listaCursos.append(i)

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
        if curso in self.__curso:
            for i in range(len(self.__curso)):
                if self.__curso[i] == curso:
                    self.__curso[i] = nuevocurso
        else:
            print( f"El curso {curso} no esa en la lista.")
    """
    Aca esta un metodo propio para agregar los elementos la variablede clase.


    def cursoClse(self):
        for i in self.__curso:
            if i not in Persona.listaCursos:
                Persona.listaCursos.append(i)
    """
prueba1 = Persona("Daniel", 24872357)
prueba1.addCursos("Python")
prueba1.addCursos("Java")
prueba1.addCursos("C++")
prueba2 = Persona("Jhan",  8429749)
prueba2.addCursos("Scala")
prueba2.addCursos("Java")
prueba2.addCursos("Python")
prueba1.addCursos("ensamblador")
prueba1.addCursos("C#")
prueba1.addCursos("C++")  
prueba3 = Persona("Camilo", 728264)
prueba2.addCursos("JavaScript")
prueba2.addCursos("NodeJs")
prueba2.addCursos("ExpressJs")
prueba4 = Persona("Pepito", 278474)
prueba2.addCursos("Scala")
prueba2.addCursos("Java")
prueba2.addCursos("Python")
prueba1.addCursos("ensamblador")
prueba1.addCursos("Ruby On Rails")
print(Persona.listaCursos)



# personaUno = Persona("Camilo", 300330)
# print(personaUno.getCursos())
# personaUno.addCursos("matematicas")
# personaUno.addCursos("ingles")
# personaUno.addCursos("Geografia")
# personaUno.addCursos("español")
# personaUno.addCursos("trigonometria")
# personaUno.addCursos("fisica")
# personaUno.addCursos("Geometria")
# personaUno.addCursos("scala")
# print(personaUno.getCursos())
# print(personaUno.buscarCurso("Geografia"))
# personaUno.deleteCurso("español")
# print(personaUno.buscarCurso("español"))
# print(personaUno.getCursos())
# personaUno.updateCurso("ingles", "sistemas")
# personaUno.updateCurso("sistemas", "etica")
# personaUno.updateCurso("sistemas", "ingles")
# print(personaUno.getCursos())
# print(personaUno.getValues())
# personaUno.addCursos("Python")
# print(personaUno.getCursos())
# perDos = Persona("Daniel", 2932974)
# perDos.addCursos("matematicas")
# perDos.addCursos("ingles")
# perDos.addCursos("Geografia")
# perDos.addCursos("español")
# perDos.addCursos("trigonometria")
# perDos.addCursos("fisica")
# perDos.addCursos("Geometria")
# perDos.addCursos("C++")
# perDos.addCursos("scala")
# print(perDos.getCursos())
# print(f" lista persona 2 {Persona.listaCursos}")










