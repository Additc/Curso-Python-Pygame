"""
Nombre del equipo: Atomos
Nombre del los integrantes: Ryan Gracida Tapia, Addi Toro Chávez
fecha: 24 de junio del 2025
versión: 9 del juego de aliens vs soldados.
En esta versión se implementaron los sonidos dej juego, además de un contador de
puntos siendo este el número de kills.
"""

from random import randint
from time import sleep
# Se importan los módulos necesarios.
import pygame
from Configurations import Configurations
from Game_functionalities import game_events, screen_refresh,check_collisions
from media import Background,Audio,Scoreboard
from Soldier import Soldier
from pygame.sprite import Group
from Alien import Alien

def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen_size = Configurations.get_screen_size()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()  # Se usa para controlar la velocidad de fotogramas (FPS).

    # Se configura el título de la ventana.
    game_title = Configurations.get_game_title()
    pygame.display.set_caption(game_title)

    # Se crea el objeto del fondo de pantalla.
    background = Background()

    # Se crea el objeto del soldado (personaje principal).
    soldier = Soldier(screen)

    # Se crea el grupo para almacenar los disparos del soldado.
    gunshots = Group()

    # Se crea el grupo para almacenar los disparos del soldado.
    aliens = Group()
    min_aliens = 5
    aliens_to_spawn = min_aliens + randint(0,10)
    for i in range(aliens_to_spawn):
        alien = Alien(screen)
        aliens.add(alien)

    # Se crea el objeto con el sonido del juego y se reproduce la música y el sonido inicial del juego.
    audio = Audio()
    audio.play_music(volume=Configurations.get_music_volume())
    audio.play_star_sound()

    # Se crea el objeto del marcador
    scoreboard = Scoreboard()

    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:

        # Función que administra los eventos del juego.
        game_over = game_events(soldier, gunshots,audio)

        if game_over:
            break

        game_over = check_collisions(screen,soldier,gunshots,aliens,audio,scoreboard)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, background, soldier, gunshots,aliens,scoreboard)

        if game_over:
            # ejemplo del audio de juego perdido
            audio.play_game_over_sound()
            sleep(3)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()