
class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)  # Resolución de la pantalla (ancho,alto)
    _game_title = "Alien game"   #Título del juego
    _background = (50, 50, 50)  # Fondo de la pantalla en formato RGB
    _fps = 40

    _background_image_path="../media/img.png"
    _soldier_image="../media/soldado.png"


    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
        """
        Getter para screen_size.
        :return:
        """
        return  cls._screen_size

    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title.
        :return:
        """
        return  cls._game_title

    @classmethod
    def get_background(cls)->tuple[int,int,int]:
        """
        Getter para background.
        :return:
        """
        return  cls._background

    @classmethod
    def get_background_image_path(cls)->str:
        """
        Getter para background.
        :return:
        """
        return  cls._background_image_path

    @classmethod
    def get_soldier_image(cls)->str:
        """
        Getter para background.
        :return:
        """
        return  cls._soldier_image


    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para background.
        :return:
        """
        return cls._fps