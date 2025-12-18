monedas =5 #cantidad de monedas iniciales

while monedas >0:#mientras tenga monedas
    print(f"tengo {monedas} monedas") #imprimir la cantidad de monedas
    monedas -=1#restar una moneda
else:
    print("Ya no tengo monedas")#imprimir cuando ya no hay monedas


respuesta="s"#respuesta inicial para el bucle

while respuesta =="s":#mientras la respuesta sea "s"
    respuesta = input("Quieres continuar? (s/n): ")#preguntar si quiere continuar
    if respuesta !="s":#si la respuesta no es "s"
        print("Gracias por participar") #imprimir mensaje de agradecimiento

