import pygame
from Configurations import Configurations
from pygame.sprite import Sprite

class Soldier(Sprite):
    """
    Clase que contiene la animación del soldado.
    """

    def __init__(self, screen: pygame.surface.Surface):
        super().__init__()  # Ahora está dentro del constructor


        #Imágen y rectágulo
        soldier_image_path = Configurations.get_soldier_image()
        self.image = pygame.image.load(soldier_image_path)
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()

        # Para centrar el soldado
        screen_rect = screen.get_rect()
        self.rect.centery = screen_rect.centery
        self.rect.right = screen_rect.right

        #Se define la velocidad con la quese movera el soldado
        self._speed=Configurations.get_soldier_speed()
        self._rect_y = float(self.rect.y)

        #Banderas que indicarán si se está moviendo
        self._is_moving_up=False
        self._is_moving_down=False
        self._is_shooting = False


        # Lista que almacena los frames del soldado.
        self._frames = []


        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = Configurations.get_soldiers_sheet_path()
        soldier_sheet = pygame.image.load(sheet_path)


        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_frames_per_column = Configurations.get_shot_frames_per_column()

        sheet_width = soldier_sheet.get_width()
        sheet_height = soldier_sheet.get_height()

        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height // sheet_frames_per_column


        # Se obtiene el tamaño para escalar cada frame.
        soldier_frame_size = Configurations.get_soldier_size()


        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_column):
            for j in range(sheet_frames_per_row):
                x = j * soldier_frame_width
                y = i * soldier_frame_height
                subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
                frame = soldier_sheet.subsurface(subsurface_rect)
                frame = pygame.transform.scale(frame, soldier_frame_size)
                self._frames.append(frame)


        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.


        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 0

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery

        """NUEVO."""
        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()


    def update_animation(self) -> None:
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            self._last_update_time = current_time
            # Si está disparando, usar frames de disparo

            if self._is_shooting:
                self.image = self._frames[self._frame_index]
                self._frame_index += 1

                if self._frame_index >= len(self._frames):
                    self._frame_index = 0
                    self._is_shooting = False  # Fin de disparo

            else:

                self.image = self._frames[self._frame_index]
                self._frame_index += 1

                if self._frame_index >= 4:
                    self._frame_index = 0

    def shoots(self)->None:
        """
        Metodo que indica el disparo.
        """
        self._is_shooting = True
        self._frame_index = 4

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana.
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