import pygame
from pygame import *

from lib import *
from levels import *


def tutorial_03():
    level = Level("levels/tutorial_levels/tutorial_03.txt", 60, velocity_jump=6)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    return level



