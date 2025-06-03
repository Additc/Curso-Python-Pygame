import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((1800, 600))
pygame.display.set_caption("Animación de zorro")

# Cargar hoja de sprites de caminata
walk_sheet = pygame.image.load("../media/zorro.png").convert_alpha()

# Dimensiones originales
original_sprite_width = walk_sheet.get_width() // 3
original_sprite_height = walk_sheet.get_height()
scale_factor = 0.5
sprite_width = int(original_sprite_width * scale_factor)
sprite_height = int(original_sprite_height * scale_factor)

# Preparar animaciones de caminata
walk_frames = [
    pygame.transform.scale(
        walk_sheet.subsurface(pygame.Rect(i * original_sprite_width, 0, original_sprite_width, original_sprite_height)),
        (sprite_width, sprite_height)
    )
    for i in range(3)
]

# Cargar y dividir sprites de apuntado
aim_sheet = pygame.image.load("../media/apuntar.png").convert_alpha()
aim_sprite_width = aim_sheet.get_width() // 3
aim_sprite_height = aim_sheet.get_height()

aim_frames = [
    pygame.transform.scale(
        aim_sheet.subsurface(pygame.Rect(i * aim_sprite_width, 0, aim_sprite_width, aim_sprite_height)),
        (sprite_width, sprite_height)
    )
    for i in range(3)
]

# Posición inicial y variables
x, y = 100, 100
walk_index = 0
aim_index = 0
direction = "right"
clock = pygame.time.Clock()
running = True

# Estado inicial: caminata
current_sprite = walk_frames[walk_index]

while running:
    screen.fill((0, 0, 0))  # Fondo negro

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False
    aiming = keys[pygame.K_SPACE]

    # Movimiento izquierda/derecha
    if keys[pygame.K_RIGHT]:
        x += 20
        direction = "right"
        walk_index = (walk_index + 1) % len(walk_frames)
        current_sprite = walk_frames[walk_index]
        moving = True
    elif keys[pygame.K_LEFT]:
        x -= 20
        direction = "left"
        walk_index = (walk_index + 1) % len(walk_frames)
        current_sprite = walk_frames[walk_index]
        moving = True

    # Si está apuntando, mostrar animación de apuntado
    if aiming:
        aim_index = (aim_index + 1) % len(aim_frames)
        current_sprite = aim_frames[aim_index]

    # Voltear si está mirando a la izquierda
    sprite_to_draw = pygame.transform.flip(current_sprite, True, False) if direction == "left" else current_sprite

    screen.blit(sprite_to_draw, (x, y))
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
sys.exit()

