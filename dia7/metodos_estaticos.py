class Pajaro: # Definición de la clase Pajaro
    alas = True # Atributo de clase

    def __init__(self,color,especie): # Método constructor
        self.color =color # Atributo color
        self.especie = especie # Atributo especie
    
    def piar(self): # Método piar
        print("Pio Pio, Mi color es "+self.color+" y mi especie es "+self.especie)

    def volar(self,metros): # Método volar
        print(f"El pájaro ha volado {metros} metros")

    def pintar_negro(self):
        self.color = "negro"
        print("el pajaro es de color "+self.color)

    @classmethod 
    def poner_huevos(cls, cantidad): 
        print(f"Puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.mirar()