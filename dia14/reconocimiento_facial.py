from cv2 import cv2
import face_recognition as fr 


# Cargar la imagen con la que se va a comparar
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)


#mostrar las imagenes
cv2.imshow('Foto de control', foto_control)
cv2.imshow('Foto de prueba', foto_prueba)

# mantener programa abierto  
cv2.waitKey(0)