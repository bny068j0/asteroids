import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            log_state()
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
