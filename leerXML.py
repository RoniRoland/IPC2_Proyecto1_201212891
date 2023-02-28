from xml.dom import minidom


def Leer_XML():
    documento = minidom.parse("Entrada.xml")
    print("============LEYENDO DATOS===========")
    datosMarte = documento.getElementsByTagName("datosMarte")
    for marte in datosMarte:
        listaOrganismos = marte.getElementsByTagName("listaOrganismos")
        for m in listaOrganismos:
            print("--LISTA Organismos!!---")
            organismo = m.getElementsByTagName("organismo")
            for o in organismo:
                codigo = o.getElementsByTagName("codigo")
                nombre = o.getElementsByTagName("nombre")
                c_codigo = int(codigo[0].firstChild.nodeValue)
                n_nombre = str(nombre[0].firstChild.nodeValue)
                print("Codigo: " + str(c_codigo) +
                      "\n" + "Nombre: " + str(n_nombre))
        listadoMuestras = marte.getElementsByTagName("listadoMuestras")
        for m in listadoMuestras:
            print("--Lista muestra Organismos!!---")
            muestra = m.getElementsByTagName("muestra")
            for muestr in muestra:
                print("=======MUESTRAS=======")
                codigo = muestr.getElementsByTagName("codigo")
                descripcion = muestr.getElementsByTagName("descripcion")
                filas = muestr.getElementsByTagName("filas")
                columnas = muestr.getElementsByTagName("columnas")
                print("Codigo: " + str(codigo[0].firstChild.nodeValue) + "\n" + "Descripcion: " + str(descripcion[0].firstChild.nodeValue) +
                      "\n" + "Filas: " + str(filas[0].firstChild.nodeValue) + "\n" + "Columnas: " + str(columnas[0].firstChild.nodeValue))
                listadoCeldasVivas = muestr.getElementsByTagName(
                    "listadoCeldasVivas")
                for lv in listadoCeldasVivas:
                    print("========LISTADO VIVAS=========")
                    celdaViva = lv.getElementsByTagName("celdaViva")
                    for cv in celdaViva:
                        fila = cv.getElementsByTagName("fila")
                        columna = cv.getElementsByTagName("columna")
                        codigoOrganismo = cv.getElementsByTagName(
                            "codigoOrganismo")
                        print("Fila: " + str(fila[0].firstChild.nodeValue) + "\n" + "Columna: " + str(
                            columna[0].firstChild.nodeValue) + "\n" + "Codigo Organismo: " + str(codigoOrganismo[0].firstChild.nodeValue))
