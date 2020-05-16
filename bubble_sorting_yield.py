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


def bubble_sorting(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        yield lst


list_ = bubble_sorting(list_for_sorting)

running = True
time_delta = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    try:
        current_list = next(list_)

        for k, value in enumerate(current_list):
            x, y = k, SIZE[1] - value
            width, height = 2, value
            color = WHITE

            pygame.draw.rect(screen, color, (x, y, width, height))

        pygame.display.flip()
        sleep(time_delta)

    except StopIteration:
        pass
