from leerXML import Leer_XML
from listaEnlazada import ListaEnlazada


def main():
    print("=====================ANALISIS DE MUESTRAS======================")
    print("|--------------------DATOS MARTE-------------------------------|")
    print("1.- Cargar archivo XML")
    print("2.- Analisis de Muestras")
    print("3.- Salir")
    while True:
        try:
            option = int(input("Ingrese una opcion: "))
            if option == 1:
                print('\n============CARGA DE ARCHIVO==============\n')
                Leer_XML()
                print(
                    "\n********************ARCHIVO CARGADO EXITOSAMENTE*****************\n")
                input('\nPresione enter para continuar...')
                main()
                break
            elif option == 2:
                pass
                break
            elif option == 3:
                break
            else:
                print("Opcion incorrecta")
        except ValueError:
            print("Opcion incorrecta")
    exit


main()
