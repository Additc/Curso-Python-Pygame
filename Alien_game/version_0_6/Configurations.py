
class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)  # Resolución de la pantalla (ancho,alto)
    _game_title = "Alien game"   #Título del juego
    _background = (50, 50, 50)  # Fondo de la pantalla en formato RGB
    _fps = 60

    _background_image_path="../media/background.png"
    _soldier_image="../media/soldier.png"
    _soldier_speed=10

    _soldier_sheet_path = "../media/soldiers.png"
    _soldiers_sheet_path = "../media/soldier-idle_shooting_sheet.png"
    _frames_per_row = 4
    _frames_per_column = 2

    _soldier_size=(142,76)
    _soldier_frame_delay=100
    _shot_sheet_path="../media/shot-sheet.png"

    _shot_size = (32,32)
    _shot_frames_per_row = 4
    _shot_frames_per_column = 2
    _shot_frame_delay = 100
    _shot_speed = 32.5

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
    def get_soldiers_sheet_path(cls)->str:
        """
        Getter para _game_title.
        :return:
        """
        return  cls._soldiers_sheet_path

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
    def get_shot_size(cls)->tuple[int,int]:
        """
        Getter para soldier size.
        :return:
        """
        return  cls._shot_size


    @classmethod
    def get_shot_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._shot_frames_per_row

    @classmethod
    def get_shot_frames_per_column(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._shot_frames_per_column


    @classmethod
    def get_shot_frame_delay(cls) -> int:
        """
        Getter para _shot_frame_delay.
        """
        return cls._shot_frame_delay


    @classmethod
    def get_shot_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._shot_speed


    @classmethod
    def get_shot_sheet_path(cls) -> str:
        """
        Getter para _shot_sheet_path.
        """
        return cls._shot_sheet_path