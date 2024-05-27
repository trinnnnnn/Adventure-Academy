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
from functions.customcursor import CustomCursor

class Stagemenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.power_button]
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.shapes = 0
        self.shapes_minigame = ""
        self.shapes_minigame_state = ""
        self.cursor = CustomCursor()

    def run(self):

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if self.gameStateManager.get_theme() == "shapes" :
            a.textframe3_rect.center = width//2, height//2
            self.display.blit(a.textframe3, a.textframe3_rect)
            text.draw_text(self.shapes_minigame, (0, 0, 0), width//2, height//2.2, 50, self.display)
            if bi.play_button.draw(self.display):
                self.gameStateManager.set_state(self.shapes_minigame_state)
                fade(self.display)
            if self.shapes is 0:
                self.shapes_minigame = "shapes\nspelling"
                self.shapes_minigame_state = "shapes"
            if self.shapes is 1:
                self.shapes_minigame = "shapes\nnaming"
            if self.shapes is 2:
                self.shapes_minigame = "shapes\nmatching"

            if self.shapes > 0:
                if bi.leftarrow_button.draw(self.display):
                    self.shapes -= 1
            if self.shapes is not 2:
                if bi.rightarrow_button.draw(self.display):
                    self.shapes += 1

        if self.gameStateManager.get_theme() == "colours" :
            text.draw_text("colours", (0, 0, 0), width//2, height//2, 50, self.display)

        if self.gameStateManager.get_theme() == "alphabet" :
            text.draw_text("alphabet", (0, 0, 0), width//2, height//2, 50, self.display)

        if bi.save_button.draw(self.display):
            self.gameStateManager.set_state("save")
            fade(self.display)

        DefaultButtons(self.display)
        
        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 
