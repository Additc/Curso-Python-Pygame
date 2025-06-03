
class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)  # Resolución de la pantalla (ancho,alto)
    _game_title = "Alien game"   #Título del juego
    _background = (50, 50, 50)  # Fondo de la pantalla en formato RGB
    _fps = 40

    _background_image_path="../media/background.png"
    _soldier_image="../media/soldier.png"
    _soldier_speed=10

    _soldier_sheet_path="../media/soldiers.png"
    _frames_per_row=4

    _soldier_size=(142,76)
    _soldier_frame_delay=300
    _shoot="../media/shot-sheet.png"

    _shoot_size=(32,32)

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

    @classmethod
    def get_soldier_speed(cls) -> int:
        """
        Getter para background.
        :return:
        """
        return cls._soldier_speed

    @classmethod
    def get_soldier_sheet_path(cls)->str:
        """
        Getter para _game_title.
        :return:
        """
        return  cls._soldier_sheet_path

    @classmethod
    def get_frames_per_row(cls)->int:
        """
        Getter para frames per now
        """
        return cls._frames_per_row

    @classmethod
    def get_soldier_size(cls)->tuple[int,int]:
        """
        Getter para soldier size.
        :return:
        """
        return  cls._soldier_size

    @classmethod
    def get_soldier_frame_delay(cls)->int:
        """
        Getter para soldier frame size
        :return:
        """
        return cls._soldier_frame_delay

    @classmethod
    def get_shoot(cls)->str:
        """
        Getter para soldier frame size.
        :return:
        """
        return cls._shoot

    @classmethod
    def get_shoot_size(cls)->tuple[int,int]:
        """
        Getter para soldier size.
        :return:
        """
        return  cls._shoot_size