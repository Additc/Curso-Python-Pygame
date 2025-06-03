import pygame
from pygame.sprite import Sprite

from media import Background
from Configurations import Configurations
from Soldier import Soldier
from Shoot import Shot

def game_events(soldier:Soldier,screen: pygame.surface.Surface,shots:pygame.sprite.Group)->bool:
    """
    Función que administra los eventos de juego.
    :return: La bandera del fin del juego.
    """
    game_over=False

    # Se verifican los eventos (teclado, ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: #Indica que se mueve hacia  arriba
                soldier.is_moving_up=True
            if event.key == pygame.K_DOWN: #Indica que se mueve hacia abajo
                soldier.is_moving_down=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:  # Indica que se mueve hacia  arriba
                soldier.is_moving_up = False
            if event.key == pygame.K_DOWN:  # Indica que se mueve hacia abajo
                soldier.is_moving_down = False

            if event.key == pygame.K_SPACE: #Indica el disparo al presionar el espacio
                new_shot=Shot(screen,soldier)
                shots.add(new_shot)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:  # Indica que se mueve hacia  arriba
                shots.is_moving_up = False
            if event.key == pygame.K_DOWN:  # Indica que se mueve hacia abajo
                shots.is_moving_down = False


        if event.type == pygame.QUIT:
            game_over = True

    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,background:Background,
                   clock:pygame.time.Clock, soldier:Soldier,shots:pygame.sprite.Group)->None:
    """
    Función que administra los elementos visuales del juego.
    """
    #Fondo de la pantalla
    background.blit(screen)

    #Se verifican las banderas
    soldier.update_pocision(screen)

    #Se anima el soldado
    soldier.update_animation()

    #Se dibuja al soldado
    soldier.blit(screen)

    #Se deibuja y se anima el soldado
    for shot in shots.sprites():
        shot.update_animation()
        shot.blit(screen)

    #Se actualiza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())