turno_perfumeria = 0
turno_farmacia = 0
turno_cosmetica = 0

def perfumeria():
    global turno_perfumeria
    turno_perfumeria += 1
    print(f"Perfumería - su turno es {turno_perfumeria}")

def farmacia():
    global turno_farmacia
    turno_farmacia += 1
    print(f"Farmacia - su turno es {turno_farmacia}")

def cosmetica():
    global turno_cosmetica
    turno_cosmetica += 1
    print(f"Cosmética - su turno es {turno_cosmetica}")


while True:
    area = input(
        "¿Qué área desea ingresar?\n"
        "1. Perfumería\n"
        "2. Farmacia\n"
        "3. Cosmética\n"
        "4. Salir\n"
        "Seleccione una opción: "
    )

    if area == '1':
        perfumeria()
    elif area == '2':
        farmacia()
    elif area == '3':
        cosmetica()
    elif area == '4':
        print("Gracias por su visita")
        break
    else:
        print("Opción no válida, intente de nuevo.")

print("\nTurnos totales del día:")
print(f"Perfumería: {turno_perfumeria}")
print(f"Farmacia: {turno_farmacia}")
print(f"Cosmética: {turno_cosmetica}")
