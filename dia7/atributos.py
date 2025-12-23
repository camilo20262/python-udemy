class Pajaro: # Definición de la clase Pajaro
    alas = True # Atributo de clase

    def __init__(self,color,especie): # Método constructor
        self.color =color # Atributo color
        self.especie = especie # Atributo especie
 
mi_pajaro = Pajaro("Verde","Loro") # Crear una instancia de la clase Pajaro

print(mi_pajaro.color)  # VERDE
print(mi_pajaro.especie)  # Loro
print(f"Tengo un pajaro de color {mi_pajaro.color} y de especie {mi_pajaro.especie}") # Tengo un pajaro de color Verde y de especie Loro
