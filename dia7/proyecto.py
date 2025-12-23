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



nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ") 
numero_cuenta=input("Ingrese su número de cuenta: ")
balance=float(input("Ingrese su balance inicial: "))
cliente = Cliente(nombre,apellido,numero_cuenta,balance)
while True:
  
    
    print("\n--- Menú de Banco ---")
    print("1. Mostrar información del cliente")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        cliente.mostrar_cliente()
    elif opcion == "2":
        depositar =float(input("Ingrese la cantidad a depositar: "))
        cliente.depositar(depositar)
    elif opcion == "3":
        retirar = float(input("Ingrese la cantidad a retirar: "))
        cliente.retirar(retirar)
    elif opcion == "4":
        print("Gracias por usar el sistema bancario. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")