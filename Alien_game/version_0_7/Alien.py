from random import  choice, uniform
import pygame
from Configurations import Configurations
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self, screen):
        super().__init__()  # Ahora está dentro del constructor

        #Banderas que indicarán si se está moviendo
        movement = [True, False]
        self._is_moving_up= choice(movement)
        self._is_moving_down= not self._is_moving_up

        # Lista que almacena los frames del alien.
        self._frames = []


        """CAMBIO. Ahora se carga la hoja, en lugar de una única imagen."""
        # Se carga la hoja que contiene los frames de lod aliens.
        sheet_path = random.choice(Configurations._aliens_random)
        alien_sheet = pygame.image.load(sheet_path)


        """NUEVO."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = alien_sheet.get_width()
        sheet_height = alien_sheet.get_height()
        alien_frame_width = sheet_width // sheet_frames_per_row
        alien_frame_height = sheet_height

        """NUEVO."""
        # Se obtiene el tamaño para escalar cada frame.
        alien_frame_size = Configurations.get_soldier_size()

        """NUEVO."""
        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * alien_frame_width
            y = 0
            subsurface_rect = (x, y, alien_frame_width, alien_frame_height)
            frame = alien_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, alien_frame_size)

            self._frames.append(frame)

        """NUEVO."""
        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.

        """NUEVO."""
        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.left = screen_rect.left
        self.rect.centery = screen_rect.centery

        # Se incluyen los atributos para el movimiento.
        self._rect_x = float(self.rect.x)
        self._rect_y = float(self.rect.y)
        self._speed_x = Configurations.get_alien_speed_x()*uniform(.8,1.2)
        self._speed_y = Configurations.get_alien_speed_y()*uniform(.6,1.4)


    def update_position(self,screen) -> None:
        """
        Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
        """
        # Se actualiza la posición del valor flotante de la posición.
        self._rect_x += self._speed_x

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.x = int(self._rect_x)

        if self._is_moving_up:
            self._rect_y -= self._speed_y

        if self._is_moving_down:
            self._rect_y += self._speed_y

        screen_rect = screen.get_rect()

        # verifica que no se sobrepase de la pantalla
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.top)
            self._is_moving_down = True
            self._is_moving_up = False

        elif self._rect_y > float(screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())
            self._is_moving_down = False
            self._is_moving_up = True


        #se actualiza la pocisión del rectángulo
        self.rect.y = int(self._rect_y)



    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_alien_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames):
                self._frame_index = 0


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana.
        :param screen: Pantalla en donde se dibuja.
        """
        screen.blit(self.image, self.rect)

