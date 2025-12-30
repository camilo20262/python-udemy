import pygame
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

def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))


#loop del juego
se_ejecuta= True

while se_ejecuta:
    pantalla.fill((219, 251, 251))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type  ==pygame.KEYDOWN:
            if evento.key ==pygame.K_LEFT:
                jugador_x_cambio -=0.1
            if evento.key ==pygame.K_RIGHT:
                jugador_x_cambio +=0.1   
        if evento.type  ==pygame.KEYUP:
            if evento.key ==pygame.K_LEFT or evento.key ==pygame.K_RIGHT:
                jugador_x_cambio =0
    jugador_x+=jugador_x_cambio

    jugador(jugador_x,jugador_y)
    pygame.display.update()
    