import pygame
import random 
#inicializar pygame
pygame.init()

#crear la pantalla

pantalla= pygame.display.set_mode((800,600))


#titulo e icono

pygame.display.set_caption("Invasion espacial")
icono= pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

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




#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))


#funcion enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y))

#loop del juego
se_ejecuta= True

while se_ejecuta:
    pantalla.fill((219, 251, 251))
    #evento cerrar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #evento presionar flechas 
        if evento.type  ==pygame.KEYDOWN:
            if evento.key ==pygame.K_LEFT:
                jugador_x_cambio -=0.3
            if evento.key ==pygame.K_RIGHT:
                jugador_x_cambio +=0.3  
        #evento soltar flechas 
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

        

    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,enemigo_y)
    #actualizar
    pygame.display.update()

    