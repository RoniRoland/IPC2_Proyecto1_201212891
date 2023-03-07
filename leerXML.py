import xml.etree.ElementTree as ET
from organizmos import Organismo
from listaEnlazada import ListaEnlazada
from rowsList import ListaFilas
from nodoRow import NodoRow


def Leer_XML(listaOrganismos):
    opc = input("Ingrese nombre del archivo: ")
    tree = ET.parse(opc)
    data = tree.getroot()
    listaOrganismos = ListaEnlazada()
    listFilas = ListaFilas()

    for item in data:
        if (item.tag == "listaOrganismos"):
            for organismo in item.iter("organismo"):
                org = Organismo(organismo.find("codigo").text,
                                organismo.find("nombre").text)
                listaOrganismos.insertar(org)

        elif (item.tag == "ListadoMuestras"):
            for muestra in item.iter("muestra"):
                for listadoceldasvivas in muestra.iter("listadoCeldaVivas"):
                    for celdaviva in listadoceldasvivas.iter("celdaViva"):
                        listFilas.insertar(
                            NodoRow(celdaviva.find("fila").text))
                        print(celdaviva.find("columna").text)

    # listaOrganismos.printNodos()
