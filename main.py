import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import * 

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    dt = 0
    clock = pygame.time.Clock()


    while True:
        screen.fill("black")
        for shape in drawable:
            if shape is Asteroid:
                color = random.choice(["gray", "purple", "blue", "green", "orange", "yellow"])
                shape.draw(color, screen)
            else:
                shape.draw(screen)

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    break

        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

        clock.tick(60)
        dt = clock.get_time() / 1000  # Convert milliseconds to seconds     

if __name__ == "__main__":
    main()
