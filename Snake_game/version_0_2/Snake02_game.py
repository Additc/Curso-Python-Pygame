"""
Nombre: Addi Toro Chávez
fecha:
versión: 0.2
-Se agregó la configuración en el módulo de Configurations.py que va a
incluir todas las configuraciones del juego.
-Se agregó el módulo Game_funcionalities.py que contiene los eventos del juego
y los elementos del juego
visuales del juego.
"""


#Se importan lo módulos para el videojuego
import pygame
from Configuration import Configurations
from Game_funtionalities import game_events
from Snake_game.version_0_2.Game_funtionalities import screen_refresh


def run_game()->None:
    """
    Función principal del videojuego
    :return:
    """
    #Se inicializa el módulo de pygame
    pygame.init()

    #Se inicializa la pantalla
    #screen_size=(1280,720)   # Resolución de la pantalla (ancho,alto)
    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #Se configura el título del juego
    #game_title="Snake game"
    pygame.display.set_caption(Configurations.get_game_title())  #Mostrar título

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        #Se verifican los eventos (teclado,ratón) del juego.
        game_over=game_events()

        #Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen)

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()