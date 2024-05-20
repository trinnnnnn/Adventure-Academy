import pygame
import functions.buttoninstance as bi
import assets.assets as a
from functions.buttonfunction import CursorChanger
from utils.window import width, height
from utils.defaultbutton import DefaultButtons
from functions.transition import *
import functions.text as text
import utils.data as data
from functions.scrollingbg import scroll_bg

class Stagemenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.power_button]
        self.bg_x = 0
        self.scroll_speed = 0.6
        self.fade_alpha = 255

    def run(self):

        self.bg_x = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.scroll_speed)

        if self.gameStateManager.get_theme() == "shapes" :
            text.draw_text("shapes", (0, 0, 0), width//2, height//2, 50, self.display)

        if self.gameStateManager.get_theme() == "colours" :
            text.draw_text("colours", (0, 0, 0), width//2, height//2, 50, self.display)

        if self.gameStateManager.get_theme() == "alphabet" :
            text.draw_text("alphabet", (0, 0, 0), width//2, height//2, 50, self.display)

        if bi.save_button.draw(self.display):
            self.gameStateManager.set_theme("save")
            self.gameStateManager.set_state("loadsave")
            fade(self.display)

        DefaultButtons(self.display)
        
        CursorChanger.change_cursor(self.buttons)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 
