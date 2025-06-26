import pygame
from Configurations import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla.
    Sus atributos son: image (apariencia) y rect (posición y tamaño).
    Sus métodos son: blit() (dibujar).
    """
    def __init__(self):
        # Se carga la imagen del fondo de pantalla.
        image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(image_path)

        # Se escala la imagen al tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el fondo de pantalla en la pantalla.
        :param screen: Pantalla en donde se dibuja el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)

class Audio:
    """
    Clase que contiene el audio del videojuego, incluyendo la música y los efectos de sonido.
    Sus atributos son: la música y los sonidos.
    Sus métodos son: para reproducir y controlar la música, así como los que reproducen los sonidos.
    """

    def __init__(self):
        # Se carga la música del videojuego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se carga el sonido de inicio.
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sound_path())

        # Se carga el sonido cuando el soldado dispara.
        self._shot_sound = pygame.mixer.Sound(Configurations.get_shot_sound_path())

        # Se carga el sonido cuando impacta una bala con un alien.
        self._kill_sound = pygame.mixer.Sound(Configurations.get_kill_sound_path())

        # Se carga el sonido cuando el jugador ha perdido.
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())

    @classmethod
    def play_music(cls, volume) -> None:
        """
        Se utiliza para reproducir la música en bucle.
        """
        pygame.mixer.music.play(loops=-1)  # Un -1 indica que la música se reproduce en bucle.
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Tiempo de desvanecimiento de la música (en ms).
        """
        pygame.mixer.music.fadeout(time)

    def play_star_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido de inicio del juego.
        """
        self._start_sound.play()

    def play_shot_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido de inicio del juego.
        """
        self._shot_sound.play()

    def play_kill_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando la serpiente come la manzana.
        """
        self._kill_sound.play()

    def play_game_over_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando el jugador ha perdido.
        """
        self._game_over_sound.play()

class Scoreboard:
    def __init__(self):
        self._typeface = "Kimono"
        self._font_size = 40
        self._font_color = (171, 250, 10)

        # Se agrega la imagen con el score
        self._font = pygame.font.SysFont(self._typeface, self._font_size)
        self.image = self._font.render("Puntos: 0", True, self._font_color)
        self.rect = self.image.get_rect()

        # Se ajusta la posición del marcador
        self.rect.x = Configurations.get_screen_size()[0] * 0.05
        self.rect.y = Configurations.get_screen_size()[1] * 0.05

    def update(self, new_score: int) -> None:
        text = "Puntos: " + str(new_score)
        self.image = self._font.render(text, True, self._font_color)

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)


#Se crea una nueva clase para la animación de muerte.
class GameOverImage:
    def __init__(self):
        pass

    def play_death_animation(self, screen: pygame.Surface) -> None:
        """
        Se utiliza para mostrar en pantalla la animación de muerte de los
        personajes.
        :param screen: Pantalla del videojuego.
        :return:
        """
        # Se cargan y se almacenan las imágenes de la animación de muerte.
        death_animation = []
        for i in range(1, 9):
            # Se carga cada imagen de la secuencia numerada (muerte_1.png a muerte_8.png).
            frame = pygame.image.load(f"../media/muerte_{i}.png").convert_alpha()

            # Se escala cada imagen al tamaño deseado (1100 x 1400 píxeles).
            frame = pygame.transform.scale(frame, (1100, 1400))

            # Se agrega el frame a la lista de animación.
            death_animation.append(frame)

        # Se obtiene el tamaño de la pantalla para centrar las imágenes.
        screen_width, screen_height = screen.get_size()

        # Se reproduce la animación frame por frame.
        for frame in death_animation:
            # Se limpia la pantalla con un color negro antes de mostrar cada frame.
            screen.fill((0, 0, 0))

            # Se calcula la posición para centrar la imagen en la pantalla.
            death_x = (screen_width - frame.get_width()) // 2
            death_y = (screen_height - frame.get_height()) // 2

            # Se dibuja el frame actual en la posición calculada.
            screen.blit(frame, (death_x, death_y))

            # Se actualiza la pantalla para mostrar el frame.
            pygame.display.flip()

            # Se espera 400 milisegundos antes de mostrar el siguiente frame.
            pygame.time.delay(400)


