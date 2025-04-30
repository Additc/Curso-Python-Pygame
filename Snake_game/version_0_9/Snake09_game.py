"""
Nombre: Addi Toro Chávez
fecha: 22 de abril del 2025
versión: 0.9
Se agregaron los colisiones del juego.
"""

#Se importan lo módulos para el videojuego
import pygame
from Configuration import Configurations
from Game_funtionalities import game_events,screen_refresh,snake_movement,check_collision, game_over_screen
from Snake import  SnakeBlock
from pygame.sprite import Group
from Apple import Apple
from Media import Background



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
    apple.random_position(snake_body)

    #Se crea un grupo con las manzana
    apples = Group()
    apples.add(apple)

    #Se crea el objeto con el fondo de pantalla
    background=Background()

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        #Se verifican los eventos (teclado,ratón) del juego.
        game_over=game_events()

        #Condición de que cerró la ventana
        if game_over:
            break

        #Se administra el movimiento de la serpiente
        snake_movement(snake_body)

        #Se revisan las colisiones en el juego
        game_over=check_collision(screen,snake_body,apples) 


        #Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen, clock,snake_body,apples,background)


        #Si ah perdido el jugador se llama a la pantalla de fin de juego.
        if game_over:
            game_over_screen()

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()