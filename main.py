import pygame 

ancho = 800
largo = 600

pantalla = pygame.display.set_mode((ancho,largo))

perro = pygame.image.load("perro.png")
perro_rect = perro.get_rect()
perro_rect.topleft = (ancho/2,largo/2)

velocidad = 1

run = True
while run:

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_RIGHT] and perro_rect.right<ancho:
        perro_rect.x += velocidad
        print("si funciona")
    elif tecla[pygame.K_LEFT] and  perro_rect.left>0:
        perro_rect.x -= velocidad
        print("si funciona")
    elif tecla[pygame.K_UP] and perro_rect.top>0:
        perro_rect.y -= velocidad
        print("si funciona")
    elif tecla[pygame.K_DOWN] and perro_rect.bottom < largo:
        perro_rect.y += velocidad
        print("si funciona")
                


    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
    
    pantalla.blit(perro,perro_rect)

    pygame.display.update()
