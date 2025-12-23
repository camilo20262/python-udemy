class Padre:
    def hablar(self):
        print("Hola")

class Madre:
        def hablar(self):
            print("como vas")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

nieto = Nieto()

nieto.hablar()  # Hola

