from nodo import Nodo


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza == None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, dato):
        nodo_actual = self.cabeza
        nodo_anterior = None
        while nodo_actual != None:
            if nodo_actual.dato == dato:
                if nodo_anterior == None:
                    self.cabeza = nodo_actual.siguiente
                else:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                return True
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        return False

    def buscar_elemento(self, dato):
        nodo_actual = self.cabeza
        while nodo_actual != None:
            if nodo_actual.dato == dato:
                return nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
