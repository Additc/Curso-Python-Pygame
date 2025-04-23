import pygame
from pygame.sprite import Sprite
from Configuration import Configurations

class Apple(Sprite):
    def __init__(self):
        super().__init__()

        self.image=pygame.Surface(Configurations.get_apple_block_size())
        self.image.fill(Configurations.get_apple_color())

        self.rect=self.image.get_rect()

    def blit(self,screen:pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibuja.
        """
        screen.blit(self.image,self.rect)