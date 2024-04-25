import pygame
import utils.window as window
from utils.fps import FPS
from states.mainmenu import MainMenu

pygame.init()

pygame.mixer.init()

#creating window, caption, and icon
caption = window.caption
screen = window.screen

clock = pygame.time.Clock()

class Game :
    def __init__(self) :
        pygame.init()

        #screen width and height
        self.screen = screen

        #fps
        self.clock = pygame.time.Clock()

        #starting gamestate
        self.gameStateManager = GameStateManager("mainmenu")

        #gamestates to call
        self.mainmenu = MainMenu(self.screen, self.gameStateManager)

        #gamestate dictionary
        self.states = {"mainmenu":self.mainmenu
                       }
        
    def run(self) :
        
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

class GameStateManager :
        def __init__(self, currentState) :
            self.currentState = currentState
            
        def get_state(self) :
            return self.currentState
        def set_state(self, state) :
            self.currentState = state

if __name__ == "__main__":
    p = Game()
    p.run()