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

            while actual != None and nodo_primero.getFila() < actual.getFila():
                nodo_primero = nodo_primero.getFilaSiguiente()

            if nodo_primero == None:
                actual.setFilaAnterior(self.ultimo)
                self.ultimo.setFilaSiguiente(actual)
                self.ultimo - actual
            elif actual.getFila() < fila_primero:
                actual.setFilaSiguiente(self.primero)
                self.primero.setFilaAnterior(actual)
                self.primero = actual
            else:
                if actual.getFila() == nodo_primero.getFila():
                    valor_incremento = 0
                else:
                    actual.setFilaSiguiente(nodo_primero)
                    actual.setFilaAnterior(nodo_primero.getFilaAnterior())
                    nodo_primero.setFilaAnterior(actual)
                    nodo_anterior = actual.getFilaAnterior()
                    nodo_anterior.setFilaSiguiente(actual)

        self.size += valor_incremento

    def addPos(pos_fila):
        pass

    def printNodos(self):
        nodo_primero = self.primero
        while nodo_primero:
            print(str(nodo_primero.fila), str(nodo_primero.fila))
            nodo_primero = nodo_primero.getFilaSiguiente()

    def createGraph(self):
        gr = Graph()
        nodo_ac = self.primero
        while nodo_ac:
            gr.addNodo(nodo_ac, nodo_ac.getSiguiente())
            nodo_ac = nodo_ac.getSiguiente()
        gr.generate()
