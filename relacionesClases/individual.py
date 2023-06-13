from Cliente import *
from producto import *


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
        
     # metodo para aplicar descuentos a todos los productos   
    def Aplicardescuentos(self):
        for i in self.productos():
            precio = i.getPrecio()
            descuento = precio * 2.0 / 100
            precio -= descuento
            i.setPrecio(precio)
    """        
    # metodo para aplicar descuentos Uno por Uno (solo para agregacion)
    
    def AplicarDescuento(self, producto):
        precio = producto.getPrecio()
        descuento = precio * 2.0 / 100
        precio -= descuento
        producto.setPrecio(precio)"""
        
        
    def descuentoCompuesto(self):
        for k in self.productos():
            precio = k.getPrecio()
            descuento = precio * 2.0 / 100
            precio -= descuento
            k.setPrecio(precio)
            
        for i in self.productos():
            p = i.getPrecio() 
            print(f"Precio de {i}: {p}")
            
        return True
    
        