import pygame
import os
import maps
import sys



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
            else:
                sys.exit()
            screen.blit(img, (x, y))
            x += 50
        y += 50
