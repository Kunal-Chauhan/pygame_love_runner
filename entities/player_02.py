import pygame
from pygame import *

from entities import constants
from entities import Entity
from entities import PlatformBlock
from entities import StairsBlock
from entities import BarBlock
from entities import GoalBlock


class Player(Entity):

    color = None

    def __init__(self, x, y, color):
        Entity.__init__(self)
        self.color = color
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.onStairs = False
        self.onBar = False
        self.image = Surface((constants.TILE_X, constants.TILE_Y))
        self.image.fill(Color(self.color))
        self.image.convert()
        self.rect = Rect(x, y, constants.TILE_X-2, constants.TILE_Y)

    def update(self, up, down, left, right, platforms):
        if up:
            if self.onStairs:
                self.yvel = -constants.VELOCITY_MOVEMENT
            else:
                # only jump if on the ground
                if self.onGround:
                    self.yvel -= constants.VELOCITY_JUMP
        if down:
            if self.onStairs or self.onBar:
                self.yvel = constants.VELOCITY_MOVEMENT
        if left:
            self.xvel = -constants.VELOCITY_MOVEMENT
        if right:
            self.xvel = constants.VELOCITY_MOVEMENT
        if not self.onGround and not self.onStairs and not self.onBar:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > constants.VELOCITY_MAX_FALL: self.yvel = constants.VELOCITY_MAX_FALL
        if not(left or right):
            self.xvel = 0
        if not(up or down) and self.onStairs and self.onBar:
            self.yvel = 0

        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, up, down, left, right, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, up, down, left, right, platforms)

    def collide(self, xvel, yvel, up, down, left, right, platforms):
        any_stairs = False
        any_bar = False
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if yvel > 0 and (
                        isinstance(p, PlatformBlock)
                        or isinstance(p, GoalBlock)
                ):
                    self.onGround = True
                if isinstance(p, StairsBlock):
                    any_stairs = True
                if isinstance(p, BarBlock):
                    any_bar = True

                if isinstance(p, GoalBlock):
                    pygame.event.post(pygame.event.Event(QUIT))

                if xvel > 0 and p.collides:
                    self.rect.right = p.rect.left
                    self.xvel = 0
                if xvel < 0 and p.collides:
                    self.rect.left = p.rect.right
                    self.xvel = 0

                if yvel > 0 and p.collides:
                    self.rect.bottom = p.rect.top
                    self.yvel = 0
                if yvel < 0 and p.collides:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
                if yvel > 0 and p.has_grip and not (self.onStairs or self.onBar) and not down:
                    # this is like a collision since we are not moving
                    self.rect.bottom = p.rect.top
                    self.yvel = 0

        if not any_bar and self.onBar and yvel < 0:
            self.yvel = 1

        self.onStairs = any_stairs
        self.onBar = any_bar
