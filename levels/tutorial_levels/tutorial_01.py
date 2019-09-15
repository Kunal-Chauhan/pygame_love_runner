import pygame
from pygame import *

from game_screen.game_screen import GameScreen
from lib import *
from levels import *


def show_image(screen, game_screen: GameScreen, width, height):
    image_file = "images/thumbs-up/julia_y_mar_muy_bien.png"
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    diff = 0.0
    factor = (1.0-diff) * (height / y)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))
    screen.blit(temp, (game_screen.x_offset+int(round(0.20*width)), game_screen.y_offset+int(round(diff*height))))

    pg_print_message(screen, game_screen, "MUY BIEN", int(round(0.3 * 1366 / 4)), int(round(3*768 / 4)), size=128)

    pygame.display.update()
    pygame.time.wait(5000)


def tutorial_01(
        game_screen: GameScreen
):
    level = Level(
        "levels/tutorial_levels/tutorial_01.txt",
        game_screen
    )
    level.add_caption(create_caption("Jugadora... tienes una cita en la casilla amarilla", 176, 120))
    level.add_caption(create_caption("PISTA: Usa las flechas para moverte", 176, 600, color_fg=(150, 150, 150)))
    level.success_animation = show_image
    return level



