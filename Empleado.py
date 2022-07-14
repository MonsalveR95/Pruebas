from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellido, cc, telefono, salario):
        super().__init__(nombre, apellido, cc, telefono)
        self.salario = salario
