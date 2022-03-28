from ListaCiudades import *
from ListaRobots import *
from cargarData import *
import easygui

ListadeCiudades = ListaCiudades()
ListadeRobots = ListaRobots()

def menuPrincipal(listadeCiudades,listadeRobots):
    opcion = None
    while(opcion != "4"):
        print("\n███████  MENÚ PRINCIPAL ██████████")
        print("█OPCIONES:                           █")
        print("█1. Cargar Data                      █")
        print("█2. Mision de Rescate                █")
        print("█3. Misión de extracción de Recursos █")
        print("█4. Salir                            █")
        print("█████████████████████████████████████")
        print(" ")
        opcion = str(input("Ingrese una de las opciones: "))
        print(" ")
        if opcion == "1":
               print("Cargando datos...")
               ruta_archivo = easygui.fileopenbox() 
               leerXML(ruta_archivo,listadeCiudades,listadeRobots)
               listadeCiudades.imprimirCiudades()
               listadeRobots.imprimirRobots(True)
        elif opcion == "2":
                print('MISION RESCATE')
        elif opcion == "3":
              print('MISION EXTRACCIÓN')
        elif opcion == "4": 
                print("Saliendo...")
        else:
                print("Ingrese una opción valida! ")
    
    print("HA SALIDO DE LA EJECUCIÓN DEL PROGRAMA CON ÉXITO ")
    

menuPrincipal(ListadeCiudades,ListadeRobots)