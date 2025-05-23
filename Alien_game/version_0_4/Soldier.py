import pygame
from Configurations import Configurations
from pygame.sprite import Sprite

class Soldier(Sprite):
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self, screen):
        super().__init__()  # Ahora está dentro del constructor

        #Imágen y rectágulo
        soldier_image_path = Configurations.get_soldier_image()
        self.image = pygame.image.load(soldier_image_path)
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()

        # Para centrar el soldado
        screen_rect = screen.get_rect()
        self.rect.centery = screen_rect.centery
        self.rect.left = screen_rect.left

        #Banderas que indicarán si se está moviendo
        self._is_moving_up=False
        self._is_moving_down=False


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibuja.
        """
        screen.blit(self.image, self.rect)

    def update_pocision(self)->None:
        """
        Verifica la pocisión del soldado.
        """
        if (self._is_moving_up):
            self.rect.y-=20

        if (self._is_moving_down):
            self.rect.y+=20

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