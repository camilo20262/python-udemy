opcion = int(input("Selecciona una opción (1: Ver perfil, 2: Editar perfil, 3: Cerrar sesión): "))

match opcion:
    case 1:
        print("Seleccionaste: Ver perfil")
    case 2:
        print("Seleccionaste: Editar perfil")
    case 3:
        print("Seleccionaste: Cerrar sesión")
    case _:
        print("Opción no válida")
