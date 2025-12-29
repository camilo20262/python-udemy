import os
import shutil
import send2trash

archivo = open('curso.txt','w')
archivo.write('Es un texto de prueba')
archivo.close()

#shutil.move('curso.txt', "C:\\Users\\camif\\OneDrive\\Escritorio")


send2trash.send2trash('curso.txt')