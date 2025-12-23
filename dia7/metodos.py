class Pajaro: # Definición de la clase Pajaro
    alas = True # Atributo de clase

    def __init__(self,color,especie): # Método constructor
        self.color =color # Atributo color
        self.especie = especie # Atributo especie
    
    def piar(self): # Método piar
        print("Pio Pio")

    def volar(self,metros): # Método volar
        print(f"El pájaro ha volado {metros} metros")