"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
import pygame
from Configurations import Configurations
from media import Background,Audio,Scoreboard
from Soldier import Soldier
from Shoot import  Shot
from random import randint
from Alien import Alien



def game_events(soldier: Soldier, gunshots: pygame.sprite.Group, audio:Audio) -> bool:
    """
    Función que administra los eventos de juego.
    :param soldier: Objeto del soldado que recibe los eventos.
    :param shots: Grupo de disparos activos.
    :return: La bandera del fin del juego.
    """
    game_over = False

    for event in pygame.event.get():
        # Evento de cierre del juego
        if event.type == pygame.QUIT:
            game_over = True

        # Teclas presionadas
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True
            elif event.key == pygame.K_DOWN:
                soldier.is_moving_down = True
            if event.key == pygame.K_SPACE and len(gunshots) <= 2:
                audio.play_shot_sound()
                new_shot = Shot(soldier)
                gunshots.add(new_shot)
                soldier.shoots()

        # Teclas soltadas
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            elif event.key == pygame.K_DOWN:
                soldier.is_moving_down = False
            elif event.key == pygame.K_SPACE:
                soldier.is_shoot = False  # desactiva animación de disparo

    return game_over

def check_collisions(screen: pygame.surface.Surface,
                     soldier:Soldier,
                     shots:pygame.sprite.Group,
                     aliens:pygame.sprite.Group,audio:Audio,scoreboard:Scoreboard) -> bool:

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

    for shot in shots.copy():
        if shot.rect.right <= screen_rect.left:
            shots.remove(shot)

    for alien in aliens.copy():
        if alien.rect.left >= screen_rect.right:
            aliens.remove(alien)

    soldier_aliens_collisions = pygame.sprite.spritecollide(soldier,aliens,False)
    if len(soldier_aliens_collisions)>=1:
        game_over = True

    if len(aliens) <= 5:
        aliens_to_spawn = randint(0, 10)
        for i in range(aliens_to_spawn):
            alien = Alien(screen)
            aliens.add(alien)

    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock:pygame.time.Clock,
                   background:Background, soldier:Soldier, shots:pygame.sprite.Group,aliens:pygame.sprite.Group,scoreboard:Scoreboard)->None:
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
    soldier.update_animation()
    #Se sobrepone la image del soldado
    soldier.blit(screen)

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