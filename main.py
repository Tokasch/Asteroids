import pygame
pygame.init()
fps_clock = pygame.time.Clock()
dt = 0
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        screen.fill((0, 0, 0))
        for draw_obj in drawable:
            draw_obj.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000
        updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
