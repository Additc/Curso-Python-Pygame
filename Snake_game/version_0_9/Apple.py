import pygame
from pygame.sprite import Sprite
from Configuration import Configurations
from random import randint


class Apple(Sprite):

    #Se crea el atributo de clase para la puntuación
    _no_apples=0

    def __init__(self):
        super().__init__()
        Apple._no_apples+=1

        "Lineas inecesarias"
        #self.image=pygame.Surface((Configurations.get_apple_block_size(),Configurations.get_snake_block_size()))
        #self.image.fill(Configurations.get_apple_color())

        self.image=pygame.image.load(Configurations.get_apple_image_path())
        apple_block_size=Configurations.get_apple_block_size()
        self.image=pygame.transform.scale(self.image,(apple_block_size,apple_block_size))

        self.rect=self.image.get_rect()

    def blit(self,screen:pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibuja.
        """
        screen.blit(self.image,self.rect)

    def random_position(self,sanke_body:pygame.sprite.Group)->None:
        """
        Se utiliza para inicializar una ubicación aleatoria de una manzana y verificar que no se sobreponga sobre el
        cuerpo de la serpiente.
        """
        repeat = True
        while repeat:
            #Se genera la pocisión aleatoria
            screen_width=Configurations.get_screen_size()[0]
            screen_height=Configurations.get_screen_size()[1]
            apple_block_size=Configurations.get_apple_block_size()

            self.rect.x= apple_block_size*randint(0,(screen_width//apple_block_size-1))
            self.rect.y= apple_block_size*randint(0,(screen_height//apple_block_size-1))

            #Se verifica  que no se encuentre sobre el cuerpo de la serpiente.
            for sanke_block in sanke_body.sprites():
                if self.rect ==sanke_block.rect:
                    repeat=True
                    break
                else:
                    repeat=False

    @classmethod
    def get_no_apples(cls)->int:
        """
        Getter de número de manzanas.
        :return:
        """
        return cls._no_apples