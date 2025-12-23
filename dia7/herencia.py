class Animal:
    def __init__(self,color,edad):
        self.color = color
        self.edad = edad

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass 

piolin= Pajaro("amarillo",3)
piolin.nacer()
print("este animal es de color "+piolin.color)
print("este animal tiene "+str(piolin.edad)+" años")