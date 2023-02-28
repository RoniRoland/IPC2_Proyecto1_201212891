from listaEnlazada import ListaEnlazada


class Organismo:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre


class CeldaViva:
    def __init__(self, fila, columna, codigo_organismo):
        self.fila = fila
        self.columna = columna
        self.codigo_organismo = codigo_organismo


class Muestra:
    def __init__(self, codigo, descripcion, filas, columnas):
        self.codigo = codigo
        self.descripcion = descripcion
        self.filas = filas
        self.columnas = columnas

    def agregar_celda_viva(self, fila, columna, organismo):
        self.celdas_vivas.append((fila, columna, organismo))

    def mostrar_celdas_vivas(self):
        for fila, columna, organismo in self.celdas_vivas:
            print(
                f"Celda viva en fila {fila}, columna {columna} con organismo {organismo.nombre} (código {organismo.codigo})")


class DatosMarte:
    def __init__(self):
        self.lista_organismos = ListaEnlazada()
        self.listado_muestras = ListaEnlazada()

    def agregar_organismo(self, organismo):
        self.lista_organismos.agregar(organismo)

    def agregar_muestra(self, muestra):
        self.listado_muestras.agregar(muestra)

    def buscar_organismo_por_codigo(self, codigo_organismo):
        nodo_actual = self.lista_organismos.cabeza
        while nodo_actual != None:
            if nodo_actual.dato.codigo == codigo_organismo:
                return nodo_actual.dato.nombre
            nodo_actual = nodo_actual.siguiente
        return None
