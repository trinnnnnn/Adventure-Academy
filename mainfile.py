import pygame
import utils.window as window
from utils.fps import FPS
from states.mainmenu import MainMenu
from states.loadsave import Loadsave
from states.newsave import Newsave
from states.categorymenu import Categorymenu
from states.stagemenu import Stagemenu
from states.shapes import Shapes

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
        self.loadsave = Loadsave(self.screen, self.gameStateManager)
        self.newsave = Newsave(self.screen, self.gameStateManager)
        self.categorymenu = Categorymenu(self.screen, self.gameStateManager)
        self.stagemenu = Stagemenu(self.screen, self.gameStateManager)
        self.shapes = Shapes(self.screen, self.gameStateManager)

        #gamestate dictionary
        self.states = {"mainmenu":self.mainmenu,
                       "loadsave":self.loadsave,
                       "newsave":self.newsave,
                       "categorymenu":self.categorymenu,
                       "stagemenu":self.stagemenu,
                       "shapes":self.shapes,
                       }
        
    def run(self) :
        
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.screen.fill((0, 0, 0))

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.flip()

            self.clock.tick(FPS)

class GameStateManager :
        def __init__(self, currentState) :
            self.currentState = currentState
            
        def get_state(self) :
            return self.currentState
        
        def set_state(self, state) :
            self.currentState = state

        def get_theme(self):
            return self.theme
        
        def set_theme(self, value):
            self.theme = value

if __name__ == "__main__":
    p = Game()
    p.run()