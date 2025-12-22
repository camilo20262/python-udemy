import os #importar el módulo os para trabajar con directorios y archivos


ruta = os.chdir('C:\\Users\\camif\\herramientas') #cambiar el directorio actual a la ruta especificada

archivo = open('clarol.txt','r')# abrir el archivo en modo lectura
print(archivo.read()) #leer y mostrar el contenido del archivo
archivo.close() #cerrar el archivo

#ruta2 = os.makedirs('C:\\Users\\camif\\herramientas\\nueva_carpeta') #crear un nuevo directorio en la ruta especificada


os.rmdir('C:\\Users\\camif\\herramientas\\nueva_carpeta') #eliminar el directorio especificado



