import functions.buttoninstance as bi
import pygame

def DefaultButtons(display):
    if bi.power_button.draw(display):
        pygame.QUIT()