import pygame, random
import utils.data as data
import functions.buttoninstance as bi
import functions.text as text
import functions.keypress as k
from utils.window import width, height
from functions.saveloadmanager import Save
from functions.buttonfunction import CursorChanger
from functions.transition import *

class Shapes:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.answer = ""
        self.score = 0
        self.buttons = [bi.start_button]
        self.last_keypress_time = pygame.time.get_ticks()
        self.fade_alpha = 255

    def run(self):
        shapes_names = list(data.shapes.keys())
        shapesname0 = shapes_names[0]
        shapes0 = data.shapes[shapesname0]

        self.display.fill((0, 0, 255))

        text.draw_text(self.answer, (255,255,255), width//2, height//2, 50, self.display)
        self.answer, _ = k.Keypress(self, "mainmenu", self.answer, None)
        data.userdata["score"] = self.score

        self.display.blit(shapes0, (0, 0))

        if bi.start_button.draw(self.display) :
            self.score = 1
            self.gameStateManager.set_state("mainmenu")
            Save(data.userdata, "save1")

        if self.answer == shapesname0 :
            self.score = 1

        CursorChanger.change_cursor(self.buttons)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 
