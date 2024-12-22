from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, player):
        super().__init__(player.position.x, player.position.y,SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1).rotate(player.rotation)*PLAYER_SHOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), self.position, SHOT_RADIUS, 1)

    def update(self, dt):
        self.position += self.velocity*dt