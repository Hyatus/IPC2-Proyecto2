from NodoCiudad import *
from claseCiudad import *

class ListaCiudades: 
  def __init__(self):
    self.primero = None 

  def insertarCiudad(self,Ciudad):
    if self.primero is None: 
      self.primero = NodoCiudad(Ciudad=Ciudad) 
      return 
    
    #Verificamos primero si la ciudad no existe aún, si existe entonces la sobreescribimos 
    existeCiudad = self.buscarCiudad(Ciudad.nombre)
    
    if existeCiudad:
          existeCiudad.Ciudad = Ciudad
    else:
          
      actual = self.primero 
    
      while actual.siguiente: 
        actual = actual.siguiente
      
      actual.siguiente = NodoCiudad(Ciudad=Ciudad)  

  def imprimirCiudades(self): 
    actual = self.primero
    while actual != None:
      print(f'Ciudad: {actual.Ciudad.nombre}')
      actual = actual.siguiente 
      
      
  def buscarCiudad(self,nombreCiudad:str):
        actual = self.primero 
        
        while actual and actual.Ciudad.nombre != nombreCiudad:
            actual = actual.siguiente
            
        if actual:
            return actual 
        else:
            return None  
          

     

