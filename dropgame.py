# KYRA CRAWFORD
import pygame
import math
import random, time, os, sys
import datetime

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#COLORS
purp = [114, 40, 189]
screen.fill(purp)
pygame.display.flip()
pygame.time.delay(1000)
class Game:
    coins = []
    def __init__(self, width, height):
        pygame.init()
        self.image = pygame.image.load('droppergame\coin.gif')
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        done = False
        generator = Generator(self)
        pygame.mouse.get_pressed
        click = pygame.mouse.get_pos
class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, screen.width - margin, width):
            for y in range(margin, int(screen.height / 2), width):
                screen.coins.append(Coin(screen, x, y))
