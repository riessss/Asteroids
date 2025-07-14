import pygame
from game.constants import *
from game.game import game_loop
from game.menu import menu_loop


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Asteroids')

    level = 2

    font = pygame.font.SysFont('dejavusans', 24)
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))
    state = 'menu'

    clock = pygame.time.Clock()

    stars_image = pygame.image.load('assets/asteroids-game.jpg').convert()
    background_image = pygame.transform.scale_by(stars_image, 0.25)

    while True:
        if state == 'game':
            state, level = game_loop(level, clock, screen, font, background_image)
        if state == 'menu':
            state, level = menu_loop(level, clock, screen, background_image, font)


if __name__ == "__main__":
    main()
