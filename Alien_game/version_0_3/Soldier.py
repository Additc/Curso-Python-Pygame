import pygame
from Configurations import Configurations
from pygame.sprite import Sprite

class Soldier(Sprite):
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self, screen):
        super().__init__()  # Ahora está dentro del constructor

        soldier_image_path = Configurations.get_soldier_image()
        self.image = pygame.image.load(soldier_image_path)
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()

        # Para centrar el soldado
        screen_rect = screen.get_rect()
        self.rect.centery = screen_rect.centery
        self.rect.left = screen_rect.left


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibuja.
        """
        screen.blit(self.image, self.rect)