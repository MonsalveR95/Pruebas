class Persona:
    def __init__(self, nombre, apellido, cc, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cc = cc
        self.telefono = telefono

    def __str__(self):
     return self.nombre + " " + self.apellido + " " + self.cc
     