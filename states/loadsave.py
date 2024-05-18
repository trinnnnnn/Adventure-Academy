from utils.window import width, height
import functions.buttoninstance as bi
import functions.text as text
import utils.data as data
import assets.assets as a
import os
from functions.buttonfunction import CursorChanger
from functions.saveloadmanager import Load
from functions.transition import fade, fadein
from utils.defaultbutton import DefaultButtons

class Loadsave:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.start_button, bi.power_button]
        self.bg_x = 0
        self.scroll_speed = 0.6
        self.fade_alpha = 255

    def run(self):
        save1check = os.path.isfile("saves/save1.txt")
        save2check = os.path.isfile("saves/save2.txt")
        save3check = os.path.isfile("saves/save3.txt")

        # Background scrolling logic
        self.bg_x += self.scroll_speed
        if self.bg_x > width:
            self.bg_x = 0

        # Draw the scrolling background
        self.display.blit(a.unscroll_bg, (self.bg_x - width, 0))
        self.display.blit(a.unscroll_bg, (self.bg_x, 0))

        a.textframe_rect.center = width//2, height//2
        self.display.blit(a.textframe, a.textframe_rect)

        if self.gameStateManager.get_theme() == "load":
            if save1check:
                self.buttons.append(bi.slot1_button)
                if bi.slot1_button.draw(self.display):
                    Load("save1")
                    self.gameStateManager.set_state("categorymenu")
                    fade(self.display)
            else:
                a.scaleemptyslot1_rect.center = 380, height//2
                self.display.blit(a.scaleemptyslot1, a.scaleemptyslot1_rect)

            if save2check:
                self.buttons.append(bi.slot2_button)
                if bi.slot2_button.draw(self.display):
                    Load("save2")
                    self.gameStateManager.set_state("categorymenu")
                    fade(self.display)
            else:
                a.scaleemptyslot2_rect.center = width//2, height//2
                self.display.blit(a.scaleemptyslot2, a.scaleemptyslot2_rect)

            if save3check:
                self.buttons.append(bi.slot3_button)
                if bi.slot3_button.draw(self.display):
                    Load("save3")
                    self.gameStateManager.set_state("categorymenu")
                    fade(self.display)
            else:
                a.scaleemptyslot3_rect.center = 900, height//2
                self.display.blit(a.scaleemptyslot3, a.scaleemptyslot3_rect)

        DefaultButtons(self.display)

        CursorChanger.change_cursor(self.buttons, self.display)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 