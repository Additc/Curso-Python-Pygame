import pygame
from Configuration import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self):
        background_image_path=Configurations._background_image_path
        self.image=pygame.image.load(background_image_path)

        screen_size=Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image,screen_size)

        self.rect=self.image.get_rect()


    def blit(self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla
        self.rect=self.image.get_rect()a.
        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)



class Applee:
    """
    Contiene la imagen de la manzana.
    """

    def __init__(self):
        apple_image="../image/apple1.jpg"
        self.image=pygame.image.load(apple_image)

        apple_new=Configurations.get_apple_block_size()
        self.image = pygame.transform.scale(self.image,apple_new)
        self.rect = self.image.get_rect()

    def blit_apple(self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar la manzana.
        :return:
        """
        screen.blit(self.image, self.rect)