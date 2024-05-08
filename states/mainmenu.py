from utils.window import width
import functions.buttoninstance as bi
from functions.buttonfunction import CursorChanger

# MainMenu class to handle the main menu functionality
class MainMenu:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.start_button]

    def run(self):
        # Display the main menu background
        self.display.fill((0, 100, 200))

        if bi.start_button.draw(self.display) :
            self.gameStateManager.set_state("start")
            
        CursorChanger.change_cursor(self.buttons, self.display)