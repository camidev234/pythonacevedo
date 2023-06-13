from individual import *
from compañia import *
from producto import *


# Usando AGregacion
clienteUno = Individual("Camilo", 1013108226, "Acevedo", "camilo222andresace@gmail.com", 3003130618)
print(clienteUno.getId())
prodUno = Producto(4728, "Samsung Galaxy A10s", "Movil", 700.000)
prodDos = Producto(243, "Iphone 14", "Movil", 5000000)
clienteUno.agregarProducto(prodUno)
clienteUno.agregarProducto(prodDos)
print(clienteUno.getProductos())
clienteUno.Aplicardescuentos()
print(prodUno.getPrecio())
print(prodDos.getPrecio())


# Con cliente tipo empresa

empresaUno = Empresa("Coca Cola", 42478, 294924)
p1 = Producto(284928, "Camion", "Automovil", 1160000)
p2 = Producto(25777, "Receta Secreta", "Receta", 38493849)
empresaUno.agregarProducto(p1)
empresaUno.agregarProducto(p2)
empresaUno.Aplicardescuentos()
print(p2.getPrecio())



#Usando Composicion

user = Individual("Andres", 101310, "Beltran", "andres@gmail.com", 3003130618)
user.componerProducto(2743, "Portatil Lenovo", "Portatil", 2450000)
user.descuentoCompuesto()





