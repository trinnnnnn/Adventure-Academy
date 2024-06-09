import functions.buttoninstance as bi
import pygame, sys
from utils.window import *

fscreen = False

settings = False

def DefaultButtons(display, buttons):
    global settings, fscreen
    buttons.append(bi.settings_button)

    if bi.settings_button.draw(display):
        if not settings:
            settings = True
            
        elif settings:
            settings = False

    if settings:
        if bi.power_button not in buttons:
            buttons.append(bi.power_button)
        if bi.fs_button not in buttons:
            buttons.append(bi.fs_button)
        if not fscreen:
            if bi.fs_button.draw(display):
                currentRez = (pygame.display.Info().current_w, pygame.display.Info().current_h)
                pygame.display.set_mode(currentRez, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
                pygame.display.toggle_fullscreen()
                fscreen = True
        if fscreen:
            if bi.min_button.draw(display):
                pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SHOWN)
                fscreen = False
        if bi.power_button.draw(display):
            sys.exit()
    if not settings:
        if bi.power_button in buttons:
            buttons.remove(bi.power_button)
        if bi.fs_button in buttons:
            buttons.remove(bi.fs_button)

    return buttons