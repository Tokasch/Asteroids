import pygame
pygame.init()
pygame.font.init()
fps_clock = pygame.time.Clock()
dt = 0
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shoot import Shot


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    all_sprites = pygame.sprite.Group()
    asteroids_group= pygame.sprite.Group()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group ()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score = 0
    score_increment = 100
    high_score = 0

    font = pygame.font.Font('ARIAL.TTF', 48)

    try:
        with open("highscore.txt", "r") as file:
            content = file.read().strip()
            if content:
                high_score = int(content)
            else:
                high_score = 0
    except FileNotFoundError:
        high_score = 0
    

    while True:
        screen.fill((0, 0, 0))
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        highscore_text = font.render(f"Highscore: {high_score}", True, (255, 255, 255))
        text_width, _ = font.size(f"High Score: {high_score}")
        screen.blit(highscore_text, (1280 - text_width - 10, 10))
        for draw_obj in drawable:
            draw_obj.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in list(asteroids):  # Create a copy of the list to safely modify during iteration
            for bullet in list(shots):
                if bullet.collision(asteroid):
                    asteroid.split()  # This should remove from all groups
                    bullet.kill()
                    score += score_increment
                    if score > high_score:
                        high_score = score
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("highscore.txt", "w") as file:
                    file.write(str(high_score))
                sys.exit()

if __name__ == "__main__":
    main()
