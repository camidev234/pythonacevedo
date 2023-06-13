from Cliente import *

class Empresa(Cliente):
    def __init__(self, nombre, id_cliente,numCel):
        Cliente.__init__(self, nombre, id_cliente)
        self.__numCel = numCel

    def getNumCel(self):
        return self.__numCel
    
    def setNumCel(self, num):
        self.__numCel = num
        
    def Aplicardescuentos(self):
        for i in self.productos():
            precio = i.getPrecio()
            descuento = precio * 3.5 / 100
            precio -= descuento
            i.setPrecio(precio)
            
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
        