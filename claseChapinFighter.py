class ChapinFighter: 
  def __init__(self,nombre:str,tipo:str,capacidadCombate:int): 
    self.nombre = nombre
    self.tipo = tipo
    self.capacidadCombate = capacidadCombate
    
    
  def imprimirDatos(self):
        print(f'nombre: {self.nombre} Capacidad de Combate: {self.capacidadCombate}')
    
    