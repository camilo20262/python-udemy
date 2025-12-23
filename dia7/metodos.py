class Pajaro: # Definición de la clase Pajaro
    alas = True # Atributo de clase

    def __init__(self,color,especie): # Método constructor
        self.color =color # Atributo color
        self.especie = especie # Atributo especie
    
    def piar(self): # Método piar
        print("Pio Pio, Mi color es "+self.color+" y mi especie es "+self.especie)

    def volar(self,metros): # Método volar
        print(f"El pájaro ha volado {metros} metros")

piolin = Pajaro("Amarillo","Canario") # Crear una instancia de la clase Pajaro

piolin.piar() # Llamar al método piar
piolin.volar(100) # Llamar al método volar con 100 metros