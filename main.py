"""Este es un pequeño borrador de las clases que en teoria estariamos utilizando para este proyecto, la logica del mismo sera trabajada
a partir de aca"""

class Vehiculo:
    #Clase para la creacion de vehiculos (carros o camionetas segun el caso)
    def __init__(self, modelo, año, precio, c_carro, c_camioneta):
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.c_carro = c_carro
        self.c_camioneta = c_camioneta

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
    def __init__(self, carros, camionetas, repuestos, costos):
        self.carros = carros
        self.camionetas = camionetas
        self.repuestos = repuestos
        self.costos = costos
        self.disponibilidad = True
    
    def compra(self):
        self.disponibilidad = False 
    def revisar(self):
        if self.disponibilidad == True:
            print("El vehiculo se encuentra disponible")
        else:
            self.disponibilidad == False
            print("El vehiculo no se encuentra disponible")
    

class Costos:
    #Clase para manejar la logica de los costos para crear facturas basicas
    def __init__(self, precio_r, precio_v, mantenimiento):
        self.precio_r = precio_r
        self.precio_v = precio_v
        self.mantenimieno = mantenimiento

carro1 = "Modelo: Toyota 2023\nPrecio: 15.000$\nTipo de Vehiculo: Carro Familiar"
carro2 = "Modelo: Pene 2020\nPrecio: 13.000$\nTipo de Vehiculo: Carro deportivo"
carro3 = "Modelo: Culo 2019\nPrecio: 8.000$\nTipo de Vehiculo: Carro todo terreno"
camioneta1 = "Modelo: Toyobobo\nPrecio: 123.390$\nTipo de Vehiculo: Carro tipo farandula"
camioneta2 = "Modelo: Yamato\nPrecio: 12B$\nTipo de Vehiculo: Vehiculo naval Blindado"
camioneta3 = "Modelo: Panzer 4FJ\nPrecio: 210.000$\nTipo de Vehiculo: Tanque mediano"


print("-"*50)
print(f"Ingrese un numero relacionado a las acciones")
print("1)Catalogo")
print("-"*50)
pregunta = str(input())
print("-"*50)
match pregunta:
    case "1":
        print(f"Cual de los tipos de vehiculos desea averiguar?")
        print("1) Carros")
        print("2) Camionetas")
        catalogo1 = str(input())
        match catalogo1:
            case "1":
                print("Cual de las categorias de carros disponibles desea averiguar?: ")
                print(f"1) Toyota 2019")
                print(f"2) Pene 2020")
                print(f"3) Culo 2019")
                carros = str(input())
                match carros:
                    case "1":
                        print(carro1)
                    case "2":
                        print(carro2)
                    case "3":
                        print(carro3)
                    case _:
                        print("Por favor, escoja una opcion valida")

            case "2":
                print("Cual de las camionetas disponibles desea averiguar?: ")
                print(f"1) Toyobobo")
                print(f"2) Yamato")
                print(f"3) Panzer 4FJ")
                camionetas = str(input())
                match camionetas:
                    case "1":
                        print(f"{camioneta1}")
                    case "2":
                        print(f"{camioneta2}")
                    case "3":
                        print(f"{camioneta3}")
                    case _:
                        print("Por favor, escoja una opcion valida")
    case _:
        print("Seleccione una opcion valida")