import functions.buttoninstance as bi
import pygame, sys

settings = False

def DefaultButtons(display, buttons):
    buttons.append(bi.settings_button)
    global settings
    if bi.settings_button.draw(display):
        if settings is False:
            buttons.append(bi.power_button)
            settings = True
        elif settings is True:
            buttons.remove(bi.power_button)
            settings = False

    if settings:
        if bi.power_button.draw(display):
            sys.exit()
    
    return buttons