
import pygame

class TicTacToeMark(pygame.sprite.Sprite):
    turno = 'X'

    def __init__(self, celda):
        super().__init__()

        # Cargar imagen según el turno
        if TicTacToeMark.turno == 'X':
            self.image = pygame.image.load("../media/x.png")
            TicTacToeMark.turno = 'O'
        else:
            self.image = pygame.image.load("../media/o.png")
            TicTacToeMark.turno = 'X'

        # Redimensionar imagen
        self.image = pygame.transform.scale(self.image, (80, 80))

        # Obtener rectángulo
        self.rect = self.image.get_rect()

        if celda == 1:
            self.rect.x, self.rect.y=(466,292)
        if celda == 2:
            self.rect.x, self.rect.y=(600,287)
        if celda == 3:
            self.rect.x, self.rect.y=(733,284)
        if celda == 4:
            self.rect.x, self.rect.y=(467,410)
        if celda == 5:
            self.rect.x, self.rect.y=(598,410)
        if celda == 6:
            self.rect.x, self.rect.y=(734,410)
        if celda == 7:
            self.rect.x, self.rect.y=(463,533)
        if celda == 8:
            self.rect.x, self.rect.y=(600,533)
        if celda == 9:
            self.rect.x, self.rect.y=(743,533)

