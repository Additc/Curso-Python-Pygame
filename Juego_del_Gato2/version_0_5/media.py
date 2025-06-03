import pygame
from Configurations import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self):
        background_image_path=Configurations.get_background_image_path()
        self.image=pygame.image.load(background_image_path)

        screen_size=Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image,screen_size)

        self.rect=self.image.get_rect()


    def blit(self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)




class TurnImage:

    def __init__(self):
        # Cargar imágenes del turno X y O
        self.image_x = pygame.image.load("../media/turnX.png")
        self.image_o = pygame.image.load("../media/turnO.png")

        # Imagen inicial del turno
        self.image = self.image_x

        # Escalar la imagen a un tamaño adecuado
        self.image = pygame.transform.scale(self.image, (1000, 200))  # Puedes ajustar este tamaño

        # Establecer posición inicial centrada
        self.rect = self.image.get_rect()
        self.rect.center = (1280 // 2, 720 // 4)  # Centrado en pantalla

    def blit(self, screen: pygame.surface.Surface):
        """
        Dibuja la imagen del turno en pantalla.
        """
        screen.blit(self.image, self.rect)

    def change_turn(self, turno: str):
        """
        Cambia la imagen del turno.
        :param turno: 'X' o 'O'
        """
        if turno == 'X':
            self.image = self.image_x
        else:
            self.image = self.image_o

        # Redimensionar la imagen y recentrarla
        self.image = pygame.transform.scale(self.image, (1000, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (1280 // 2, 720 // 4)



