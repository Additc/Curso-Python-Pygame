import pygame
from pygame.sprite import Sprite

class SnakeBlock(Sprite):

    def __init__(self):
        """
        Constructor de clase
        """
        super().__init__() #Llamar al super constructor de Sprite

        color = (255,0,0)

        self.image=pygame.Surface((40,40))
        self.image.fill(color)

        self.rect=self.image.get_rect()

    def blit(self,screen:pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        :param screen:  Pantalla en donde se dibuja
        :return:
        """

        screen.blit(self.image,self.rect)