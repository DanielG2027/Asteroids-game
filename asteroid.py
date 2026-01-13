from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        asteroid_one_velocity = self.velocity.rotate(angle)
        asteroid_two_velocity = self.velocity.rotate(-angle)
        asteroid_one_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_two_radius = asteroid_one_radius
        
        asteroid_one = Asteroid(self.position.x, self.position.y, asteroid_one_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, asteroid_two_radius)
        
        asteroid_one.velocity = asteroid_one_velocity * 1.2
        asteroid_two.velocity = asteroid_two_velocity * 1.2