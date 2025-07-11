from objects.circleshape import CircleShape
import pygame
from game.constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color=(255,255,255),
            center=self.position, 
            radius=self.radius, 
            width=2)
        
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return self.kill()
        else:
            angle = random.uniform(20, 50)
            velocity = self.velocity.rotate(angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # Positive angle
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity * 1.2

            # Negative angle
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = -velocity * 1.2

            self.kill()
    
                

    def update(self, dt):
        self.position += self.velocity * dt