import pygame
import functions.buttoninstance as bi
import functions.keypress as k
import functions.text as text
import utils.data as data
import assets.assets as a
from utils.window import width, height
from functions.saveloadmanager import Save
from functions.buttonfunction import CursorChanger
from utils.defaultbutton import DefaultButtons
from functions.transition import *
from functions.scrollingbg import scroll_bg
from functions.xshake import x_shake
from functions.customcursor import CustomCursor

# MainMenu class to handle the main menu functionality
class Newsave:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.name = ""
        self.buttons = [bi.start_button, bi.power_button]
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.last_keypress_time = pygame.time.get_ticks()
        self.fade_alpha = 255
        self.limit = False
        self.width = width // 2
        self.original_width = self.width
        self.shake_amplitude = 12
        self.shake_speed = 80
        self.shake_duration = 1.8
        self.shake_start_time = None
        self.elapsed = 0
        self.text = ""
        self.cursor = CustomCursor()

    def run(self):

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if bi.start_button.draw(self.display):
            self.gameStateManager.set_state("categorymenu")
            fade(self.display)

        if self.limit:
            
            self.width, self.shake_start_time, self.elapsed = x_shake(self.width, self.original_width, self.shake_amplitude, self.shake_speed, self.shake_duration, self.shake_start_time)
        
        if len(self.name) == 13:
            self.text = "Maximum characters\nhave been reached"
        else:
            self.text = "Enter your name"
        a.textinputframe_rect.center = self.width, 400
        self.display.blit(a.textinputframe, a.textinputframe_rect)

        text.draw_text(self.text, (0, 0, 0), self.width, 220, 50, self.display)
        text.draw_text(self.name, (0, 0, 0), self.width, 400, 50, self.display)
        self.name, _, self.limit = k.Keypress(self, "categorymenu", self.name, 13, 1.8)
        data.userdata["username"] = self.name

        DefaultButtons(self.display, self.buttons)

        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 