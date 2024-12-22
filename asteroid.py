from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()

        if self.radius==ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(rand_angle)
        vel2 = self.velocity.rotate(-rand_angle)

        new_size = self.radius-ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x,self.position.y, new_size)
        child2 = Asteroid(self.position.x,self.position.y, new_size)
        child1.velocity=vel1
        child2.velocity=vel2