from pathlib import Path
import os

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
                print("cual recetas de carnes quisieras leer?: \n -1.Entrecot al Malbec \n -2.Matambre a la Pizza")
                receta = input("Receta: ")
                if receta == "1":
                    carnes1= open('C:\\Users\\camif\\Recetas\\Carnes\\Entrecot al Malbec.txt','r') #abrir el archivo en modo lectura
                    print(carnes1.read()) #leer y mostrar el contenido del archivo
                    break
                elif receta == "2":
                    carnes2= open('C:\\Users\\camif\\Recetas\\Carnes\\Matambre a la Pizza.txt','r') #abrir el archivo en modo lectura
                    print(carnes2.read()) #leer y mostrar el contenido del archivo
                    break
                else:
                    print("\nReceta no valida. Intente de nuevo.")
            while categoria =="ensaladas":
                print("cual recetas de ensaladas quisieras leer?: \n -1.Ensalada Griega \n -2.Ensalada Mediterranea")
                receta = input("Receta: ")
                if receta == "1":
                    ensalada1= open('C:\\Users\\camif\\Recetas\\Ensaladas\\Ensalada Griega.txt','r') #abrir el archivo en modo lectura
                    print(ensalada1.read()) #leer y mostrar el contenido del archivo
                    break
                elif receta == "2":
                    ensalada2= open('C:\\Users\\camif\\Recetas\\Ensaladas\\Ensalada Mediterranea.txt','r') #abrir el archivo en modo lectura
                    print(ensalada2.read()) #leer y mostrar el contenido del archivo
                    break
                else:
                    print("\nReceta no valida. Intente de nuevo.")
            while categoria =="pastas":
                print("cual recetas de pastas quisieras leer?: \n -1.Canelones de Espinaca \n -2.Ravioles de Ricotta")
                pasta = input("Receta: ")
                if pasta == "1":
                    pasta1= open('C:\\Users\\camif\\Recetas\\Pastas\\Canelones de Espinaca.txt','r') #abrir el archivo en modo lectura
                    print(pasta1.read()) #leer y mostrar el contenido del archivo
                    break
                elif pasta == "2":
                    pasta2= open('C:\\Users\\camif\\Recetas\\Pastas\\Ravioles de Ricotta.txt','r') #abrir el archivo en modo lectura
                    print(pasta2.read()) #leer y mostrar el contenido del archivo
                    break
                else:
                    print("\nReceta no valida. Intente de nuevo.")   
            while categoria =="postres":
                print("cual recetas de postres quisieras leer?: \n -1.Compote de manzana \n -2.Tarta de frambuesa")
                postre = input("Receta: ")
                if postre == "1":
                    postre1= open('C:\\Users\\camif\\Recetas\\Postres\\Compota de Manzana.txt','r') #abrir el archivo en modo lectura
                    print(postre1.read()) #leer y mostrar el contenido del archivo
                    break
                elif postre == "2":
                    postre2= open('C:\\Users\\camif\\Recetas\\Postres\\Tarta de Frambuesa.txt','r') #abrir el archivo en modo lectura
                    print(postre2.read()) #leer y mostrar el contenido del archivo
                    break
                else:
                    print("\nReceta no valida. Intente de nuevo.")
        case "2":      
              ruta = os.chdir('C:\\Users\\camif\\Recetas') #cambiar el directorio actual a la ruta especificada
              print("Que categoria desea elegir?\n carnes\n ensaladas\n pastas \n postres")  
              categoria = input("Categoria: ")
              while categoria not in ["carnes", "ensaladas", "pastas", "postres"]:
                  print("Categoria no valida. Intente de nuevo.")
                  categoria = input("Categoria: ")
              while categoria =="ensaladas":
                    ruta = os.chdir('C:\\Users\\camif\\Recetas\\Ensaladas') #cambiar el directorio actual a la ruta especificada
                    titulo=input("Ingrese el titulo de la nueva receta de ensaladas: ")
                    nueva_receta = input("Ingrese el nombre de la nueva receta de ensaladas: ")
                    archivo = open(titulo,'a') #abrir el archivo en modo lectura
                    archivo.write(nueva_receta) #leer y mostrar el contenido del archivo
                    archivo.close() #cerrar el archivo
                    print(f"Receta '{titulo}' agregada a la categoria ensaladas.")
                    break
              while categoria =="pastas":
                    ruta = os.chdir('C:\\Users\\camif\\Recetas\\Pastas') #cambiar el directorio actual a la ruta especificada
                    titulo=input("Ingrese el titulo de la nueva receta de pastas: ")
                    nueva_receta = input("Ingrese el nombre de la nueva receta de pastas: ")
                    archivo = open(titulo,'a') #abrir el archivo en modo lectura
                    archivo.write(nueva_receta) #leer y mostrar el contenido del archivo
                    archivo.close() #cerrar el archivo
                    print(f"Receta '{titulo}' agregada a la categoria pastas.")
                    break
              while categoria =="postres":
                    ruta = os.chdir('C:\\Users\\camif\\Recetas\\Postres') #cambiar el directorio actual a la ruta especificada
                    titulo=input("Ingrese el titulo de la nueva receta de postres: ")
                    nueva_receta = input("Ingrese el nombre de la nueva receta de postres: ")
                    archivo = open(titulo,'a') #abrir el archivo en modo lectura
                    archivo.write(nueva_receta) #leer y mostrar el contenido del archivo
                    archivo.close() #cerrar el archivo
                    print(f"Receta '{titulo}' agregada a la categoria postres.")
                    break
              while categoria =="carnes":
                    ruta = os.chdir('C:\\Users\\camif\\Recetas\\Carnes') #cambiar el directorio actual a la ruta especificada
                    titulo=input("Ingrese el titulo de la nueva receta de carnes: ")
                    nueva_receta = input("Ingrese el nombre de la nueva receta de carnes: ")
                    archivo = open(titulo,'a') #abrir el archivo en modo lectura
                    archivo.write(nueva_receta) #leer y mostrar el contenido del archivo
                    archivo.close() #cerrar el archivo
                    print(f"Receta '{titulo}' agregada a la categoria carnes.")
                    break
                    