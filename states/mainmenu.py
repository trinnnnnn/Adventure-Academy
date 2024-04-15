from utils.window import width

# MainMenu class to handle the main menu functionality
class MainMenu:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        # Display the main menu background
        self.display.fill((0, 100, 200))