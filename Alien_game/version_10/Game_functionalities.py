"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
import pygame
from Configurations import Configurations
from media import Background,Audio,Scoreboard
from Soldier import Soldier
from Soldier2 import Soldier2
from Shoot import  Shot
from random import randint
from Alien import Alien



def game_events(soldier: Soldier, gunshots: pygame.sprite.Group, audio:Audio, soldier2:Soldier2) -> bool:
    """
    Función que administra los eventos del juego.
    :param soldier: Objeto con el soldado (personaje principal).
    :param gunshots: Grupo que almacena los disparos del soldado.
    :return: La bandera de fin del juego.
    """
    # Se declara la bandera de fin del juego que se retorna.
    game_over = False

    # Se verifican los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # El evento es un clic para cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True
# EVENTOS DE LOS JUGADORES --------------------------------------------------------------------------------------
        # Se verifica el evento de presionar una tecla.
        if event.type == pygame.KEYDOWN:
            # Se verifica las flechas para el movimiento del primer jugador
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            # Se verifican las flechas para el movimiento del segundo jugador.
            if event.key == pygame.K_w:
                soldier2.is_moving_up = True

            if event.key == pygame.K_s:
                soldier2.is_moving_down = True

            # Si se presionó el espacio, entonces se crea un nuevo disparo y se agrega al grupo.
            if event.key == pygame.K_f and len(gunshots) <= 2:
                audio.play_shot_sound()
                new_shot2 = Shot(soldier2)
                gunshots.add(new_shot2)
                soldier2.shoots()

            # Si se presionó el espacio, entonces se crea un nuevo disparo y se agrega al grupo.
            if event.key == pygame.K_SPACE and len(gunshots) <= 2:
                audio.play_shot_sound()
                new_shot = Shot(soldier)
                gunshots.add(new_shot)
                soldier.shoots()

        # Se verifica el evento de soltar una tecla.
        if event.type == pygame.KEYUP:
            # Se verifica las flechas para dejar de moverse en el primer jugador
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

            # se verifican las del segundo jugador
            if event.key == pygame.K_w:
                soldier2.is_moving_up = False
            if event.key == pygame.K_s:
                soldier2.is_moving_down = False
    # --------------------------------------------------------------------------------------------------------------

    # Se regresa la bandera.
    return game_over

def check_collisions(screen: pygame.surface.Surface,
                     soldier:Soldier,
                     shots:pygame.sprite.Group,
                     aliens:pygame.sprite.Group,audio:Audio,scoreboard:Scoreboard,
                     soldier2:Soldier2) -> bool:

    # Se declara la bandera de fin de juego
    game_over = False

    # Se revisa .
    screen_rect = screen.get_rect()

    # Se revisarán las coliciones con los disparos.
    aliens_gunshots_collisions = pygame.sprite.groupcollide(shots,aliens,True,True)
    if aliens_gunshots_collisions:
        audio.play_kill_sound()
        soldier.increment_kills()
        scoreboard.update(soldier.get_no_kills())
        soldier2.increment_kills()
        scoreboard.update(soldier2.get_no_kills())

    for shot in shots.copy():
        if shot.rect.right <= screen_rect.left:
            shots.remove(shot)

    for alien in aliens.copy():
        if alien.rect.left >= screen_rect.right:
            aliens.remove(alien)

    soldier_aliens_collisions = pygame.sprite.spritecollide(soldier,aliens,False)
    if len(soldier_aliens_collisions)>=1:
        game_over = True

    soldier_aliens_collisions = pygame.sprite.spritecollide(soldier2,aliens,False)
    if len(soldier_aliens_collisions)>=1:
        game_over = True

    if len(aliens) <= 5:
        aliens_to_spawn = randint(0, 10)
        for i in range(aliens_to_spawn):
            alien = Alien(screen)
            aliens.add(alien)

    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock:pygame.time.Clock,
                   background:Background, soldier:Soldier, shots:pygame.sprite.Group,aliens:pygame.sprite.Group,
                   scoreboard:Scoreboard, soldier2:Soldier2)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    #Fondo de la pantalla
    background.blit(screen)
    # se dibuja el objeto del scoreboard
    scoreboard.blit(screen)
    #Se actualiza la posicion del soldado
    soldier.update_position(screen)
    soldier2.update_position(screen)
    soldier.update_animation()
    soldier2.update_animation()
    #Se sobrepone la image del soldado
    soldier.blit(screen)
    soldier2.blit(screen)

    for shot in shots.sprites():
        shot.update_position()
        shot.update_animation()

    shots.draw(screen)

    for alien in aliens.sprites():
        alien.update_position(screen)
        alien.update_animation()

    aliens.draw(screen)
    #Se actuliza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())



def game_over_screen(audio: Audio) -> None:
    """
    Función con la pantalla del fin del juego.
    :param audio: Objeto con el audio del juego.
    """

    pygame.display.flip()
    """NUEVO."""
    # Se realiza un desvanecimiento de la música y se reproduce el sonido de fin del juego.
    audio.music_fadeout(time = Configurations.get_music_fadeout_time())
    audio.play_game_over_sound()

    # Se agrega una pausa para que el usuario se dé cuenta de que ha perdido.
    #time.sleep(Configurations.)