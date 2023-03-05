from nodoRow import NodoRow
from grafica import Graph


class ListaFilas:
    id = 0

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, valor):
        self.id += 1
        actual = valor
        valor_incremento = 1
        if self.size == 0:
            self.primero = actual
            self.ultimo = actual
        else:
            fila_primero = self.primero.getFila()
            nodo_primero = self.primero

            while actual != None

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
