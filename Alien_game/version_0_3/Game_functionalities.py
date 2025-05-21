import pygame
from media import Background
from Configurations import Configurations
from Soldier import Soldier

def game_events()->bool:
    """
    Función que administra los eventos de juego.
    :return: la bandera del fin del juego.
    """
    game_over=False

    # Se verifican los eventos (teclado, ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego
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

    #Se dibuja al soldado
    soldier.blit(screen)

    #Se actualiza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())