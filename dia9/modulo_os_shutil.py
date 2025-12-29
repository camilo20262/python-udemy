import os
import shutil

archivo = open('curso.txt','w')
archivo.write('Es un texto de prueba')
archivo.close()

shutil.move('curso.txt', "C:\\Users\\camif\\OneDrive\\Escritorio")