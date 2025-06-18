import pygame
from Configurations import Configurations
from media import Background
from Soldier import Soldier
from Shoot import Shot
from Alien import Alien
from random import randint



def game_events(soldier: Soldier, gunshots: pygame.sprite.Group) -> bool:
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
        # Se verifica el evento de presionar una tecla.
        if event.type == pygame.KEYDOWN:
            # Se verifica las flechas para el movimiento.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            # Si se presionó el espacio, entonces se crea un nuevo disparo y se agrega al grupo.
            if event.key == pygame.K_SPACE and len(gunshots)<= 1:
                new_shot = Shot(soldier)
                gunshots.add(new_shot)
                soldier.shoots()

        # Se verifica el evento de soltar una tecla.
        if event.type == pygame.KEYUP:
            # Se verifica las flechas para dejar de moverse.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

    # Se regresa la bandera.
    return game_over


def check_collision(screen: pygame.surface.Surface,
                    soldier:Soldier,gunshots: pygame.sprite.Group,
                    aliens:pygame.sprite.Group)->bool:
    """
    Función que revisa las colisiones del juego:
    *Cabeza de la serpiente con el cuerpo.
    *Cabeza de la serpiente con el borde de la pantalla.
    *Cabeza de la serpiente con la manzana.
    :param screen: Pantalla
    :param snake_body: Cuerpo de la serpiente.
    :param apples: Grupo de las manzanas.
    :return: Las banderas de fin de juego.
    """

    #Se declara la bandera de fin de juego
    game_over=False

    #Se revisa la condición de la cabeza de la serpiente con la pantalla
    screen_rect=screen.get_rect()

    #Se revisan las colisiones con los disparos.
    aliens_gunshots_collisions = pygame.sprite.groupcollide(gunshots,aliens,True,True)

    #Remover los aliens cuando estén fuera de la pantalla
    for alien in aliens.copy():
        if alien.rect.left > screen_rect.right:
            aliens.remove(alien)

    #Remover los disparos cuando estén fuera de la pantalla
    for shot in gunshots.copy():
        if shot.rect.right < screen_rect.left:
            gunshots.remove(shot)

    soldier_alien_collisions = pygame.sprite.spritecollide(soldier,aliens,False)
    if len(soldier_alien_collisions) >=1:
        game_over=True

    if len(aliens) <= 5:
        aliens_to_spawn =  randint(0, 10)
        for _ in range(aliens_to_spawn):
            alien = Alien(screen)
            aliens.add(alien)


    return game_over



def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier,
                   gunshots: pygame.sprite.Group,
                   aliens:pygame.sprite.Group) -> None:
    """
    Función que administra los elementos de la pantalla.
    :param screen: Objeto con la pantalla.
    :param clock: Objeto con el reloj del videojuego.
    :param background: Objeto con el fondo de pantalla.
    :param soldier: Objeto con el soldado (personaje principal).
    :param gunshots: Grupo que almacena los disparos del soldado.
    """
    # Se dibuja el fondo de la pantalla.
    background.blit(screen)

    # Se actualiza la posición del soldado, se anima su sprite y se dibuja en la pantalla.
    soldier.update_pocision(screen)
    soldier.update_animation()
    soldier.blit(screen)


    # Se actualizan las posiciones, se animan y se dibujan los sprites del grupo de los disparos del soldado.
    for shot in gunshots.sprites():
        shot.update_position()
        shot.update_animation()
        shot.blit(screen)

    #Se actualizan las posiciones, se animan y se dibujan los sprites del grupo de aliens
    for alien in aliens.sprites():
        alien.update_position(screen)
        alien.update_animation()
        alien.blit(screen)


    # Se actualiza la pantalla, dando la impresión de movimiento.
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())