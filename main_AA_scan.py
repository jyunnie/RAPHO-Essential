import pygame
import sys
import os

# Screen settings
WIDTH = 1920
HEIGHT = 1080
FPS = 60
STRIPE_HEIGHT = 100
BG_COLOR = (0, 0, 0)
STRIPE_COLOR = (255, 255, 255)

# Sweep duration (1 second = 30 frames at 30Hz)
FRAMES_PER_SWEEP = 30
STEP_SIZE = (HEIGHT - STRIPE_HEIGHT) / FRAMES_PER_SWEEP  # move per frame

def run_scanline():
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{(3840 - WIDTH) // 2},{(2160 - HEIGHT) // 2}"

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    pygame.display.set_caption("Sharp Scanline Sweep")

    clock = pygame.time.Clock()
    y = 0

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        screen.fill(BG_COLOR)

        # Draw sharp-edged stripe
        pygame.draw.rect(screen, STRIPE_COLOR, (0, int(y), WIDTH, STRIPE_HEIGHT))
        pygame.display.flip()

        # Move stripe down
        y += STEP_SIZE
        if y > HEIGHT:
            y = 0

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_scanline()
