class Animal:
    def __init__(self,color,edad):
        self.color = color
        self.edad = edad

    def nacer(self):
        print("Este animal ha nacido")
    
    def hablar(self):
        print("el animal emite un sonido")

class Pajaro(Animal):
    def hablar(self):
        print("pio, pio")
piolin= Pajaro("amarillo",3)

piolin.hablar()