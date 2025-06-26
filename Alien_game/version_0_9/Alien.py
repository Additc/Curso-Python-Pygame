from random import random, choice, uniform, randint
from pygame.sprite import Sprite
from Configurations import Configurations
import pygame


class Alien(Sprite):
    """
    Clase que contiene al soldado.
    """

    def __init__(self,screen: pygame.surface.Surface):
        super().__init__()
        "Banderas de movimiento"
        movement_alien = [True,False]
        self._is_moving_up = choice(movement_alien)
        self._is_moving_down = not self._is_moving_up
        """NUEVO."""
        # Lista que almacena los frames del soldado.
        self._frames = []

        """CAMBIO. Ahora se carga la hoja, en lugar de una única imagen."""
        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = choice(Configurations.get_alien_sheet_path())
        alien_sheet = pygame.image.load(sheet_path)

        """NUEVO."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_soldier_frames_per_row()
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
        self.rect.y =  alien_frame_size[1] * randint(0, (screen.get_height() // alien_frame_height - 1))
        self.rect.x -= alien_frame_size[0]

        """NUEVO."""
        # Se incluyen los atributos para el movimiento.
        self._rect_x = float(self.rect.x)
        self._speed_x = Configurations.get_alien_speed_x()*uniform(.8,1.2)

        """NUEVO."""
        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.y)
        self._speed_y = Configurations.get_alien_speed_y()*uniform(.6,1.9)

    """NUEVO."""

    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
        :param screen: Pantalla en donde se verifican los límites.
        """
        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect = screen.get_rect()

        # Se actualiza la posición del valor flotante de la posición en x.
        self._rect_x += self._speed_x

        # Se actualiza la posición del rectángulo de acuerdo a la posición en x.
        self.rect.x = int(self._rect_x)

        # Se verifican los estados de la bandera para modificar la posición.
        if self._is_moving_up:
            self._rect_y -= self._speed_y

        elif self._is_moving_down:
            self._rect_y += self._speed_y

        # Se verifica que el personaje no sobrepase los bordes de la pantalla.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.x)
            self._is_moving_up = False
            self._is_moving_down = True

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())
            self._is_moving_up = True
            self._is_moving_down = False

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)

    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_shot_frame_delay()
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
        Se utiliza para dibujar el soldado en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)