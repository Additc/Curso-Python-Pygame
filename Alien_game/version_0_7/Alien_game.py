"""
Nombre del alumno: Addi Toro Chávez
fecha: 13 de mayo del 2025
versión: 0.5
"""

#Se importan los módulos para el videojuego
import pygame
from Configurations import Configurations
from Game_functionalities import game_events,screen_refresh
from media import Background
from Soldier import Soldier
from Shoot import Shot
from Alien import Alien
from random import randint

def run_game()->None:
    """
    Función principal del videojuego.
    """
    #Se inicializa el módulo de pygame
    pygame.init()


    #Se configura el reloj del juego
    clock=pygame.time.Clock()

    #Se inicializa la pantalla
    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #Se crea al soldado
    soldier=Soldier(screen)

    #Se crea un grupo de aliens.
    aliens = pygame.sprite.Group()
    min_aliens = 5
    aliens_to_spawn = min_aliens + randint(0,10)
    for _ in range(aliens_to_spawn):
        alien=Alien(screen)
        aliens.add(alien)


    #Se crea un grupo de disparos
    shots=pygame.sprite.Group()

    background=Background()

    #Se configura el título del juego
    pygame.display.set_caption(Configurations.get_game_title())  #Mostrar título

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:

        # Se verifican los eventos (teclado, ratón) del juego.
        game_over = game_events(soldier,shots)

        #Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen,clock,background,soldier,shots,aliens)

    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()