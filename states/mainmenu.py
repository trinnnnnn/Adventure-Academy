from utils.window import width, height
import os, pygame
import functions.text as text
import functions.buttoninstance as bi
import assets.assets as a
from functions.buttonfunction import CursorChanger
from functions.transition import *
from utils.defaultbutton import DefaultButtons
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor

# MainMenu class to handle the main menu functionality
class MainMenu:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.loadcheck = False
        self.tint_surface = pygame.Surface((width, height))
        self.tint_surface.set_alpha(128)
        self.tint_surface.fill((0, 0, 0))
        self.buttons = [bi.start_button, bi.power_button]
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.cursor = CustomCursor()

    def run(self):
        
        savefile1check = os.path.isfile("saves/save1.txt")
        savefile2check = os.path.isfile("saves/save2.txt")
        savefile3check = os.path.isfile("saves/save3.txt")

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if bi.start_button.draw(self.display):
            if savefile1check or savefile2check or savefile3check:
                self.loadcheck = True
            else:
                self.gameStateManager.set_state("newsave")
                fade(self.display)

        if self.loadcheck:
            self.display.blit(self.tint_surface,(0, 0))
            a.textframe_rect.center = width // 2, 720 // 2
            self.display.blit(a.textframe, a.textframe_rect)
            text.draw_text("a save file have been\ndetected, would you like to\nload it or not?", (0, 0, 0), width//2, height//2.5, 36, self.display)
            if bi.confirm_button.draw(self.display):
                self.gameStateManager.set_state("loads")
                fade(self.display)
            if bi.unconfirm_button.draw(self.display):
                self.gameStateManager.set_state("newsave")
                fade(self.display)
            if bi.start_button in self.buttons:
                self.buttons.clear()
                self.buttons.extend({bi.confirm_button, bi.unconfirm_button})

        if self.gameStateManager.get_state() is not "mainmenu":
            self.loadcheck = False

        if not self.loadcheck:
            DefaultButtons(self.display)
        
        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 

        if self.gameStateManager.get_state() is not "mainmenu":
            self.fade_alpha = 255
            self.del_true = False