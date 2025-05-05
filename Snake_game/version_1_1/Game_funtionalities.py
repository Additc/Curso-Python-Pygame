import time

import pygame
from Configuration import Configurations
from Snake import SnakeBlock
from Apple import Apple
from Media import Background

def game_events()->bool:
    """
    Función que administra los eventos de juego
    :return: la bandera del fin del juego
    """
    game_over=False

    # Se verifican los eventos (teclado,ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

        #Se verifica que se precione una tecla
        if event.type == pygame.KEYDOWN:
            #Verificar que tecla presiona
            if event.key == pygame.K_RIGHT: #Indica que se mueve hacia la derecha
                SnakeBlock.set_is_moving_right(True)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_LEFT: #Indica que se mueve hacia la izquierda
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(True)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_UP: #Indica que se mueve hacia  arriba
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(True)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_DOWN: #Indica que se mueve hacia abajo
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(True)


    #Se regresa la bandera
    return game_over

def snake_movement(snake_body:pygame.sprite.Group)->None:
    """
    Función que gestona el movimiento del cuerpo de la
    serpiente.
    :param sanke_body: Grupo von el cuerpo de la serpiente.
    """
    body_size=len(snake_body.sprites())-1

    for i in range(body_size,0,-1):
        snake_body.sprites()[i].rect.x=snake_body.sprites()[i-1].rect.x
        snake_body.sprites()[i].rect.y=snake_body.sprites()[i-1].rect.y

    head=snake_body.sprites()[0]

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configurations.get_snake_block_size()

def check_collision(screen: pygame.surface.Surface,
                    snake_body:pygame.sprite.Group,
                    apples:pygame.sprite.Group)->bool:
    """
    Función que revisa las colisiones del juego:
    *Cabeza de la serpiente con el cuerpo.
    *Cabeza de la serpiente con el borde de la pantalla.
    *Cabeza de la serpiente con la manzana.
    :param screen: Pantalla
    :param snake_body: Cuerpo de la serpiente.
    :param apples: Grupo de las manzanas.
    :return: Las banderas de  fin de juego.
    """

    #Se declara la bandera de fin de juego
    game_over=False

    #Se obtiene la cabeza de la serpiente
    head=snake_body.sprites()[0]

    #Se revisa la condición de la cabeza de la serpiente con la pantalla
    screen_rect=screen.get_rect()

    if head.rect.right>screen_rect.right:
        game_over=True
    if head.rect.left<screen_rect.left:
        game_over=True
    if head.rect.top<screen_rect.top:
        game_over=True
    if head.rect.bottom>screen_rect.bottom:
        game_over=True

    #Se revisan la condicion de la cabeza de la serpiente con el cuerpo de la serpiente.
    head_body_collisions=pygame.sprite.spritecollide(head,snake_body, dokill=False)

    if len(head_body_collisions) > 1:
        game_over=True

    #Se revisa la condicion de la cabeza de la serpiente con la manzana.
    head_apples_collisions=pygame.sprite.spritecollide(head,apples, dokill=True)

    if len(head_apples_collisions) > 0:
        new_snake_block=SnakeBlock()
        new_snake_block.rect.x=snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y=snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)

        new_apple=Apple()
        new_apple.random_position(snake_body)
        apples.add(new_apple)

    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock:pygame.time.Clock,
                   snake_body:pygame.sprite.Group,
                   apples:pygame.sprite.Group,
                   background:Background)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    # Se dibuja el fondo de la pantalla en formato RGB
    background.blit(screen)

    #screen.fill(Configurations.get_background())


    #Se dibuja el cuerpo de la serpiente
    for snake_block in reversed (snake_body.sprites()):
        snake_block.blit(screen)

    snake_body.sprites()[0].animate_head()

    #Se anima el movimiento de la manzana
    apples.sprites()[0].animate_apple()

    #Se dibuja la manzana
    apples.draw(screen)


    #Se actuliza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())

def game_over_screen()->None:
    """
    Función con la parte del fin de juego.
    """
    time.sleep(Configurations.get_game_over_screen_time())