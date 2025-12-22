from pathlib import Path

nombre = input("Dime tu nombre: ")
print(f"Bienvenido/a {nombre}")

ruta = Path("C:/Users/camif/Recetas")

print(f"Las recetas están en la siguiente ruta:\n{ruta}")

def contar_carpetas(carpeta):
    return sum(1 for item in carpeta.iterdir() if item.is_dir())

print("Cantidad de recetas:", contar_carpetas(ruta))

def abrir_leer(ruta): #función para abrir y leer un archivo
    archivo = open(ruta, 'r') #abrir el archivo en modo lectura
    contenido = archivo.read() #leer el contenido del archivo 
    archivo.close()#cerrar el archivo 
    return contenido#retornar el contenido leído

def mostrar_menu():
    print("\n Bienvenidos al menu ")
    print("1. leer receta")
    print("2. crear receta ")
    print("3. crear categoria ")
    print("4. eliminar receta ")
    print("5. eliminar categoria ")
    print("6. Finalizar programa ")

while True:
    mostrar_menu()
    opcion= input("Selecccione una opcion:")
    match opcion:
        case "1":
            print("Que categoria desea leer?\n carnes\n ensaladas\n pastas \n postres")
            categoria = input("Categoria: ")
            while categoria not in ["carnes", "ensaladas", "pastas", "postres"]:
                print("Categoria no valida. Intente de nuevo.")
                categoria = input("Categoria: ")
            while categoria =="carnes":
                print("cual recetas de carnes quisieras leer?: \n - Entrecot al Malbec \n - Matambre a la Pizza")
                receta = input("Receta: ")
                if receta == "Entrecot al Malbec":
                    carnes1= open('C:\\Users\\camif\\Recetas\\Carnes\\Entrecot al Malbec.txt','r') #abrir el archivo en modo lectura
                    print(carnes1.read()) #leer y mostrar el contenido del archivo
                elif receta == "Matambre a la Pizza":
                    carnes2= open('C:\\Users\\camif\\Recetas\\Carnes\\Matambre a la Pizza.txt','r') #abrir el archivo en modo lectura
                    print(carnes2.read()) #leer y mostrar el contenido del archivo