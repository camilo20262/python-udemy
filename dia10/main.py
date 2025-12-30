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

def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))


#loop del juego
se_ejecuta= True

while se_ejecuta:
    pantalla.fill((219, 251, 251))
    jugador_x +=0.1
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    jugador(jugador_x,jugador_y)
    pygame.display.update()
    