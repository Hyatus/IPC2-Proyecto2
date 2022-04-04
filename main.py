from ListaCiudades import *
from ListaRobots import *
from cargarData import *
import easygui

ListadeCiudades = ListaCiudades()
ListadeRobots = ListaRobots()

def escogerMapaE(listadeCiudades):
        print("\n------------ ESCOJA UN MAPA ------------")
        listadeCiudades.imprimirCiudades()
        print(" ")
        nombreCiudad = input("Ingrese el nombre de una Ciudad -> ")
        print(" ")
        ciudadEscogida = listadeCiudades.buscarCiudad(nombreCiudad)
        if ciudadEscogida:       
                print("CIUDAD SELECCIONADA: ")
                print(f'█{ciudadEscogida.Ciudad.nombre}')
                print(" ")
                contadorRecurso = ciudadEscogida.Ciudad.matrizDispersa.contarRecursos()
                if contadorRecurso == 0:
                        print("NO HAY UNIDADES DE RECURSOS NO SE PUEDE REALIZAR LA MISIÓN ")
                if contadorRecurso == 1:
                        print("\nEXISTE SÓLO UNA UNIDAD DE RECURSOS ")
                        unidadRecursoEscogida = ciudadEscogida.Ciudad.matrizDispersa.seleccionAutomaticaRecurso()
                        print(f"SE HA ESCOGIDO LA UNIDAD EN LA POSICIÓN ({unidadRecursoEscogida.y},{unidadRecursoEscogida.x})")
                        return ciudadEscogida,unidadRecursoEscogida.y,unidadRecursoEscogida.x
                if contadorRecurso > 1:
                        print("\nESCOJA QUÉ UNIDAD DE RECURSOS DESEA EXTRAER ")
                        ciudadEscogida.Ciudad.matrizDispersa.mostrarUnidadesRecursos()
                        fila = input("Ingrese la fila -> ")
                        columna = input("Ingrese la columna -> ")
                        return ciudadEscogida,fila,columna   
        else: 
                print("NOMBRE DE CIUDAD INGRESADO NO EXISTE! ")
                return None," "," " 

def escogerMapaC(listadeCiudades):
        print("\n------------ ESCOJA UN MAPA ------------")
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
                        return None,0,0
                if contadorCiviles == 1:
                        print("\nEXISTE SÓLO UNA UNIDAD CIVIL ")
                        unidadCivilEscogida = ciudadEscogida.Ciudad.matrizDispersa.seleccionAutomaticaCivil()
                        print(f"SE HA ESCOGIDO LA UNIDAD EN LA POSICIÓN ({unidadCivilEscogida.y},{unidadCivilEscogida.x})")
                        return ciudadEscogida,unidadCivilEscogida.x,unidadCivilEscogida.y
                if contadorCiviles > 1:
                        print("\nESCOJA QUÉ UNIDAD CIVIL DESEA RESCATAR ")
                        ciudadEscogida.Ciudad.matrizDispersa.mostrarUnidadesCiviles()
                        fila = input("Ingrese la fila -> ")
                        columna = input("Ingrese la columna -> ")
                        return ciudadEscogida,fila,columna   
        else: 
                print("NOMBRE DE CIUDAD INGRESADO NO EXISTE! ")
                return None," "," " 

def escogerRobotC(listadeRobots):
        contadorChapinRescue = listadeRobots.contadorRobotsRescate()
        if contadorChapinRescue == 1:
                #------------------------------------------#
                #          SOLO UNA UNIDAD DE RESCATE      #
                #------------------------------------------#
                robotDeRescate = listadeRobots.escogerChapinRescueAutomatico()
                print("\nExiste sólo un Robot de rescate ")
                print(f'ChapinRescue: {robotDeRescate.nombre}')  
                return robotDeRescate.nombre                     
        else:  
                #------------------------------------------#
                #          MÁS DE UNA UNIDAD DE RESCATE    #
                #------------------------------------------#      
                print("\n------------ ESCOJA UN ROBOT ------------")
                listadeRobots.imprimirRobots() 
                print(" ")
                nombreRobot = input("Ingrese el nombre del Robot -> ")
                robotEscogido = listadeRobots.buscarRobot(nombreRobot,"ChapinRescue")                  
                if robotEscogido:
                        print(" ")
                        print("\nROBOT SELECCIONADO: ")
                        robotEscogido.Robot.imprimirDatos()
                        return robotEscogido.Robot.nombre       
                else:
                        print(" ")
                        print("ROBOT INGRESADO NO EXISTE ")
                        return " "
                
