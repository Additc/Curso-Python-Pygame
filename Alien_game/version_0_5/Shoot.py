import pygame
from Configurations import Configurations
from pygame.sprite import Sprite


class Shot(Sprite):
    """
    Clase que contiene la animación de disparo
    """
    def __init__(self,screen,soldier):
        super().__init__()


        #Imágen y rectágulo
        shoot_image_path = Configurations.get_shoot()
        self.image = pygame.image.load(shoot_image_path)
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()


        # Para centrar el disparo
        screen_rect = screen.get_rect()
        self.rect.centery = screen_rect.centery
        self.rect.right = screen_rect.right

        #Se define la velocidad con la quese movera el soldado
        self._speed=Configurations.get_soldier_speed()
        self._rect_y = float(self.rect.y)

        #Banderas que indicarán si se está moviendo
        self._is_moving_up=False
        self._is_moving_down=False

        # Lista que almacena los frames del disparo.
        self._frames = []

        """CAMBIO. Ahora se carga la hoja, en lugar de una única imagen."""
        # Se carga la hoja que contiene los frames del disparo.
        sheet_path = Configurations.get_shoot()
        soldier_sheet = pygame.image.load(sheet_path)

        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = soldier_sheet.get_width()
        sheet_height = soldier_sheet.get_height()
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height


        # Se obtiene el tamaño para escalar cada frame.
        soldier_frame_size = Configurations.get_shoot_size()


        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * soldier_frame_width
            y = 0
            subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
            frame = soldier_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, soldier_frame_size)

            self._frames.append(frame)

        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.


        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = soldier.rect
        self.rect.left = screen_rect.left
        self.rect.centery = screen_rect.centery-10


        # Se incluyen los atributos para el movimiento.
        self._rect_x = float(self.rect.x)
        self._speed = Configurations.get_soldier_speed()


    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()
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
        Se utiliza para dibujar el disparo.
        :param screen: Pantalla en donde se dibuja.
        """
        screen.blit(self.image, self.rect)


    def update_pocision(self,screen)->None:
        """
        Verifica la pocisión del soldado.
        """
        if self._is_moving_up:
            self._rect_y-= self._speed

        if self._is_moving_down:
            self._rect_y+= self._speed

        screen_rect=screen.get_rect()


        if self._rect_y < float(screen_rect.top):
            self._rect_y=float(screen_rect.top)

        elif self._rect_y > float(screen_rect.bottom - self.image.get_height()):
            self._rect_y= float(screen_rect.bottom - self.image.get_height())

        self.rect.y = int(self._rect_y)



    @property
    def is_moving_up(self):
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, valor):
        self._is_moving_up = valor

    @property
    def is_moving_down(self):
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self, valor):
        self._is_moving_down = valor