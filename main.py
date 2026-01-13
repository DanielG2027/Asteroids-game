import pygame
import sys
from constants import SCREEN_HEIGHT,  SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import * 
from asteroidfield import *
from circleshape import * 
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    new_asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game_clock = pygame.time.Clock()
    dt = 0
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
         
        for asteroid in asteroids:
            if asteroid.collision_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collision_with(asteroid):
                    log_event("asteroid_shot")
                    s.kill()
                    asteroid.split()
                    
        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60)/1000
if __name__ == "__main__":
    main()
