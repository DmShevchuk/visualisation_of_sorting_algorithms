import pygame
import os
from time import sleep
from random import randint, shuffle

os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.init()
SIZE = (602, 650)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Bubble sorting')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(BLACK)

list_for_sorting = list(range(1, 601))

for _ in range(randint(1, 11)):
    shuffle(list_for_sorting)

n = len(list_for_sorting)

running = True
time_delta = 0

while running:
    # Bubble sorting
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list_for_sorting[j] > list_for_sorting[j + 1]:
                list_for_sorting[j], list_for_sorting[j + 1] = list_for_sorting[j + 1], list_for_sorting[j]

        screen.fill(BLACK)

        for k in range(len(list_for_sorting)):
            x, y = k, SIZE[1] - list_for_sorting[k]
            width, height = 2, list_for_sorting[k]
            color = WHITE

            pygame.draw.rect(screen, color, (x, y, width, height))

        pygame.display.flip()
        sleep(time_delta)
