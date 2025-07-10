import sys
import pygame
from settings.constants import *
from objects.player import Player
from objects.asteroids import Asteroid
from objects.asteroidfield import AsteroidField
from objects.shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Asteroids')

    font = pygame.font.SysFont('dejavusans', 24)
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))
    stars_image = pygame.image.load('assets/asteroids-game.jpg').convert()
    background_image = pygame.transform.scale_by(stars_image, 0.25)
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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                asteroid.kill()
                lives -= 1
                if lives == 0:
                    print("Game over!")
                    sys.exit()
        
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



if __name__ == "__main__":
    main()
