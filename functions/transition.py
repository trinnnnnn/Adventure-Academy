import pygame
from utils.window import width, height
from utils.fps import FPS

def fade(screen):
    opacity = pygame.Surface((width, height))
    opacity.fill((0, 0, 0))

    clock = pygame.time.Clock()
    alpha = 0

    while alpha < 255:
        opacity.set_alpha(alpha)
        screen.blit(opacity, (0, 0))
        pygame.display.update()
        alpha += 5
        clock.tick(FPS)

def fadein(screen, alpha):
    opacity = pygame.Surface((width, height))
    opacity.fill((0, 0, 0))
    opacity.set_alpha(alpha)
    screen.blit(opacity, (0, 0))