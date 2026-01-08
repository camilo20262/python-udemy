import cv2
import face_recognition as fr 


# Cargar la imagen con la que se va a comparar
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# -------------------------------
# LOCALIZAR CARAS
# -------------------------------

# Cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# Cara prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# -------------------------------
# DIBUJAR RECTÁNGULOS
# -------------------------------

# Rectángulo cara control
cv2.rectangle(
    foto_control,
    (lugar_cara_A[3], lugar_cara_A[0]),  # esquina superior izquierda
    (lugar_cara_A[1], lugar_cara_A[2]),  # esquina inferior derecha
    (0, 255, 0),
    2
)

# Rectángulo cara prueba
cv2.rectangle(
    foto_prueba,
    (lugar_cara_B[3], lugar_cara_B[0]),
    (lugar_cara_B[1], lugar_cara_B[2]),
    (0, 255, 0),
    2
)

#REALIZAR COMPARACIÓN
resultado= fr.compare_faces([cara_codificada_A], cara_codificada_B)
print('¿Son la misma persona?: ', resultado)


#mostrar las imagenes
cv2.imshow('Foto de control', foto_control)
cv2.imshow('Foto de prueba', foto_prueba)

#medida de distancia 
distancia= fr.face_distance([cara_codificada_A], cara_codificada_B)
print('Distancia entre las caras: ', distancia)


# mantener programa abierto  
cv2.waitKey(0)