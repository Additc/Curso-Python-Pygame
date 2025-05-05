class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)  # Resolución de la pantalla (ancho,alto)
    _game_title = "Snake game"   #Título del juego
    #_background = (20, 30, 50)  # Fondo de la pantlla en formato RGB
    _fps=8
    _game_over_screen_time=1

    #Configuraciones de la serpiente
    _snake_block_size=80         #Tamaño del bloque de la serpiente
    _snake_head_color=(255,255,255)   #Color de la cabeza de la serpiente
    _snake_body_color=(0,255,0)    #Color del cuerpo de la serpiente

    #Configuraciones de la manzana
    _apple_block_size=_snake_block_size
    #_apple_color=(255,0,0)

    #Las rutas de los archivos multimendia
    _background_image_path = "../media/background_image.jpg"
    _apple_image_path="../media/apple1.png"
    _snake_head_image_path="../media/head1.png"
    _snake_body_image_path= ["../media/body1.png",
                        "../media/body2.png",
                        "../media/body3.png"]

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
    def get_fps(cls) -> int:
        """
        Getter para background.
        :return:
        """
        return cls._fps

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para game_over_screen_time.
        :return:
        """
        return cls._game_over_screen_time

    @classmethod
    def get_snake_block_size(cls)->int:
        """
        Getter para _sanke_block_size.
        :return:
        """
        return  cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls)->tuple[int,int,int]:
        """
        Getter para snake_head_color.
        :return:
        """
        return  cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        """
        Getter para background.
        :return:
        """
        return cls._snake_body_color

    @classmethod
    def get_apple_block_size(cls) ->int:
        """
        Getter para background.
        :return:
        """
        return cls._apple_block_size

    @classmethod
    def get_apple_color(cls) -> tuple[int, int,int]:
        """
        Getter para background.
        :return:
        """
        return cls._apple_color

    @classmethod
    def get_background_image_path(cls)->str:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._background_image_path


    @classmethod
    def get_apple_image_path(cls)->str:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._apple_image_path

    @classmethod
    def get_snake_head_image_path(cls)->str:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._snake_head_image_path

    @classmethod
    def get_snake_body_image_path(cls)->list:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._snake_body_image_path