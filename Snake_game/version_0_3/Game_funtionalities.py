import pygame
from Configuration import Configurations
from Snake import SnakeBlock

def game_events()->bool:
    """
    Función que administra los evento de juego
    :return: la bandera del fin del juego
    """
    game_over=False

    # Se verifican los eventos (teclado,ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,snake_head:SnakeBlock)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    #Fondo de la pantalla en formato RGB
    screen.fill(Configurations.get_background())

    #Se dibuja la cabeza de la serpiente
    snake_head.blit(screen)

    #Se actuliza la pantalla
    pygame.display.flip()