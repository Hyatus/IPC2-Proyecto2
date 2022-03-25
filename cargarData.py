from MatrizDispersa import MatrizDispersa
from NodoInterno import NodoInterno


def leerXML(path):
    try:
        import xml.etree.ElementTree as ET
        tree = ET.parse(path)
        root = tree.getroot()
        columnas = 1
        matrizAux = None
        nombreCiudad = ""
        contadorMatriz = 0
        for elementos in root:
            print(elementos.tag,elementos.attrib)
            for ciudades in elementos.iter('ciudad'):
                # print(ciudades.tag,ciudades.attrib)
                for nombre in ciudades.iter('nombre'):
                    filas = int(nombre.attrib['filas'])
                    columnas = int(nombre.attrib['columnas'])
                    nombreCiudad = nombre.text
                    print(f"\nFilas: {filas} - Columnas: {columnas} - Nombre: {nombreCiudad}")
                    matrizAux = MatrizDispersa(contadorMatriz)
                    contadorMatriz += 1
                for fila in ciudades.iter('fila'):
                    numeroFila = int(fila.attrib['numero'])
                    print(f'Fila número {numeroFila}')
                    contenidoColumnas = fila.text
                    i = 1
                    while i < len(contenidoColumnas)-1:
                        nodoAux = NodoInterno(numeroFila,i,contenidoColumnas[i])
                        matrizAux.insertar(nodoAux)
                        print(contenidoColumnas[i],end="-")
                        print(f"Número Columna {i} ")
                        i += 1
        # FILA COLUMNA
        matrizAux.recorrerMatriz(2,5)   
        matrizAux.recorrerMatriz(5,5)             
        #nodoMilitar = NodoInterno(4,2,'M') 
        #matrizAux.insertar(nodoMilitar)
        matrizAux.graficarDot("Final")
                        
                  
  
        print("CARGA DE DATOS REALIZADA CON ÉXITO!")
    except:
        print("ERROR AL CARGAR ARCHIVO! ")    
        


leerXML("archivo.xml")