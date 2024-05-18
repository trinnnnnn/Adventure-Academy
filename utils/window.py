import pygame

#screen height and width
width = 1280
height = 720

#creating window, caption, and icon (hwsurface = hardware acceleration and doublebuf = double buffering)
screen = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SHOWN)
caption = pygame.display.set_caption("Adventure Academy")
#icon = pygame.image.load('directory')
#pygame.display.set_icon(icon)