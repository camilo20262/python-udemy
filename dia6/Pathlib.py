from pathlib import Path, PureWindowsPath

archivo = Path('C:/Users/camif/pythonudemy/python-udemy/dia6/pruebba.txt') #abrir el archivo en modo lectura

ruta =PureWindowsPath(archivo) #convertir la ruta a formato Windows
print("La ruta del archivo en windows es : ", ruta)

print("-----")
if not archivo.exists():
    print("El archivo no existe en la ruta especificada.")
else:
    print("este es el contenido del archivo: \n", archivo.read_text())