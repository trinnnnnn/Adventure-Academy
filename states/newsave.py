from utils.window import width, height
import pygame
import functions.buttoninstance as bi
import functions.keypress as k
import functions.text as text
import utils.data as data
import assets.assets as a
from functions.saveloadmanager import Save
from functions.buttonfunction import CursorChanger
from utils.defaultbutton import DefaultButtons
from functions.transition import fade, fadein

# MainMenu class to handle the main menu functionality
class Newsave:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.name = ""
        self.buttons = [bi.start_button, bi.power_button]
        self.bg_x = 0
        self.scroll_speed = 0.6
        self.last_keypress_time = pygame.time.get_ticks()
        self.fade_alpha = 255

    def run(self):

        self.bg_x += self.scroll_speed
        if self.bg_x > width:
            self.bg_x = 0
        self.display.blit(a.unscroll_bg, (self.bg_x - width, 0))
        self.display.blit(a.unscroll_bg, (self.bg_x, 0))

        if bi.start_button.draw(self.display):
            self.gameStateManager.set_state("stagemenu")
            fade(self.display)

        if bi.save_button.draw(self.display):
            Save(data.userdata, "save1")

        text.draw_text(self.name, (0, 0, 0), width//2, height//2, 50, self.display)
        self.name, _ = k.Keypress(self, "mainmenu", self.name, None)
        data.userdata["username"] = self.name

        DefaultButtons(self.display)

        CursorChanger.change_cursor(self.buttons, self.display)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 