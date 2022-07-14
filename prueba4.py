#Programacion orientada a objetos, ejemplo

# class Cuadrado:
#     def __init__(self, ancho, alto):
#         self.ancho = ancho
#         self.alto = alto
    
#     def calcularArea(self):
#         area = self.ancho * self.alto
#         return area 


# figura = Cuadrado(10, 10)

# print(figura.ancho)
# print(figura.calcularArea())

from Empleado import Empleado
from Cliente import Cliente

#emp = Empleado("Manuel", "Monsalve", "1015452043", 3178516670, "20000")
#cli = Cliente("Gabriela", "Pedreros", "111010293", 3224547372 ,"vip")





def cargar():
    respuesta = input("Agregar empleado: ")
    nombre = input("Inserte nombre: ")
    apellido = input("Inserte el apellido: ")
    cc = input("Inserte la cc: ")
    telefono = input("Inserte telefono: ")

    if (respuesta == "si"):
        salario = input("Ingrese salario: ")
        emp = Empleado(nombre, apellido, cc, telefono, int(salario))
        personas.append(emp)
    else: 
        categoria = input("Ingrese categoria: ")
        cli = Cliente(nombre, apellido, cc, telefono, categoria)
        personas.append(cli)

personas = []
cargar()
#cargar()
for persona in personas:
    print(persona)

