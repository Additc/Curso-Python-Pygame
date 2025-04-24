"""
Nombre: Addi Toro Chávez
fecha: 22 de abril del 2025
versión: 0.8
-Se agregaron los colisiones del juego.
"""


#Se importan lo módulos para el videojuego
import pygame
from Configuration import Configurations
from Game_funtionalities import game_events,screen_refresh,snake_movement,check_collision
from Snake import  SnakeBlock
from pygame.sprite import Group
from Apple import Apple


from Snake_game.version_0_6.Apple import Apple


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

    #Se crea un grupo para almacenar el cuerpo de la serpiente.
    snake_body=Group()
    snake_body.add(snake_head)

    #Se crea el bloque inicial de la manzana
    apple=Apple()
    apple.random_position()

    #Se crea un grupo con las manzana
    apples = Group()
    apples.add(apple)

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        #Se verifican los eventos (teclado,ratón) del juego.
        game_over=game_events(snake_body,apples)

        #Se administra el movimiento de la serpiente
        snake_movement(snake_body)

        #Se revisan las colisiones en el juego
        game_over=check_collision(screen,snake_body,apples)

        #Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen, clock,snake_body,apples)


    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()