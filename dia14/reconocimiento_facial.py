from cv2 import cv2
import face_recognition as fr 


# Cargar la imagen con la que se va a comparar
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')