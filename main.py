import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    clock = pygame.time.Clock()

    while True:
        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

        clock.tick(60)
        dt = clock.get_time() / 1000  # Convert milliseconds to seconds     

if __name__ == "__main__":
    main()
