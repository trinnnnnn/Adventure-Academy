import pygame

width = 1280
height = 720

screen = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SHOWN, vsync=1)
caption = pygame.display.set_caption("Adventure Academy")
icon = pygame.image.load("assets/images/util/logo.png").convert_alpha()
pygame.display.set_icon(icon)