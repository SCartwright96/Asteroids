import pygame
from constants import *
from player import *
from asteroid import *  
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers =(asteroids,updatable,drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    field = AsteroidField()

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while 1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill ((0,0,0))

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()


        for obj in drawable:
            obj.draw(screen)
        
        

        pygame.display.flip()
        dt = game_clock.tick(60)/1000




if __name__ == "__main__":
    main()