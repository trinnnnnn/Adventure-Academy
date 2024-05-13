from utils.window import width, height
import pygame
import functions.buttoninstance as bi
import functions.keypress as k
import functions.text as text
import utils.data as data
from functions.saveloadmanager import Save
from functions.buttonfunction import CursorChanger

# MainMenu class to handle the main menu functionality
class Newsave:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.name = ""
        self.buttons = [bi.start_button]
        self.last_keypress_time = pygame.time.get_ticks()

    def run(self):
        # Display the main menu background
        self.display.fill((0, 255, 255))

        if bi.start_button.draw(self.display):
            self.gameStateManager.set_state("scoringtest")

        if bi.save_button.draw(self.display):
            Save(data.userdata, "testing")

        text.draw_text(self.name, (255,255,255), width//2, height//2, 50, self.display)
        self.name, _ = k.Keypress(self, "mainmenu", self.name, None)
        data.userdata["username"] = self.name

        CursorChanger.change_cursor(self.buttons, self.display)