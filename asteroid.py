from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_delta = random.uniform(20, 50)
        random_angle = self.velocity.rotate(angle_delta)
        random_angle_minus = self.velocity.rotate(angle_delta * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_0 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_0.velocity = random_angle * 1.2
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = random_angle_minus * 1.2
