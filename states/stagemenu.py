import pygame
import functions.buttoninstance as bi
import assets.assets as a
from functions.buttonfunction import CursorChanger
from utils.window import width, height
from utils.defaultbutton import DefaultButtons
from functions.transition import fade, fadein
import functions.text as text
import utils.data as data

class Stagemenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.power_button]
        self.bg_x = 0
        self.scroll_speed = 0.6
        self.fade_alpha = 255

    def run(self):

        self.bg_x += self.scroll_speed
        if self.bg_x > width:
            self.bg_x = 0
        self.display.blit(a.unscroll_bg, (self.bg_x - width, 0))
        self.display.blit(a.unscroll_bg, (self.bg_x, 0))

        DefaultButtons(self.display)
        
        CursorChanger.change_cursor(self.buttons, self.display)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 
