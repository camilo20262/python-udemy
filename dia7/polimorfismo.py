class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre +"dice Muuuu")

class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre +"dice Beeee")


vaca=Vaca("Lola")
oveja=Oveja("Dolly")

vaca.hablar()
oveja.hablar()
        