"""
Nombre: Addi Toro Chávez
fecha:
versión: 0.1
-se crea la pantalla de inicio
-Se configura el título de la pantalla
"""


#Se importan lo módulos para el videojuego
import pygame




def run_game()->None:
    """
    Función principal del videojuego
    :return:
    """
    #Se inicializa el módulo de pygame
    pygame.init()

    #Se inicializa la pantalla
    screen_size=(1280,720)   # Resolución de la pantalla (ancho,alto)
    screen=pygame.display.set_mode(screen_size)

    #Se configura el título del juego
    game_title="Snake game"
    pygame.display.set_caption(game_title)  #Mostrar título

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        #Se verifican los eventos (teclado,ratón) del juego.
        for event in pygame.event.get():
            #Un clic en cerrar el juego
            if event.type == pygame.QUIT:
                game_over=True

        #Se dibujan los elementos gráficos en la pantalla
        background=(20,30,50)  #Fondo de la pantlla en formato RGB
        screen.fill(background)

        #Se actualiza la pantalla
        pygame.display.flip()
    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()