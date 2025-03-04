import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE

class Asteroid(CircleShape, pygame.sprite.Sprite):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((radius * 2, radius *2), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)

    def update(self, dt):
        position_change = self.velocity * dt
        self.position += position_change
        self.x, self.y = self.position  
        self.rect.center = (self.x, self.y)

        

