class Animal:
    def __init__(self,color,edad):
        self.color = color
        self.edad = edad

    def nacer(self):
        print("Este animal ha nacido")
    
    def hablar(self):
        print("el animal emite un sonido")

class Pajaro(Animal):
    def __init__(self, color, edad,altura_vuelo):
        super().__init__(color, edad) 
        self.altura_vuelo = altura_vuelo


    def hablar(self):
        print("pio, pio")
    def volar(self,metros):
        print(f"el pajaro vuela {metros} metros")



piolin= Pajaro("amarillo",3,60)  

print(piolin.altura_vuelo)
piolin.nacer()
piolin.hablar()