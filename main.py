import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
   
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroidField = AsteroidField()
    
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid  in asteroids:
            if asteroid.collided(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collided(bullet):
                    for roid in asteroid.split():
                       asteroids.add(roid)
                    bullet.kill()
        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) /1000
        

if __name__ == "__main__":
    main()