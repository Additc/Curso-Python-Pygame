import pygame
from media import Background
from Configurations import Configurations
from Soldier import Soldier

def game_events(soldier:Soldier)->bool:
    """
    Función que administra los eventos de juego.
    :return: la bandera del fin del juego.
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

        if event.type == pygame.QUIT:
            game_over = True

    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,background:Background,
                   clock:pygame.time.Clock, soldier:Soldier)->None:
    """
    Función que administra los elementos visuales del juego.
    """
    #Fondo de la pantalla
    background.blit(screen)

    #Se verifican las banderas
    soldier.update_pocision(screen)

    #Se dibuja al soldado
    soldier.blit(screen)

    #Se actualiza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())