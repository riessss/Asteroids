import sys
import pygame
from .constants import *
from objects.player import Player
from objects.asteroids import Asteroid
from objects.asteroidfield import AsteroidField
from objects.shot import Shot

def game_loop(screen, font, background_image):
    life_image = pygame.image.load('assets/life.png').convert_alpha()
    life_image = pygame.transform.scale(life_image,(50,50))

    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(x, y, radius=PLAYER_RADIUS)

    dt = 0
    asteroid_field = AsteroidField()

    score = 0
    hits = 0
    lives = 3

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                asteroid.kill()
                lives -= 1
                if lives == 0:
                    state = "menu"
                    game_running = False
                    return state
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot) == True:
                    asteroid.split()
                    shot.kill()
                    hits += 1
                    score += 500

        score += 5

        screen.fill((0,0,0))
        screen.blit(background_image, (0,0))
        screen.blit(font.render(f'Lives:', True, (0,255,0)), (5,10))  
        for i in range(lives):
            screen.blit(life_image, (75 + 25 * i, 0))
        screen.blit(font.render(f'Score: {score}', True, (0,255,0)), (5,35))
        screen.blit(font.render(f'Hits: {hits}', True, (0,255,0)), (5,60))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000