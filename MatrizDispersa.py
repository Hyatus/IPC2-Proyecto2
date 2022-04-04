from NodoEncabezado import NodoEncabezado
from ListaEncabezado import ListaEncabezado
from NodoInterno import *
import os
import numpy as np
from PilaPosValidas import *
from clasePosValida import *

class MatrizDispersa():
    def __init__(self, capa = None):
        self.capa = capa
        self.filas = ListaEncabezado("LISTAS")
        self.columnas = ListaEncabezado("COLUMNAS")
        self.pilaPosValidas = PilaPosValidas()
        self.Dx = 0
        self.Dy = 0
        self.nombreCiudad = None
        self.nombreRobot = None
    
    def insertar(self, nodoInterno):
        encabezadoX = self.filas.getEncabezado(nodoInterno.x)
        encabezadoY = self.columnas.getEncabezado(nodoInterno.y)

        if encabezadoX == None:
            encabezadoX = NodoEncabezado(nodoInterno.x)
            self.filas.insertarEncabezado(encabezadoX)
        
        if encabezadoY == None:
            encabezadoY = NodoEncabezado(nodoInterno.y)
            self.columnas.insertarEncabezado(encabezadoY)
        
        if encabezadoX.acceso == None:
            encabezadoX.acceso = nodoInterno
        else:
            #INSERTAR NODO INTERNO EN FILA
            if nodoInterno.y < encabezadoX.acceso.y:
                nodoInterno.derecha = encabezadoX.acceso
                encabezadoX.acceso.izquierda = nodoInterno
                encabezadoX.acceso = nodoInterno
            else:
                aux = encabezadoX.acceso
                while aux != None:
                    if nodoInterno.y < aux.y:
                        nodoInterno.derecha = aux
                        nodoInterno.izquierda = aux.izquierda
                        aux.izquierda.derecha = nodoInterno
                        aux.izquierda = nodoInterno
                        break
                    else:
                        if aux.derecha == None:
                            aux.derecha = nodoInterno
                            nodoInterno.izquierda = aux
                            break
                        else:
                            aux = aux.derecha

        if encabezadoY.acceso == None:
            encabezadoY.acceso = nodoInterno
        else:
             #INSERTAR NODO INTERNO EN COLUMNA
            if nodoInterno.x < encabezadoY.acceso.x:
                nodoInterno.abajo = encabezadoY.acceso
                encabezadoY.acceso.arriba = nodoInterno
                encabezadoY.acceso = nodoInterno
            else:
                aux2 = encabezadoY.acceso
                while aux2 != None:
                    if nodoInterno.x < aux2.x:
                        nodoInterno.abajo = aux2
                        nodoInterno.arriba = aux2.arriba
                        aux2.arriba.abajo = nodoInterno
                        aux2.arriba = nodoInterno
                        break
                    else:
                        if aux2.abajo == None:
                            aux2.abajo = nodoInterno
                            nodoInterno.arriba = aux2
                            break
                        else:
                            aux2 = aux2.abajo
                            
    def insertarMilitar(self,fila:int,columna:int,poder:int):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.x == fila and aux2.y == columna:
                        aux2.caracter = 'M'
                        aux2.poder = poder
                    #print(f'Posicion: ({aux2.x} , {aux2.y}) Caracter: {aux2.caracter}')
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
                
    def contarRecursos(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        contadorRecursos = 0
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'R':
                        contadorRecursos += 1
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
                
        return contadorRecursos
           
    def contarCiviles(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        contadorCiviles = 0
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'C':
                         contadorCiviles += 1
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
                
        return contadorCiviles
    
    def contarEntradas(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        contadorEntradas = 0
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'E':
                         contadorEntradas += 1
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
                
        return contadorEntradas
    
    def seleccionAutomaticaCivil(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'C':
                        return aux2
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
                
    def seleccionAutomaticaRecurso(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'R':
                        return aux2
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
                
    def seleccionAutomaticaEntrada(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'E':
                        return aux2
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        
    def mostrarUnidadesCiviles(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'C':
                        print(f'█ Unidad Civil en posición (fila:{aux2.x},col:{aux2.y})')
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso

    def mostrarUnidadesRecursos(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'R':
                        print(f'█ Unidad Recurso en posición (fila:{aux2.x},col:{aux2.y})')
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
    
    def mostrarEntradas(self):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.caracter == 'E':
                        print(f'█ Entrada en posición (fila:{aux2.x},col:{aux2.y})')
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
    
    def graficarDot(self, nombreCiudad,nombreRobot):
        #-- lo primero es settear los valores que nos preocupan
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        grafo += '\nroot[label = \"capa: '+ str(self.capa) +'\", group=1]\n'
        grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                    \n'''.format(f'Tipo de misión: rescate \nUnidad civil rescatada: {self.Dx},{self.Dy} \nRobot utilizado: {nombreRobot} (Chapin Rescue)')

        # --- lo siguiente es escribir los nodos encabezados, empezamos con las filas, los nodos tendran el foramto Fn
        x_fila = self.filas.primero
        while x_fila != None:
            grafo += 'F{}[label="F{}",fillcolor="plum",group=1];\n'.format(x_fila.id, x_fila.id)
            x_fila = x_fila.siguiente

        # --- apuntamos los nodos F entre ellos
        x_fila = self.filas.primero
        while x_fila != None:
            if x_fila.siguiente != None:
                grafo += 'F{}->F{};\n'.format(x_fila.id, x_fila.siguiente.id)
                grafo += 'F{}->F{};\n'.format(x_fila.siguiente.id, x_fila.id)
            x_fila = x_fila.siguiente

        # --- Luego de los nodos encabezados fila, seguimos con las columnas, los nodos tendran el foramto Cn
        y_columna = self.columnas.primero
        while y_columna != None:
            group = int(y_columna.id)+1
            grafo += 'C{}[label="C{}",fillcolor="powderblue",group={}];\n'.format(y_columna.id, y_columna.id, str(group))
            y_columna = y_columna.siguiente
        
        # --- apuntamos los nodos C entre ellos
        cont = 0
        y_columna = self.columnas.primero
        while y_columna is not None:
            if y_columna.siguiente is not None:
                grafo += 'C{}->C{}\n'.format(y_columna.id, y_columna.siguiente.id)
                grafo += 'C{}->C{}\n'.format(y_columna.siguiente.id, y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente

        # --- luego que hemos escrito todos los nodos encabezado, apuntamos el nodo root hacua ellos 
        y_columna = self.columnas.primero
        x_fila = self.filas.primero
        grafo += 'root->F{};\n root->C{};\n'.format(x_fila.id, y_columna.id)
        grafo += '{rank=same;root;'
        cont = 0
        y_columna = self.columnas.primero
        while y_columna != None:
            grafo += 'C{};'.format(y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente
        grafo += '}\n'
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont += 1
            while aux2 != None:
                if aux2.caracter == '*':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="black"];\n'.format(aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)   
                elif aux2.caracter == 'R':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="gray"];\n'.format(aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)     
                elif aux2.caracter == 'C': 
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="blue"];\n'.format(aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1) 
                elif aux2.caracter == 'E':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="green"];\n'.format(aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)  
                elif aux2.caracter == 'M':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="red"];\n'.format(aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1) 
                elif aux2.correcto == 'X':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="blueviolet"];\n'.format(aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1) 
                elif aux2.correcto == 'Y':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="yellow"];\n'.format(aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)    
                elif aux2.caracter == ' ':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="white"];\n'.format(aux2.x, aux2.y, aux2.caracter, int(aux2.y)+1)   
   
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux is not None:
            rank = '{'+f'rank = same;F{aux.id};'
            cont = 0
            while aux2 != None:
                if cont == 0:
                    grafo += 'F{}->N{}_{};\n'.format(aux.id, aux2.x, aux2.y)
                    grafo += 'N{}_{}->F{};\n'.format(aux2.x, aux2.y, aux.id)
                    cont += 1
                if aux2.derecha != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.x, aux2.y, aux2.derecha.x, aux2.derecha.y)
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.derecha.x, aux2.derecha.y, aux2.x, aux2.y)

                rank += 'N{}_{};'.format(aux2.x, aux2.y)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
            grafo += rank+'}\n'
        aux = self.columnas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont = 0
            grafo += ''
            while aux2 != None:
                if cont == 0:
                    grafo += 'C{}->N{}_{};\n'.format(aux.id, aux2.x, aux2.y)
                    grafo += 'N{}_{}->C{};\n'.format(aux2.x, aux2.y, aux.id) 
                    cont += 1
                if aux2.abajo != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.abajo.x, aux2.abajo.y, aux2.x, aux2.y)
                    grafo += 'N{}_{}->N{}_{};\n'.format( aux2.x, aux2.y,aux2.abajo.x, aux2.abajo.y)
                aux2 = aux2.abajo
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        grafo += '}'

        # ---- luego de crear el contenido del Dot, procedemos a colocarlo en un archivo
        dot = "matriz_{}_dot.txt".format(nombreCiudad.strip())
        with open(dot, 'w') as f:
            f.write(grafo)
        result = "matriz_{}.pdf".format(nombreCiudad.strip())
        os.system("dot -Tpdf " + dot + " -o " + result) 

    def calcularH(self,X1:int,Y1:int,X2:int,Y2:int):
                                     
        print("#CALCULAR H#")        
                                 
        print(f"VALORES INGRESADOS: |{X1}-{Y2}|+|{X2}-{Y1}|")
        h = np.abs(X1-Y2) + np.abs(X2-Y1)
        print(f"Valor de H es {h} - ({X1},{Y1})")
        return h
       
    def buscarNodo(self,columna:int,fila:int):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.x == fila and aux2.y == columna:
                        print(f"Nodo encontrado pos({aux2.x},{aux2.y}) caracter: {aux2.caracter}")
                        return aux2
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        return None
    
    def marcarVisitado(self,columna,fila):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.x == fila and aux2.y == columna:
                        aux2.visitado = True
                        print(f"Marca Visitado en pos({aux2.x},{aux2.y}) caracter: {aux2.caracter}")
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
                
    def marcarCorrecto(self,columna,fila):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.x == fila and aux2.y == columna:
                        aux2.correcto = 'Y'
                        print(f"Marca Correcto en pos({aux2.x},{aux2.y}) caracter: {aux2.caracter}")
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
    
    def limpiarRecorrido(self):    
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                   aux2.visitado = False
                   aux2.correcto = None
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
    
    def marcarIncorrecto(self,columna,fila):
        aux = self.filas.primero
        aux2 = aux.acceso
        
        while aux is not None:
            while aux2 != None:
                if aux2.derecha != None:
                    if aux2.x == fila and aux2.y == columna:
                        aux2.correcto = 'X'
                        print(f"Marca Incorrecto en pos({aux2.x},{aux2.y}) caracter: {aux2.caracter}")
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        
    def buscarNuevoCamino(self):
        self.pilaPosValidas.recorrer()
        nodoPos = self.pilaPosValidas.desapilar()
        nodoAux = self.buscarNodo(nodoPos.Yv,nodoPos.Xv)
        
        contador = 0
        
        while nodoAux != None and self.pilaPosValidas.noEsVacia():
            
            print(f"# -NC- NODO ACTUAL EN COORDENADAS ({nodoAux.x},{nodoAux.y}) ######")
            VecinoArriba = self.buscarNodo(nodoAux.y,nodoAux.x-1)
            VecinoAbajo = self.buscarNodo(nodoAux.y,nodoAux.x+1)
            VecinoDerecha = self.buscarNodo(nodoAux.y+1,nodoAux.x)
            VecinoIzquierda = self.buscarNodo(nodoAux.y-1,nodoAux.x)
            
            if (VecinoArriba != None and (VecinoArriba.caracter == " " or VecinoArriba.caracter == 'E' or VecinoArriba.caracter == 'C') and VecinoArriba.correcto != 'Y' and VecinoArriba.correcto != 'X'):
                    print(" -> Camino disponible Hacia Arriba")
                    self.algoritmo(VecinoArriba.y,VecinoArriba.x,self.Dx,self.Dy,self.nombreCiudad,self.nombreRobot)
                    break
            else:       
                if (VecinoAbajo != None and (VecinoAbajo.caracter == " " or VecinoAbajo.caracter == 'E' or VecinoAbajo.caracter == 'C') and VecinoAbajo.correcto != 'Y' and VecinoAbajo.correcto != 'X'):
                        print(" -> Camino disponible Hacia Abajo")
                        self.algoritmo(VecinoAbajo.y,VecinoAbajo.x,self.Dx,self.Dy,self.nombreCiudad,self.nombreRobot)
                        break
                else:        
                    if (VecinoDerecha != None and (VecinoDerecha.caracter == " " or VecinoDerecha.caracter == 'E' or VecinoDerecha.caracter == 'C') and VecinoDerecha.correcto != 'Y' and VecinoDerecha.correcto != 'X'):
                            print(" -> Camino disponible Hacia Derecha")
                            self.algoritmo(VecinoDerecha.y,VecinoDerecha.x,self.Dx,self.Dy,self.nombreCiudad,self.nombreRobot)
                            break
                    else:
                        if (VecinoIzquierda != None and (VecinoIzquierda.caracter == " " or VecinoIzquierda.caracter == 'E' or VecinoIzquierda.caracter == 'C') and VecinoIzquierda.correcto != 'Y' and VecinoIzquierda.correcto != 'X'):
                            print(" -> Camino disponible Hacia Izquierda")
                            self.algoritmo(VecinoIzquierda.y,VecinoIzquierda.x,self.Dx,self.Dy,self.nombreCiudad,self.nombreRobot)
                            break
                        else:
                            self.marcarIncorrecto(nodoAux.y,nodoAux.x)
            
            nodoPos = self.pilaPosValidas.desapilar()
            nodoAux = self.buscarNodo(nodoPos.Yv,nodoPos.Xv)
            contador += 1
               
    def algoritmo(self,Ex,Ey,Dx,Dy,nombreCiudad,nombreRobot):
        #fila columna fila columna
        nodoEntrada = self.buscarNodo(Ex,Ey)
        nodoSalida = self.buscarNodo(Dx,Dy)
        self.marcarVisitado(Ex,Ey)
        contador = 0
        self.Dx = Dx
        self.Dy = Dy
        self.nombreCiudad = nombreCiudad
        self.nombreRobot = nombreRobot
        X2 = int(Dx)
        Y2 = int(Dy)
        if nodoEntrada and nodoSalida:
            nodoAux = nodoEntrada
            print(f"Coordenadas nodo salida ({Dx},{Dy})")
            print(f"Coordenadas nodo Entrada ({Ex},{Ey})")
            
            while nodoAux != None:
                
                print("------------------------------------------------")
                                                      #fila          col
                print(f"# NODO ACTUAL EN COORDENADAS ({nodoAux.x},{nodoAux.y}) ######")
                self.marcarCorrecto(nodoAux.y,nodoAux.x)
                posValidaAux = PosicionValida(nodoAux.x,nodoAux.y)
                self.pilaPosValidas.apilar(posValidaAux)
                print("ARRIBA")  
                VecinoArriba = self.buscarNodo(nodoAux.y,nodoAux.x-1)
                print("ABAJO")
                VecinoAbajo = self.buscarNodo(nodoAux.y,nodoAux.x+1)
                print("DERECHA")
                VecinoDerecha = self.buscarNodo(nodoAux.y+1,nodoAux.x)
                print("IZQUIERDA")
                VecinoIzquierda = self.buscarNodo(nodoAux.y-1,nodoAux.x)
                fArriba = 999999
                fAbajo = 999999
                fDerecha = 999999
                fIzquierda = 999999
                contadorBloqueos = 0
                
                if (VecinoArriba != None and (VecinoArriba.caracter == 'M' or VecinoArriba.caracter == 'R' or VecinoArriba.caracter == "*" or VecinoArriba.visitado == True)):
                    contadorBloqueos += 1
                    
                if (VecinoAbajo != None and (VecinoAbajo.caracter == 'M' or VecinoAbajo.caracter == 'R' or VecinoAbajo.caracter == "*" or VecinoAbajo.visitado == True)):
                    contadorBloqueos += 1
                    
                if (VecinoDerecha != None and (VecinoDerecha.caracter == 'M' or VecinoDerecha.caracter == 'R' or VecinoDerecha.caracter == "*" or VecinoDerecha.visitado == True)):
                    contadorBloqueos += 1
                    
                if (VecinoIzquierda != None and (VecinoIzquierda.caracter == 'M' or VecinoIzquierda.caracter == 'R' or VecinoIzquierda.caracter == "*" or VecinoIzquierda.visitado == True)):
                    contadorBloqueos += 1

                if nodoAux.caracter == 'C':
                    print("MISION CUMPLIDA")
                    self.graficarDot(nombreCiudad,nombreRobot)
                    self.limpiarRecorrido()
                    self.pilaPosValidas.vaciar()
                    return
                else: 
                    if contadorBloqueos > 3:
                        print("ATASCO")
                        self.buscarNuevoCamino()
                        break
                                   
            
                if VecinoArriba != None and VecinoArriba.caracter != 'M' and VecinoArriba.caracter != '*' and VecinoArriba.caracter != 'R' and VecinoArriba.visitado == False and VecinoArriba != nodoAux:
                     print(f"Vecino Arriba visitado? {VecinoArriba.visitado}")
                     #self.marcarVisitado(VecinoArriba.y,VecinoArriba.x)
                     X1 = int(VecinoArriba.x)
                     Y1 = int(VecinoArriba.y)
                     hArriba = self.calcularH(X1,Y1,X2,Y2)
                     fArriba = hArriba
                     print(f"valor F Arriba = {fArriba}")
            
                    
                if VecinoAbajo != None and VecinoAbajo.caracter != 'M' and VecinoAbajo.caracter != '*' and VecinoAbajo.caracter != 'R' and VecinoAbajo.visitado == False and VecinoAbajo != nodoAux:
                     print(f"Vecino Abajo visitado? {VecinoAbajo.visitado}")
                     #self.marcarVisitado(VecinoAbajo.y,VecinoAbajo.x)
                     X1 = int(VecinoAbajo.x)
                     Y1 = int(VecinoAbajo.y)
                     hAbajo = self.calcularH(X1,Y1,X2,Y2)
                     fAbajo = hAbajo
                     print(f"valor F Abajo = {fAbajo}")
           
                    
                if VecinoDerecha != None and VecinoDerecha.caracter != 'M' and VecinoDerecha.caracter != '*' and VecinoDerecha.caracter != 'R' and VecinoDerecha.visitado == False and VecinoDerecha != nodoAux:
                     print(f"Vecino Derecha visitado? {VecinoDerecha.visitado}")
                     #self.marcarVisitado(VecinoDerecha.y,VecinoDerecha.x)
                     X1 = int(VecinoDerecha.x)
                     Y1 = int(VecinoDerecha.y)
                     hDerecha = self.calcularH(X1,Y1,X2,Y2)
                     fDerecha = hDerecha
                     print(f"valor F Derecha = {fDerecha}") 
          
                     
                if VecinoIzquierda != None and VecinoIzquierda.caracter != 'M' and VecinoIzquierda.caracter != '*' and VecinoIzquierda.caracter != 'R' and VecinoIzquierda.visitado == False and VecinoIzquierda != nodoAux:
                     print(f"Vecino Izquierda visitado? {VecinoIzquierda.visitado}")
                     #self.marcarVisitado(VecinoIzquierda.y,VecinoIzquierda.x)
                     X1 = int(VecinoIzquierda.x)
                     Y1 = int(VecinoIzquierda.y)
                     hIzquierda = self.calcularH(X1,Y1,X2,Y2)
                     fIzquierda = hIzquierda
                     print(f"valor F Izquierda = {fIzquierda}")  
           
                     
                print(f"fArriba {fArriba} - fAbajo {fAbajo} - fDerecha {fDerecha} - fIzquierda {fIzquierda}")     
                
                if fAbajo == 999999 and fArriba == 999999 and fDerecha == 999999 and fIzquierda == 999999:
                    print("MISION IMPOSIBLE ")
                    self.graficarDot("MisionImposible",self.nombreRobot)
                    break
                
                if fAbajo < fArriba and fAbajo < fDerecha and fAbajo < fIzquierda:
                    print(f"#ITERACION # {contador}")
                    print(f"Vecino más cercano en pos ({VecinoAbajo.x},{VecinoAbajo.y})")
                    nodoAux = VecinoAbajo
                    self.marcarVisitado(nodoAux.y,nodoAux.x)
                else:
                    if fArriba < fAbajo and fArriba < fDerecha and fArriba < fIzquierda:
                        print(f"#ITERACION # {contador}")
                        print(f"Vecino más cercano en pos ({VecinoArriba.x},{VecinoArriba.y})")
                        nodoAux = VecinoArriba
                        self.marcarVisitado(nodoAux.y,nodoAux.x)
                    else:
                        if fDerecha < fArriba and fDerecha < fAbajo and fDerecha < fIzquierda:
                            print(f"#ITERACION # {contador}")
                            print(f"Vecino más cercano en pos ({VecinoDerecha.x},{VecinoDerecha.y})")
                            nodoAux = VecinoDerecha
                            self.marcarVisitado(nodoAux.y,nodoAux.x)
                        else:
                            if fIzquierda < fArriba and fIzquierda < fDerecha and fIzquierda < fAbajo:
                                print(f"#ITERACION # {contador}")
                                print(f"Vecino más cercano en pos ({VecinoIzquierda.x},{VecinoIzquierda.y})")
                                nodoAux = VecinoIzquierda
                                self.marcarVisitado(nodoAux.y,nodoAux.x)
                            else:
                                if ((fArriba != 999999) and (fArriba == fAbajo or fArriba == fDerecha or fArriba == fIzquierda)):
                                    print(f"#ITERACION # {contador}")
                                    print(f"Vecino más cercano en pos ({VecinoArriba.x},{VecinoArriba.y})")
                                    nodoAux = VecinoArriba
                                    self.marcarVisitado(nodoAux.y,nodoAux.x)
                                else:
                                    if ((fAbajo != 999999) and (fAbajo == fArriba or fAbajo == fDerecha or fAbajo == fIzquierda)):
                                        print(f"#ITERACION # {contador}")
                                        print(f"Vecino más cercano en pos ({VecinoAbajo.x},{VecinoAbajo.y})")
                                        nodoAux = VecinoAbajo
                                        self.marcarVisitado(nodoAux.y,nodoAux.x)
                                    else:
                                        if ((fDerecha != 999999) and (fDerecha == fArriba or fDerecha == fAbajo or fDerecha == fIzquierda)):
                                            print(f"#ITERACION # {contador}")
                                            print(f"Vecino más cercano en pos ({VecinoDerecha.x},{VecinoDerecha.y})")
                                            nodoAux = VecinoDerecha
                                            self.marcarVisitado(nodoAux.y,nodoAux.x)
                                        else: 
                                            if ((fIzquierda != 999999) and (fIzquierda == fArriba or fIzquierda == fAbajo or fIzquierda == fDerecha)):
                                                print(f"#ITERACION # {contador}")
                                                print(f"Vecino más cercano en pos ({VecinoIzquierda.x},{VecinoIzquierda.y})")
                                                nodoAux = VecinoIzquierda
                                                self.marcarVisitado(nodoAux.y,nodoAux.x)

                contador +=1   
                
        else:
            print("Coordenadas ingresadas inválidas")
                
            
            

        