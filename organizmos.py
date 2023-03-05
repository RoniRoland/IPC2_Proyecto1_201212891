from listaEnlazada import ListaEnlazada


class Organismo:
    def __init__(self, codigo, nombre, color=None):
        self.codigo = codigo
        self.nombre = nombre
        self.color = color

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
