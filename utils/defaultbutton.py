import functions.buttoninstance as bi
import pygame, sys
from utils.window import *

fscreen = False

settings = False

autosave = False

autosave_disable_click_time = None

autosave_enable_click_time = None

autosave_delay = 200

def DefaultButtons(display, buttons, ascheck=True):
    global settings, fscreen, autosave, autosave_disable_click_time, autosave_enable_click_time
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
        if ascheck:
            if bi.ason_button not in buttons:
                buttons.append(bi.ason_button)
        if not fscreen:
            if bi.min_button.draw(display):
                pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
                pygame.display.toggle_fullscreen()
                fscreen = True
        if fscreen:
            if bi.fs_button.draw(display):
                pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SHOWN, vsync=1)
                fscreen = False
        if bi.power_button.draw(display):
            sys.exit()
        if ascheck:
            current_time = pygame.time.get_ticks()
            if not autosave:
                if bi.asoff_button.draw(display):
                    autosave_enable_click_time = current_time
            else:
                if bi.ason_button.draw(display):
                    autosave_disable_click_time = current_time
            if autosave_enable_click_time:
                if current_time - autosave_enable_click_time >= autosave_delay:
                    autosave = True
                    autosave_enable_click_time = None
            if autosave_disable_click_time:
                if current_time - autosave_disable_click_time >= autosave_delay:
                    autosave = False
                    autosave_disable_click_time = None 
    if not settings:
        if bi.power_button in buttons:
            buttons.remove(bi.power_button)
        if bi.fs_button in buttons:
            buttons.remove(bi.fs_button)
        if ascheck:
            if bi.ason_button in buttons:
                buttons.remove(bi.ason_button)

    return buttons