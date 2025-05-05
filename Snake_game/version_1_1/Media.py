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
        self.rect=self.image.get_rect()a..
        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)

class Audio:
    def __init__(self):

        #Se cargan los sonidos del juego
        self._start_sound = pygame.mixer.Sound("../media/start_sound.wav")
        self._eats_apple_sound= pygame.mixer.Sound("../media/eats_apple_sound.wav")
        self._game_over_sound= pygame.mixer.Sound("../media/game_over_sound.wav")

    @classmethod
    def play_music(cls,volumen):
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(volumen)



