import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)

    asteroids = pygame.sprite.Group()
    updatable.add(asteroids)
    drawable.add(asteroids)

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)

    shots = pygame.sprite.Group()
    updatable.add(shots)
    drawable.add(shots)

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            log_state()
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in updatable:
            sprite.update(0.04)
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")
                        asteroids.update(0.04)
                        asteroids.add(asteroid.split())
                        shot.kill()
            if isinstance(sprite, Asteroid) and sprite.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        dt += clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
