from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, cc, telefono, categoria):
        super().__init__(nombre, apellido, cc, telefono)
        self.categoria = categoria