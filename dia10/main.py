import pygame
import random 
import math 
#inicializar pygame
pygame.init()

#crear la pantalla

pantalla= pygame.display.set_mode((800,600))


#titulo e icono

pygame.display.set_caption("Invasion espacial")
icono= pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo= pygame.image.load("Fondo.jpg")

#jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x= 368
jugador_y = 528
jugador_x_cambio=0

#enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x= random.randint(0,736)
enemigo_y = random.randint(50,200)
enemigo_x_cambio=0.3
enemigo_y_cambio=50


#bala
img_bala = pygame.image.load("bala.png")
bala_x= 0
bala_y = 500
bala_x=0
bala_y_cambio=1
bala_visible = False 

#puntaje
puntaje=0 


#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))


#funcion enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y))

#funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible= True 
    pantalla.blit(img_bala,(x+16,y+10))


# funcion dectetar coliciones 

def hay_colision(x_1,y_1,x_2,y_2):
    distancia=  math.sqrt(math.pow(x_1-x_2, 2) + math.pow ( y_2 - y_1, 2))
    if distancia < 27:
        return True 
    else:
        return False
                 
#loop del juego
se_ejecuta= True

while se_ejecuta:
    #imagen de fondo
    pantalla.blit(fondo,(0,0))
    #evento cerrar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #evento presionar teclas
        if evento.type  ==pygame.KEYDOWN:
            if evento.key ==pygame.K_LEFT:
                jugador_x_cambio -=0.3
            if evento.key ==pygame.K_RIGHT:
                jugador_x_cambio +=0.3  
            if evento.key == pygame.K_SPACE:
                if not bala_visible:

                    bala_x=jugador_x
                    disparar_bala(bala_x,bala_y)

        #evento soltar teclas 
        if evento.type  ==pygame.KEYUP:
            if evento.key ==pygame.K_LEFT or evento.key ==pygame.K_RIGHT:
                jugador_x_cambio =0
        
    #modificar ubicacion    del jugador        
    jugador_x+=jugador_x_cambio

    #mantener dentro de bordes del jugador   
    if jugador_x <=0:
        jugador_x=0
    elif jugador_x >=736:
        jugador_x= 736
    #modificar ubicacion    del enemigo      
    enemigo_x+=enemigo_x_cambio

    #mantener dentro de bordes del enemigo 
    if enemigo_x <=0:
        enemigo_x_cambio=0.3
        enemigo_y+=enemigo_y_cambio
    elif enemigo_x >=736:
        enemigo_x_cambio=-0.3
        enemigo_y+=enemigo_y_cambio

    #movimiento bala
    if bala_y <=-64:
        bala_y=500 
        bala_visible= False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y-= bala_y_cambio

    #colision
    colision=hay_colision(enemigo_x,enemigo_y,bala_x,bala_y)
    if colision:
        bala_y=500 
        bala_visible= False 
        puntaje +=1
        print(puntaje)
        enemigo_x= random.randint(0,736)
        enemigo_y = random.randint(50,200)
        

    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,enemigo_y)
    #actualizar
    pygame.display.update()

    