class Nodo:
    # Constructor para crear un nuevo nodo
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

# Obtener datos del nodo
    def get_datos(self):
        return self.datos

# establecer los datos al nodo
    def set_datos(self, valores):
        self.datos = valores

# Obtener siguiente nodo
    def get_siguiente(self):
        return self.siguiente

# Establecer siguiente nodo
    def set_siguiente(self, valores):
        self.siguiente = valores
