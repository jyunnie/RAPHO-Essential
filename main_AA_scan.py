import pygame
import sys

# Settings
WIDTH, HEIGHT = 1920, 1080
FPS = 30
STRIPE_HEIGHT = 10
SPEED = 5
BG_COLOR = (0, 0, 0)
STRIPE_COLOR = (255, 255, 255)

def run_scanline():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    pygame.display.set_caption("Scanline")

    # Move window to center of main screen (3840x2160)
    import os
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{(3840 - WIDTH) // 2},{(2160 - HEIGHT) // 2}"

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

        # Use antialiased alpha stripe (slightly blended top/bottom if desired)
        stripe_surface = pygame.Surface((WIDTH, STRIPE_HEIGHT), pygame.SRCALPHA)
        stripe_surface.fill(STRIPE_COLOR)
        screen.blit(stripe_surface, (0, y))

        pygame.display.flip()

        y += SPEED
        if y > HEIGHT:
            y = 0

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_scanline()
