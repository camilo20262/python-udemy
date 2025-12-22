import os #importar el módulo os para trabajar con directorios y archivos


ruta = os.chdir('C:\\Users\\camif\\herramientas') #cambiar el directorio actual a la ruta especificada

archivo = open('clarol.txt','r')# abrir el archivo en modo lectura
print(archivo.read()) #leer y mostrar el contenido del archivo
archivo.close() #cerrar el archivo