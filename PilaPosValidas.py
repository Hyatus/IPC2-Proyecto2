from clasePosValida import *

class PilaPosValidas: 
  def __init__(self):
    self.pila = []
  
  def apilar(self,PosicionValida):
    self.pila.append(PosicionValida)

  def recorrer(self):
    for elemento in self.pila:
        print(f" Coordenada: ({elemento.Xv},{elemento.Yv})")

  def desapilar(self):
      return self.pila.pop()  
        

  def vaciar(self):
    self.pila.clear() 

  def size(self):
     return len(self.pila) 
   
  def noEsVacia(self):
      if not self.pila:
            #Está vacía 
            return False
      else:
            return True
  