import os
import pygame
import random
import sys

import utils
import maps


pygame.init()
map = maps.map2
width, height = utils.get_map_size(map)
screen = pygame.display.set_mode((width, height))


class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None


    def move(self):
        if self.direction == 'up':
            self.y -= 50
        elif self.direction == 'down':
            self.y += 50
        elif self.direction == 'left':
            self.x -= 50
        elif self.direction == 'right':
            self.x += 50


    def draw(self):
        pacman_img = pygame.image.load('./media/pacman.png')
        screen.blit(pacman_img, (self.x, self.y))
        pygame.display.update()


pacman = Pacman(int(len(map[0]) / 2 * 50), int(len(map) / 2 * 50))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pacman.direction = 'up'
            elif event.key == pygame.K_d:
                    pacman.direction = 'right'
            elif event.key == pygame.K_s:
                    pacman.direction = 'down'
            elif event.key == pygame.K_a:
                    pacman.direction = 'left'
    utils.draw_map(screen, map)
    pacman.move()
    pacman.draw()
