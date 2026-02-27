import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clk = pygame.time.Clock()
    dt = 0

    updatable = drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clk.tick(60)/1000

if __name__ == "__main__":
    main()
