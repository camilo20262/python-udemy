

nombre= input("¿Cuál es tu nombre? ")
ventas= input("¿Cuánto vendiste hoy? ")
ventas= int(ventas)
comision = round(ventas * 13/100)

print(f"Ok {nombre} este mes ganaste de comisiones. {comision} ")