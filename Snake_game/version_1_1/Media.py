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
        #Se carga la música del juego
        pygame.mixer.music.load(Configurations.get_music_path())

        #Se cargan los sonidos del juego
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sound())
        self._eats_apple_sound= pygame.mixer.Sound(Configurations.get_eats_apple_sound())
        self._game_over_sound= pygame.mixer.Sound(Configurations.get_game_over_sound())

    @classmethod
    def play_music(cls,volumen):
        """
        Se utiliza para reproducir la música en bloque.
        """
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(volumen)

    @classmethod
    def music_fadeout(cls, time):
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Tiempo de desvanecimiento de la música (en mes).
        """
        pygame.mixer.music.fadeout(time)

    def play_star_sound(self)->None:
        """
        Se utiliza para reproducir el sonido de inicio del juego.
        """
        self._start_sound.play()

    def play_eats_apple_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando la serpiente come una manzana.
        """
        self._eats_apple_sound.play()

    def play_game_over_sound(self)->None:
        """
        Se utiliza para reproducir el sonido cuando el jugador ha perdido.
        """
        self._game_over_sound.play()

