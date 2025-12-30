import pygame
#inicializar pygame
pygame.init()

#crear la pantalla

pantalla= pygame.display.set_mode((800,600))


#titulo e icono

pygame.display.set_caption("Invasion espacial")
icono= pygame.image.load("ovni.png")
pygame.display.set_icon(icono)


#loop del juego
se_ejecuta= True

while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    pantalla.fill((219, 251, 251))
    pygame.display.update()
    