from nodoRobot import *
from claseChapinFighter import *
from claseChapinRescue import *


class ListaRobots: 
  def __init__(self):
    self.primero = None 

  def insertarRobot(self,Robot):
    if self.primero is None: 
      self.primero = NodoRobot(Robot=Robot) 
      return 
    
    #Verificamos primero si el robot no existe aún, si existe entonces la sobreescribimos 
    existeRobot = self.buscarRobot(Robot.nombre,Robot.tipo)
    
    if existeRobot:
          existeRobot.Robot= Robot
    else:
          
      actual = self.primero 
    
      while actual.siguiente: 
        actual = actual.siguiente
      
      actual.siguiente = NodoRobot(Robot=Robot)  

  def imprimirRobots(self,esChapinFighter=False): 
      
    tipoRobot = None  
    if esChapinFighter: 
       tipoRobot = "ChapinFighter"
    else:
       tipoRobot = "ChapinRescue"
       
    actual = self.primero
    
    while actual != None:
        if actual.Robot.tipo == tipoRobot:
            actual.Robot.imprimirDatos()    
           
        actual = actual.siguiente    
  
  def buscarRobot(self,nombreRobot:str,tipoRobot:str):
        actual = self.primero 
        
        while actual:
            if actual.Robot.nombre == nombreRobot and actual.Robot.tipo == tipoRobot:
               return actual
            actual = actual.siguiente
            
        return None
      
  def hayRobotsDeRescate(self):
      actual = self.primero
      
      while actual != None:
        if actual.Robot.tipo == "ChapinRescue":
              return True
        actual = actual.siguiente
      
      return False
        
  def hayRobotsDeExtraccion(self):
      actual = self.primero
      
      while actual != None:
        if actual.Robot.tipo == "ChapinFighter":
              return True
        actual = actual.siguiente
      
      return False
     
  def contadorRobotsRescate(self):
      actual = self.primero
      contador = 0
      while actual != None:
        if actual.Robot.tipo == "ChapinRescue":
            contador += 1
        actual = actual.siguiente
      
      return contador 
    
  def escogerChapinRescueAutomatico(self):
      actual = self.primero
      while actual != None:
        if actual.Robot.tipo == "ChapinRescue":
            return actual.Robot
        actual = actual.siguiente 
        
  def escogerChapinFighterAutomatico(self):
      actual = self.primero
      while actual != None:
        if actual.Robot.tipo == "ChapinFighter":
            return actual.Robot
        actual = actual.siguiente 
            
  def contadorRobotsExtraccion(self):
      actual = self.primero
      contador = 0
      while actual != None:
        if actual.Robot.tipo == "ChapinFighter":
            contador += 1
        actual = actual.siguiente
      
      return contador 
    
    
        
        