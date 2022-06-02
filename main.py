import os
import pygame
import sys
from random import randint
import random

import utils
import maps


pygame.init()
pacman_map = maps.map2
width, height = utils.get_map_size(pacman_map)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
img_size = 50


def init_enemies():
    enemies = []
    for i in range(4):
        enemy = Enemy()
        enemies.append(enemy)
    return enemies


class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None
        self.move = 0
        self.moveDelay = 15


    def is_allow_move(self, x, y):
        if pacman_map[int(x / img_size)][int(y / img_size)] == 1:
            return 0
        return 1


    def draw(self):
        pacman_img = pygame.image.load('./media/pacman.png')
        screen.blit(pacman_img, (self.x, self.y))
        pygame.display.update()
    
    
    def update(self):
        if self.direction == 'up' and self.is_allow_move(self.x, self.y - img_size):
            self.y -= img_size
        elif self.direction == 'down' and self.is_allow_move(self.x, self.y + img_size):
            self.y += img_size
        elif self.direction == 'left' and self.is_allow_move(self.x - img_size, self.y):
            self.x -= img_size
        elif self.direction == 'right' and self.is_allow_move(self.x + img_size, self.y):
            self.x += img_size
        self.draw()


class Enemy:
    def __init__(self):
        self.x = randint(0, 5) * img_size
        self.y = randint(0, 5) * img_size
        self.direction = random.choice(['left', 'right', 'up', 'down'])


    def update(self):
        pass


    def draw(self):
        enemy_img = pygame.image.load('./media/pacman.png')
        screen.blit(enemy_img, (self.x, self.y))
        # pygame.display.update()


pacman = Pacman(int(len(pacman_map[0]) / 2) * img_size, int(len(pacman_map) / 2) * img_size)
enemies = init_enemies()


while True:
    clock.tick(60)
    pacman.move += 1
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
    for enemy in enemies:
        enemy.draw()
    pygame.display.flip()
    if pacman.move == pacman.moveDelay:
        pacman.move = 0
        utils.draw_map(screen, pacman_map)
        pacman.update()
