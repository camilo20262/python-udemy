class Persona: 
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona): 
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def mostrar_cliente(self):
        print(f"Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Balance: {self.balance}")
    
    def depositar(self,cantidad):
        self.balance += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo balance: {self.balance}")

    def retirar(self,retirar_cantidad):
        if retirar_cantidad > self.balance:
            print("fondos insuficientes")
        else:
            self.balance -= retirar_cantidad
            print(f"Retiro de {retirar_cantidad} realizado. Nuevo balance: {self.balance}")