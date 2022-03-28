from MatrizDispersa import MatrizDispersa
from NodoInterno import NodoInterno
from ListaCiudades import *
from claseChapinFighter import ChapinFighter
from claseChapinRescue import ChapinRescue
from ListaRobots import *



def leerXML(path,ListaCiudades,ListaRobots):
    try:
        import xml.etree.ElementTree as ET
        tree = ET.parse(path)
        root = tree.getroot()
        columnas = 1
        matrizAux = None
        nombreCiudad = ""
        contadorMatriz = 0
        for elementos in root:
            #print(elementos.tag,elementos.attrib)
            for ciudades in elementos.iter('ciudad'):
                # print(ciudades.tag,ciudades.attrib)
                for nombre in ciudades.iter('nombre'):
                    filas = int(nombre.attrib['filas'])
                    columnas = int(nombre.attrib['columnas'])
                    nombreCiudad = nombre.text
                    #print(f"\nFilas: {filas} - Columnas: {columnas} - Nombre: {nombreCiudad}")
                    matrizAux = MatrizDispersa(contadorMatriz)
                    contadorMatriz += 1
                for fila in ciudades.iter('fila'):
                    numeroFila = int(fila.attrib['numero'])
                    #print(f'Fila número {numeroFila}')
                    contenidoColumnas = fila.text
                    i = 1
                    while i < len(contenidoColumnas)-1:
                        nodoAux = NodoInterno(numeroFila,i,contenidoColumnas[i],0)
                        matrizAux.insertar(nodoAux)
                        #print(contenidoColumnas[i],end="-")
                        #print(f"Número Columna {i} ")
                        i += 1
                        
                ciudadAux = Ciudad(nombreCiudad,matrizAux)
                ListaCiudades.insertarCiudad(ciudadAux) 
                
                for unidadMilitar in ciudades.iter('unidadMilitar'):
                    filaUM = unidadMilitar.attrib['fila']
                    columnaUM = unidadMilitar.attrib['columna']
                    poderMilitar = unidadMilitar.text
                    #print(f'filaUM: {filaUM} colUM: {columnaUM} poderMilitar: {poderMilitar}')
                    matrizAux.insertarMilitar(int(filaUM),int(columnaUM),int(poderMilitar))
                        
            for robots in elementos.iter('robot'):
                for nombre in robots.iter('nombre'):
                    nombreRobot = nombre.text
                    tipoRobot = nombre.attrib['tipo']
                    if tipoRobot == 'ChapinFighter':
                        capacidadPelea = nombre.attrib['capacidad']
                        ChapinFighterAux = ChapinFighter(nombreRobot,tipoRobot,capacidadPelea)
                        #print(f'Nombre: {nombreRobot} Tipo: {tipoRobot} Capacidad: {capacidadPelea}')
                        ListaRobots.insertarRobot(ChapinFighterAux)
                    elif tipoRobot == 'ChapinRescue':
                        chapinRescueAux = ChapinRescue(nombreRobot,tipoRobot)
                        ListaRobots.insertarRobot(chapinRescueAux)
                        #print(f'Nombre: {nombreRobot} Tipo: {tipoRobot}')
                        
                       
        # FILA COLUMNA
        #        matrizAux.insertarMilitar(2,5)   
        #        matrizAux.insertarMilitar(5,5)             
        #matrizAux.graficarDot("Final")
        print("CARGA DE DATOS REALIZADA CON ÉXITO!")
    except:
        print("ERROR AL CARGAR ARCHIVO! ")    
        

#listadeCiudades = ListaCiudades()
#listadeRobots = ListaRobots()
#leerXML("archivo.xml",listadeCiudades,listadeRobots)
#listadeCiudades.imprimirCiudades()
#listadeRobots.imprimirRobots(True)
#ciudadGuate = listadeCiudades.buscarCiudad("CiudadGuate")
#ciudadGuate.Ciudad.matrizDispersa.graficarDot("CiudadGuate")
#ciudadGuate = listadeCiudades.buscarCiudad("CiudadPetapa")
#ciudadGuate.Ciudad.matrizDispersa.graficarDot("CiudadPetapa")