class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Soldados vs aliens"              # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    _fps = 30                                       # Número máximo de FPS del videojuego.
    # Tiempo de espera en cierre de juego.
    _time_game_over = 5

    # Configuraciones del soldado.
    _soldier_size = (142, 76)                       # Escala del soldado (ancho, alto).
    _soldier_frames_per_row = 4                     # Número de frames que contiene cada fila de la hoja de frames.
    """NUEVO."""
    _soldier_frames_per_column = 2                  # Número de filas de la hoja de frames.
    _soldier_frame_delay = 300                      # Tiempo de cada frame del personaje (en ms) para la animación del descanso.
    """NUEVO."""
    _soldier_shooting_frame_delay = 34              # Tiempo de cada frame del personaje (en ms) para la animación del disparo.
    _soldier_speed = 12.5                           # Velocidad (en píxeles) del personaje.
    _alien_speed_x = 5                             # Velocidad (en píxeles) del personaje.
    _alien_speed_y = 5                              # Velocidad (en píxeles) del personaje.

    # Configuraciones de los disparos.
    _shot_size = (32, 32)                           # Escala del disparo (ancho, alto).
    _shot_frames_per_row = 4                        # Número de frames que contiene cada fila de la hoja de frames.
    _shot_frame_delay = 100                         # Tiempo de cada frame del disparo (en ms).
    _shot_speed = 32.5                              # Velocidad (en píxeles) del disparo.

    """CAMBIO. Se modificó la imagen que se carga para la hoja de sprites del soldado."""
    # Rutas de las imágenes utilizadas.
    _background_image_path = "../media/background.png"
    _soldier_sheet_path = "../media/soldier-idle_shooting_sheet.png"
    _soldier2_sheet_path = "../media/soldier2.png"
    _shot_sheet_path = "../media/shot-sheet.png"
    _alien_sheet_path = ["../media/alien1.png","../media/alien2.png","../media/alien3.png","../media/alien4.png","../media/alien5.png"]


    # Configuraciones de la música del juego.
    _music_volume = 0.25  # Volumen de la música de fondo (valor entre 0 y 1).
    _music_fadeout_time = _time_game_over * 1000  # Duración del desvanecimiento de la música (en ms).

    # Rutas de los audios utilizados en la clase Audio.
    _music_path = "../media/music_path.mp3"
    _start_sound_path = "../media/music_path.mp3"
    _shot_sound_path = "../media/shot_sound_path.mp3"
    _kill_sound_path = "../media/kill_sound_path.mp3"
    _game_over_sound_path = "../media/grito_sound_game over.mp3"

    """ %%%%%%%     MÉTODOS DE ACCESO.    %%%%%%%%%%%%%%%%%%%%% """
    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title.
        """
        return cls._game_title

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_soldier_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._soldier_size

    @classmethod
    def get_soldier_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._soldier_frames_per_row

    """NUEVO."""
    @classmethod
    def get_soldier_frames_per_column(cls) -> int:
        """
        Getter para _soldier_frames_per_column.
        """
        return cls._soldier_frames_per_column

    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    """NUEVO."""
    @classmethod
    def get_soldier_shooting_frame_delay(cls) -> int:
        """
        Getter para _soldier_shooting_frame_delay.
        """
        return cls._soldier_shooting_frame_delay

    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed

    @classmethod
    def get_alien_speed_x(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._alien_speed_x

    @classmethod
    def get_alien_speed_y(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._alien_speed_y

    @classmethod
    def get_shot_size(cls) -> tuple[int, int]:
        """
        Getter para _shot_size.
        """
        return cls._shot_size

    @classmethod
    def get_shot_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._shot_frames_per_row

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
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    @classmethod
    def get_soldier2_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier2_sheet_path

    @classmethod
    def get_shot_sheet_path(cls) -> str:
        """
        Getter para _shot_sheet_path.
        """
        return cls._shot_sheet_path

    @classmethod
    def get_alien_sheet_path(cls) -> list:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._alien_sheet_path

    # //////////////////////////////////////////////////////////////////////
    @classmethod
    def get_music_volume(cls) -> float:
        """
        Getter para _music_volume.
        """
        return cls._music_volume

    @classmethod
    def get_music_fadeout_time(cls) -> int:
        """
        Getter para _music_fadeout_time.
        """
        return cls._music_fadeout_time

    @classmethod
    def get_music_path(cls) -> str:
        """
        Getter para _music_path.
        """
        return cls._music_path

    @classmethod
    def get_shot_sound_path(cls) -> str:
        """
        Getter para _start_sound_path.
        """
        return cls._shot_sound_path

    @classmethod
    def get_start_sound_path(cls) -> str:
        """
        Getter para _start_sound_path.
        """
        return cls._start_sound_path

    @classmethod
    def get_kill_sound_path(cls) -> str:
        """
        Getter para _eats_apple_sound_path.
        """
        return cls._kill_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _game_over_sound_path.
        """
        return cls._game_over_sound_path