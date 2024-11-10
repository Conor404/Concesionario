"""Este es un pequeño borrador de las clases que en teoria estariamos utilizando para este proyecto, la logica del mismo sera trabajada
a partir de aca"""

class Vehiculo:
    #Clase para la creacion de vehiculos (carros o camionetas segun el caso)
    def __init__(self, modelo, año, precio, c_carro, c_camioneta):
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.c_carro = c_carro
        self.c_camioneta = camioneta

class Usuario:
    #Clase para la creacion del usuario como objeto
    def __init__(self, n_usuario, correo, h_compra):
        self.n_usuario = n_usuario
        self.correo = correo
        self.h_compra = h_compra
        
class Repuestos:
    #Clase para la creacion de los repuestos segun su categoria y tipo de vehiculo (sean carros o camionetas)
    def __init__(self, categoria, r_carro, r_camioneta):
        self.categoria = categoria
        self.r_carro = r_carro
        self.r_camioneta = r_camioneta

class Catalogo:
    #Clase para la creacion del catalogo al cual se subiria en teoria el inventario de vehiculos y repuestos disponibles
    def __init__(self, vehiculo, repuestos):
        self.vehiculo = vehiculo
        self.repuestos = repuestos
    
class Costos:
    #Clase para manejar la logica de los costos para crear facturas basicas
    def __init__(self, precio_r, precio_v, mantenimiento):
        self.precio_r = precio_r
        self.precio_v = precio_v
        self.mantenimieno = mantenimiento
        
"""Nuevamente, esto es un pequeño borrador inicial por lo que todo el archivo esta sujeto a constante cambio, conforme trabajemos
el proyecto las cosas iran tomando mas forma. Subire un archivo de texto con el commit de la modificacion de este main para
aclarar el nombre de algunas variables que por los momentos pueden resultar un poco ambiguos"""