import pygame
import functions.buttoninstance as bi
import assets.assets as a
from functions.buttonfunction import CursorChanger
from utils.window import width, height
from utils.defaultbutton import DefaultButtons
from functions.transition import fade, fadein
import functions.text as text
import utils.data as data

class Categorymenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.shapes_button, bi.alphabet_button, bi.colours_button, bi.power_button]
        self.bg_x = 0
        self.scroll_speed = 0.6
        self.fade_alpha = 255
        self.text = ""

    def run(self):
        self.text = f"Hello {data.userdata['username']}"

        self.bg_x += self.scroll_speed
        if self.bg_x > width:
            self.bg_x = 0
        self.display.blit(a.unscroll_bg, (self.bg_x - width, 0))
        self.display.blit(a.unscroll_bg, (self.bg_x, 0))

        a.textframe2_rect.center = width//2, height//2
        self.display.blit(a.textframe2, a.textframe2_rect)\
        
        text.draw_text(self.text, (0, 0, 0), width//2, 120, 40, self.display)

        if bi.shapes_button.draw(self.display):
            self.gameStateManager.set_state("stagemenu")
            fade(self.display)

        if bi.alphabet_button.draw(self.display):
            pass

        if bi.colours_button.draw(self.display):
            pass

        DefaultButtons(self.display)
        
        CursorChanger.change_cursor(self.buttons, self.display)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 
