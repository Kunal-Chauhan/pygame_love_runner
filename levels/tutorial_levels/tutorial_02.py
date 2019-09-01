import pygame
from pygame import *

from lib import *
from levels import *


def show_image(screen, width, height):
    image_file = "images/thumbs-up/hugo_muy_bien.png"
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    diff = 0.0
    factor = (1.0-diff) * (height / y)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))

    screen.blit(temp, (width - temp.get_rect().size[0], int(round(diff*height))))

    pg_print_message(screen, "MUY BIEN", int(round(0.3 * width / 4)), int(round(3*height / 4)), size=128)

    pygame.display.update()
    pygame.time.wait(5000)


def tutorial_02():
    level = Level("levels/tutorial_levels/tutorial_02.txt", 64, velocity_jump=6)
    level.add_caption(create_caption("Jugador... tienes una cita en la casilla amarilla, y vas tarde...", 176, 120))
    level.success_animation = show_image
    level.offset_width = 10
    return level



