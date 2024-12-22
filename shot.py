from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, player):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1)*PLAYER_SHOT_SPEED
        self.rotation = player.rotation

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), self.position, SHOT_RADIUS, 1)

    def update(self, dt):
        self.position += self.velocity*dt