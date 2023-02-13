from nodo import Nodo


class ListaSimple:

    def __init__(self):
        self.inicio = None

    def imprimirLista(self):
        temp = self.inicio
        while (temp):
            print(temp.datos)
            temp = temp.siguiente

    def agregarInicio(self, new_datos):
        new_Nodo = Nodo(new_datos)
        new_Nodo.siguiente = self.inicio
        self.inicio = new_Nodo

    def insertarDespues(self, nodoAnterior, new_datos):
        if nodoAnterior is None:
            print("El nodo anterior debe existir")
            return
        new_Nodo = Nodo(new_datos)
        new_Nodo.siguiente = nodoAnterior.siguiente
        nodoAnterior.siguiente = new_Nodo

    def agregar(self, new_datos):
        new_Nodo = Nodo(new_datos)
        if self.inicio is None:
            self.inicio = new_Nodo
            return

        ultimo = self.inicio
        while (ultimo.siguiente):
            ultimo = ultimo.siguiente
        ultimo.siguiente = new_Nodo

    def eliminarNodo(self, llave):
        temp = self.inicio
        if (temp is not None):
            if (temp.data == llave):
                self.inicio = temp.siguiente
                temp = None
                return

        while (temp is not None):
            if temp.data == llave:
                break
            anterior = temp
            temp = temp.siguiente

        if (temp == None):
            return

        anterior.siguiente = temp.siguiente
        temp = None