def escogerRobotE(listadeRobots):
        contadorChapinFighter = listadeRobots.contadorRobotsExtraccion()
        if contadorChapinFighter == 1:
                #------------------------------------------#
                #          SOLO UNA UNIDAD DE EXTRACCION   #
                #------------------------------------------#
                robotDeExtraccion = listadeRobots.escogerChapinFighterAutomatico()
                print("\nEXISTE SÓLO UN ROBOT DE EXTRACCIÓN: ")
                print(f'ChapinFighter: {robotDeExtraccion.nombre} Capacidad Combate: {robotDeExtraccion.capacidadCombate}')  
                return robotDeExtraccion.nombre, robotDeExtraccion.capacidadCombate                    
        else:  
                #------------------------------------------#
                #          MÁS DE UNA UNIDAD DE RESCATE    #
                #------------------------------------------#      
                print("\n------------ ESCOJA UN ROBOT ------------")
                listadeRobots.imprimirRobots(True) 
                print(" ")
                nombreRobot = input("Ingrese el nombre del Robot -> ")
                robotEscogido = listadeRobots.buscarRobot(nombreRobot,"ChapinFighter")                  
                if robotEscogido:
                        print(" ")
                        print("\nROBOT SELECCIONADO: ")
                        robotEscogido.Robot.imprimirDatos()
                        return robotEscogido.Robot.nombre,robotEscogido.Robot.capacidadCombate       
                else:
                        print(" ")
                        print("ROBOT INGRESADO NO EXISTE ")
                        return " ",0
                

def escogerEntrada(ciudadEscogida):
    contadorEntradas = ciudadEscogida.Ciudad.matrizDispersa.contarEntradas()  
    if contadorEntradas == 1:
            print("\nSÓLO EXISTE UNA ENTRADA")
            entradaEscogida = ciudadEscogida.Ciudad.matrizDispersa.seleccionAutomaticaEntrada()
            print(f"SE HA ESCOGIDO LA UNIDAD EN LA POSICIÓN ({entradaEscogida.y},{entradaEscogida.x})")
            return entradaEscogida.y,entradaEscogida.x
    elif contadorEntradas > 1:
            print("\nESCOJA UNA DE LAS SIGUIENTES ENTRADAS ")
            ciudadEscogida.Ciudad.matrizDispersa.mostrarEntradas()
            fila = input("Ingrese la fila -> ")
            columna = input("Ingrese la columna -> ")                        
            return fila,columna
                        
        

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
                   nombreRobot = escogerRobotC(listadeRobots)
                   ciudadEscogida,filaCivil,columnaCivil = escogerMapaC(listadeCiudades)
                   if ciudadEscogida:
                        columnaEntrada,filaEntrada = escogerEntrada(ciudadEscogida)
                        print("\n----DATOS------")
                        print(f"Se escogió el Robot -> {nombreRobot}" )
                        print(f"Ciudad Seleccionada: {ciudadEscogida.Ciudad.nombre}")
                        print(f"Unidad Civil Seleccionada en pos ({filaCivil},{columnaCivil})")
                        print(f"Entrada Seleccionada en pos ({filaEntrada},{columnaEntrada})")
                        ciudadEscogida.Ciudad.matrizDispersa.algoritmo(int(filaEntrada),int(columnaEntrada),int(columnaCivil),int(filaCivil),ciudadEscogida.Ciudad.nombre,nombreRobot)
                else:
                   print("No hay robots ChapinRescue, no se puede realizar misión de rescate")
                        
        elif opcion == "3":
              print('\n████████████ MISION EXTRACCION  ████████████')
              hayRobotsDeExtraccion = listadeRobots.hayRobotsDeExtraccion()
              if hayRobotsDeExtraccion:
                      nombreRobot,capacidadCombate = escogerRobotE(listadeRobots)
                      ciudadEscogida,filaRecurso,columnaRecurso = escogerMapaE(listadeCiudades)
                      if ciudadEscogida:
                        columnaEntrada,filaEntrada = escogerEntrada(ciudadEscogida)
                        print("\nRESUMEN DE DATOS: ")
                        print(f"SE ESCOGIÓ EL ROBOT {nombreRobot}")
                        print(f"CAPACIDAD DE COMBATE {capacidadCombate}")
                        print(f"Ciudad Seleccionada: {ciudadEscogida.Ciudad.nombre}")
                        print(f"Unidad de Recurso Seleccionada en pos ({filaRecurso},{columnaRecurso})")
                        print(f"Entrada Seleccionada en pos ({filaEntrada},{columnaEntrada})")
                
              else:
                      print("\nNo hay robots ChapinFighter, no se puede realizar misión de extracción")
        elif opcion == "4": 
                print("Saliendo...")
        else:
                print("Ingrese una opción valida! ")
    
    print("HA SALIDO DE LA EJECUCIÓN DEL PROGRAMA CON ÉXITO ")
    

menuPrincipal(ListadeCiudades,ListadeRobots)