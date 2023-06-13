from producto import *


class Cliente:
    def __init__(self, nombre, idCliente):
        self.__nombre = nombre
        self.__idCliente = idCliente
        self.__productos = []

    def getId(self):
        return self.__idCliente
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre


    def agregarProducto(self, producto):
        self.__productos.append(producto)

    def getProductos(self):
        listaProductos = []
        for h in self.__productos:
            listaProductos+=[h.getNombre()]
            
        return listaProductos
            
    def productos(self):
        return self.__productos

    def componerProducto(self, id, nombre,tipo, precio):
        productoUno = Producto(id, nombre,tipo, precio)
        self.__productos.append(productoUno) 
        
    
