import pygame
from utils.window import width, height
from utils.fps import FPS

# function to create a fade effect on the screen
def fade(screen):
    # create a black surface with the size of the window
    opacity = pygame.Surface((width, height))
    opacity.fill((0, 0, 0))

    clock = pygame.time.Clock()
    alpha = 0

    while alpha < 255:
        opacity.set_alpha(alpha)
        screen.blit(opacity, (0, 0))
        pygame.display.update()
        alpha += 5  # Adjust the increment value to control the fade speed
        clock.tick(FPS)

def fadein(screen, alpha):
    # Create a black surface with the size of the window
    opacity = pygame.Surface((width, height))
    opacity.fill((0, 0, 0))
    opacity.set_alpha(alpha)
    screen.blit(opacity, (0, 0))