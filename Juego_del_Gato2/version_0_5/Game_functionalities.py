import pygame
from Configurations import Configurations
from media import Background, TurnImage
from TikTacToe import TicTacToeMark

def game_events(marks_group,turn_image)->bool:
    """
    Función que administra los eventos de juego.
    :return: la bandera del fin del juego.
    """
    game_over=False

    # Se verifican los eventos (teclado, ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            key_map = {
                pygame.K_q: 1,
                pygame.K_w: 2,
                pygame.K_e: 3,
                pygame.K_a: 4,
                pygame.K_s: 5,
                pygame.K_d: 6,
                pygame.K_z: 7,
                pygame.K_x: 8,
                pygame.K_c: 9,
            }
            if event.key in key_map:
                celda = key_map[event.key]

                # Obtener celdas ya ocupadas
                celdas_ocupadas = [mark.get_cell_number() for mark in marks_group]

                if celda not in celdas_ocupadas:
                    nueva_marca = TicTacToeMark(celda)
                    marks_group.add(nueva_marca)
                    turno = TicTacToeMark.turno
                    turn_image.change_turn(turno)

    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock:pygame.time.Clock,
                   background:Background,marks_group,turn_image:TurnImage)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    #Fondo de la pantalla
    background.blit(screen)

    # Se dibuja el turno
    turn_image.blit(screen)

    #Se dibujan las marcas
    marks_group.draw(screen)


    #Se actuliza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())