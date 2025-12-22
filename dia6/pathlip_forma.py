from pathlib import Path


carpeta = Path('/Users/camif/herramientas') #definir la ruta de la carpeta
archivo = carpeta / 'clarol.txt' #definir la ruta completa del archivo
mi_archivo = open(archivo) #abrir el archivo en modo lectura
print(mi_archivo.read()) #leer y mostrar el contenido del archivo