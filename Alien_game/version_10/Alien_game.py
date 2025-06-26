"""
Nombre del equipo: Atomos
Nombre del los integrantes: Ryan Gracida Tapia, Addi Toro Chávez
fecha: 24 de junio del 2025
versión: 10 del juego de aliens vs soldados.
En esta versión se implementó el segundo jugador del juego, además de la animación de muerte.
"""
from random import randint
from time import sleep
# Se importan los módulos necesarios.
import pygame
from Configurations import Configurations
from Game_functionalities import game_events, screen_refresh,check_collisions,game_over_screen
from media import Background,Audio,Scoreboard,GameOverImage
from Soldier import Soldier
from Soldier2 import Soldier2
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

    #Se crea el segundo soldado
    soldier2 = Soldier2(screen)

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
        game_over = game_events(soldier, gunshots,audio,soldier2)

        if game_over:
            break

        game_over = check_collisions(screen,soldier,gunshots,aliens,audio,scoreboard,soldier2)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, background, soldier, gunshots,aliens,scoreboard,soldier2)

        if game_over:
            death_anim = GameOverImage()
            game_over_screen(audio)
            death_anim.play_death_animation(screen)
            sleep(4)
    # Cierra todos los recursos del módulo pygame.
    pygame.quit()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()