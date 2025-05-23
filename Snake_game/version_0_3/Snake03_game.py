"""
Nombre: Addi Toro Chávez
fecha:
versión: 0.3
-Se controla la velocidad de fotogramas
"""


#Se importan lo módulos para el videojuego
import pygame
from Configuration import Configurations
from Game_funtionalities import game_events
from Game_funtionalities import screen_refresh
from Snake import  SnakeBlock


def run_game()->None:
    """
    Función principal del videojuego
    :return:
    """
    #Se inicializa el módulo de pygame
    pygame.init()

    #Se configura el reloj del juego
    clock=pygame.time.Clock()

    #Se inicializa la pantalla
    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #Se configura el título del juego
    pygame.display.set_caption(Configurations.get_game_title())  #Mostrar título

    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head=SnakeBlock(is_head=True)
    snake_head.snake_head_init()

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        #Se verifican los eventos (teclado,ratón) del juego.
        game_over=game_events()

        #Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen, clock,snake_head)

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()