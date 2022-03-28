class NodoInterno():
    def __init__(self, x = None, y = None, caracter = None, poder = 0):
        self.caracter = caracter
        self.x = x
        self.y = y
        self.poder = poder
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None