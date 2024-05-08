from utils.window import width, height
import os
import functions.buttoninstance as bi
import functions.text as text
import utils.data as data
from functions.buttonfunction import CursorChanger
from functions.saveloadmanager import Load

# MainMenu class to handle the main menu functionality
class Start:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.start_button]

    def run(self):

        savecheck = os.path.isfile("saves/testing.txt")

        self.display.fill((0, 255, 255))

        if bi.start_button.draw(self.display) :
            self.gameStateManager.set_state("newsave")

        if savecheck:
            text.draw_text(data.data["username"], (255,255,255), width//2, 100, 50, self.display)
            if bi.save_button.draw(self.display) :
                Load("testing")

        text.draw_text("new game", (255,255,255), width//2, height//2, 50, self.display)

        CursorChanger.change_cursor(self.buttons, self.display)