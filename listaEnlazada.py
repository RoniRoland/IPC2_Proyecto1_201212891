from nodo import Nodo
from grafica import Graph


class ListaEnlazada:
    id = 0

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, valor):
        self.id += 1
        actual = Nodo(valor, self.id)
        if self.size == 0:
            self.primero = actual
            self.ultimo = actual
        else:
            actual.setAnterior(self.ultimo)
            self.ultimo.setSiguiente(actual)
            self.ultimo = actual
        self.size += 1

    def addPos(pos_fila):
        pass

    def printNodos(self):
        nodo_ac = self.primero
        while nodo_ac:
            print(nodo_ac.getValor().getNombre())
            nodo_ac = nodo_ac.getSiguiente()

    def createGraph(self):
        gr = Graph()
        nodo_ac = self.primero
        while nodo_ac:
            gr.addNodo(nodo_ac, nodo_ac.getSiguiente())
            nodo_ac = nodo_ac.getSiguiente()
        gr.generate()
