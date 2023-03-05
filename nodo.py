
class Nodo:
    def __init__(self, valor=None, id=-1):
        self.valor = valor
        self.siguiente = None
        self.anterior = None
        self.id = id

    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getSiguiente(self):
        return self.siguiente

    def setAnterior(self, anterior):
        self.anterior = anterior

    def getAnterior(self):
        return self.anterior
