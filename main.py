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
               #listadeCiudades.imprimirCiudades()
               #listadeRobots.imprimirRobots(True)
        elif opcion == "2":
                print('████████████ MISION RESCATE  ████████████')
                hayRobotsDeRescate = listadeRobots.hayRobotsDeRescate()
                if hayRobotsDeRescate:
                        contadorChapinRescue = listadeRobots.contadorRobotsRescate()
                        if contadorChapinRescue == 1:
                                #------------------------------------------#
                                #          SOLO UNA UNIDAD DE RESCATE      #
                                #------------------------------------------#
                                robotDeRescate = listadeRobots.escogerChapinRescueAutomatico()
                                print("Existe sólo un Robot de rescate ")
                                print(f'ChapinRescue: {robotDeRescate.nombre}')
                                print("------------ ESCOJA UN MAPA ------------")
                                listadeCiudades.imprimirCiudades()
                                print(" ")
                                nombreCiudad = input("Ingrese el nombre de una Ciudad -> ")
                                print(" ")
                                ciudadEscogida = listadeCiudades.buscarCiudad(nombreCiudad)
                                if ciudadEscogida:       
                                        print("CIUDAD SELECCIONADA: ")
                                        print(f'█{ciudadEscogida.Ciudad.nombre}')
                                        print(" ")
                                        contadorCiviles = ciudadEscogida.Ciudad.matrizDispersa.contarCiviles()
                                        #print(contadorCiviles)
                                        if contadorCiviles == 0:
                                                print("NO HAY UNIDADES CIVILES NO SE PUEDE REALIZAR LA MISIÓN ")
                                        if contadorCiviles == 1:
                                                print("EXISTE SÓLO UNA UNIDAD CIVIL ")
                                        if contadorCiviles > 1:
                                                print("ESCOJA QUÉ UNIDAD CIVIL DESEA RESCATAR ")
                                else: 
                                        print("NOMBRE DE CIUDAD INGRESADO NO EXISTE! ")
                        else:  
                                #------------------------------------------#
                                #          MÁS DE UNA UNIDAD DE RESCATE    #
                                #------------------------------------------#      
                                print("------------ ESCOJA UN ROBOT ------------")
                                listadeRobots.imprimirRobots() 
                                print(" ")
                                nombreRobot = input("Ingrese el nombre del Robot -> ")
                                robotEscogido = listadeRobots.buscarRobot(nombreRobot,"ChapinRescue") 
                                 
                                if robotEscogido:
                                        print(" ")
                                        print("ROBOT SELECCIONADO: ") 
                                        robotEscogido.Robot.imprimirDatos()
                                        print(" ")
                                        print("------------ ESCOJA UN MAPA ------------")
                                        listadeCiudades.imprimirCiudades()
                                        print(" ")
                                        nombreCiudad = input("Ingrese el nombre de una Ciudad -> ")
                                        print(" ")
                                        ciudadEscogida = listadeCiudades.buscarCiudad(nombreCiudad)
                                        if ciudadEscogida:       
                                                print("CIUDAD SELECCIONADA: ")
                                                print(f'█{ciudadEscogida.Ciudad.nombre}')
                                                print(" ")
                                                contadorCiviles = ciudadEscogida.Ciudad.matrizDispersa.contarCiviles()
                                                #print(contadorCiviles)
                                                if contadorCiviles == 0:
                                                        print("NO HAY UNIDADES CIVILES NO SE PUEDE REALIZAR LA MISIÓN ")
                                                if contadorCiviles == 1:
                                                        print("EXISTE SÓLO UNA UNIDAD CIVIL ")
                                                        
                                                if contadorCiviles > 1:
                                                        print("ESCOJA QUÉ UNIDAD CIVIL DESEA RESCATAR ")
                                        else: 
                                                print("NOMBRE DE CIUDAD INGRESADO NO EXISTE! ")
                                        
                                else:
                                     print(" ")
                                     print("ROBOT INGRESADO NO EXISTE ")
                        
                else:
                        print("No hay robots ChapinRescue")
                        
        elif opcion == "3":
              print('MISION EXTRACCIÓN')
              hayRobotsDeExtraccion = listadeRobots.hayRobotsDeExtraccion()
              if hayRobotsDeExtraccion:
                      
                      print("Escoja un mapa")
              else:
                      print("No hay robots ChapinFighter ")
        elif opcion == "4": 
                print("Saliendo...")
        else:
                print("Ingrese una opción valida! ")
    
    print("HA SALIDO DE LA EJECUCIÓN DEL PROGRAMA CON ÉXITO ")
    

menuPrincipal(ListadeCiudades,ListadeRobots)