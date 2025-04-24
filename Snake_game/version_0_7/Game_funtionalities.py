import pygame
from Configuration import Configurations
from Snake import SnakeBlock
from Apple import Apple

def game_events(snake_body:pygame.sprite.Group,
                apples:pygame.sprite.Group)->bool:
    """
    Función que administra los evento de juego
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

            if event.key == pygame.K_SPACE:
                new_snake_block=SnakeBlock()
                snake_body.add(new_snake_block)

                new_apple=Apple()
                new_apple.random_position(snake_body)
                #print(Apple.get_no_apples())

                #apples.remove(apples.sprites()[0])
                apples.empty()
                apples.add(new_apple)

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




def screen_refresh(screen: pygame.surface.Surface,
                   clock:pygame.time.Clock,
                   snake_body:pygame.sprite.Group,
                   apples:pygame.sprite.Group)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    #Fondo de la pantalla en formato RGB
    screen.fill(Configurations.get_background())


    #Se dibuja el cuerpo de la serpiente
    for snake_block in reversed (snake_body.sprites()):
        snake_block.blit(screen)

    #Se dibuja la manzana
    apples.draw(screen)


    #Se actuliza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())