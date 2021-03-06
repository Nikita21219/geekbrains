import os
import pygame
import sys
from random import randint
import random

import maps


def get_map_size(map):
    columns_count = len(map[0])
    for line in map:
        if len(line) != columns_count:
            return None
    return columns_count * 50, len(map) * 50


def draw_map(screen, map):
    y = 0
    for row in map:
        x = 0
        for col in row:
            if col == 0:
                img = pygame.image.load('./media/floor.png')
            elif col == 1:
                img = pygame.image.load('./media/border.png')
            screen.blit(img, (x, y))
            x += 50
        y += 50


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
        self.is_moving = 1
        self.move_delay = 15
        self.open_mouth = 1
        self.mouth = 0
        self.mouth_delay = 15
        self.enemies_count = 0


    def is_allow_move(self, x, y):
        if pacman_map[int(x / img_size)][int(y / img_size)] == 1:
            return 0
        return 1


    def draw(self):
        if self.open_mouth > 0 and self.is_moving == 1:
            pacman_img = pygame.image.load('./media/pacman2.png')
        else:
            pacman_img = pygame.image.load('./media/pacman.png')
        screen.blit(pacman_img, (self.x, self.y))


    def update(self):
        self.is_moving = 1
        if self.direction == 'up' and self.is_allow_move(self.x, self.y - img_size):
            self.y -= img_size
        elif self.direction == 'down' and self.is_allow_move(self.x, self.y + img_size):
            self.y += img_size
        elif self.direction == 'left' and self.is_allow_move(self.x - img_size, self.y):
            self.x -= img_size
        elif self.direction == 'right' and self.is_allow_move(self.x + img_size, self.y):
            self.x += img_size
        else:
            self.is_moving = 0


class Enemy:
    def __init__(self):
        self.x, self.y = self.generate_coord()
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.move = 0
        self.move_delay = 15
        self.change_direction = 0


    def draw(self):
        enemy_img = pygame.image.load('./media/enemy.png')
        screen.blit(enemy_img, (self.x, self.y))


    def is_allow_move(self, x, y):
        if pacman_map[int(x / img_size)][int(y / img_size)] == 1:
            return 0
        return 1


    def update(self):
        i = 0
        if self.direction == 'up' and self.is_allow_move(self.x, self.y - img_size):
            self.y -= img_size
        elif self.direction == 'down' and self.is_allow_move(self.x, self.y + img_size):
            self.y += img_size
        elif self.direction == 'left' and self.is_allow_move(self.x - img_size, self.y):
            self.x -= img_size
        elif self.direction == 'right' and self.is_allow_move(self.x + img_size, self.y):
            self.x += img_size
        if self.change_direction:
            self.change_direction = 0
            self.direction = random.choice(['left', 'right', 'up', 'down'])
        i += 1


    def generate_coord(self):
        while True:
            x = randint(0, 5)
            y = randint(0, 5)
            if pacman_map[x][y] == 0:
                return x * img_size, y * img_size


pygame.init()
pacman_map = maps.map_list
width, height = get_map_size(pacman_map)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
img_size = 50
pacman = Pacman(int(len(pacman_map[0]) / 2) * img_size, int(len(pacman_map) / 2) * img_size)
enemies = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.direction = 'up'
            elif event.key == pygame.K_RIGHT:
                pacman.direction = 'right'
            elif event.key == pygame.K_DOWN:
                pacman.direction = 'down'
            elif event.key == pygame.K_LEFT:
                pacman.direction = 'left'
    clock.tick(60)
    pacman.move += 1
    pacman.mouth += 1
    if len(enemies) == 0:
        enemies = init_enemies()
    draw_map(screen, pacman_map)
    for enemy in enemies:
        if pacman.x == enemy.x and pacman.y == enemy.y:
            enemies.remove(enemy)
            continue
        enemy.move += 1
        if pygame.time.get_ticks() % 5000 <= 50:
            enemy.change_direction = 1
        if enemy.move == enemy.move_delay:
            enemy.move = 0
            enemy.update()
    if pacman.mouth == pacman.mouth_delay:
        pacman.mouth = 0
        pacman.open_mouth *= -1
    if pacman.move == pacman.move_delay:
        pacman.move = 0
        pacman.update()
    pacman.draw()
    for enemy in enemies:
        enemy.draw()
    pygame.display.update()
