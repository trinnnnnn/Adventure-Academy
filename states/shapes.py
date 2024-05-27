import pygame, random
import utils.data as database
import functions.buttoninstance as bi
import functions.text as text
import functions.keypress as k
from utils.window import width, height
from functions.saveloadmanager import Save
from functions.buttonfunction import CursorChanger
from functions.transition import *
from functions.scrollingbg import scroll_bg
import assets.assets as a

class Shapes:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.answer = ""
        self.score = 0
        self.buttons = [bi.start_button]
        self.last_keypress_time = pygame.time.get_ticks()
        self.fade_alpha = 255
        self.data_randomized = False
        self.question = 1
        self.question_start_time = None
        self.used_shapes = []

    def set_data(self, data):
        self.data = data

    def data_randomizer(self, data):
        available_shapes = list(data.keys())
        for used_shape in self.used_shapes:
            if used_shape in available_shapes:
                available_shapes.remove(used_shape)

        if not available_shapes:
            self.used_shapes = []
            available_shapes = list(data.keys())

        random.shuffle(available_shapes)
        self.data_name = available_shapes[0]
        self.current_shape = data[self.data_name]
        self.used_shapes.append(self.data_name)

    def run(self):
        self.set_data(database.shapes)
        if not self.data_randomized:
            self.data_randomizer(self.data)
            self.data_randomized = True

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        a.textinputframe_rect.center = width//2, 550
        self.display.blit(a.textinputframe, a.textinputframe_rect)
        text.draw_text(self.answer, (0, 0, 0), width//2, 550, 50, self.display)
        self.answer, _, _ = k.Keypress(self, None, self.answer, None)
        database.userdata["score"] = self.score

        if bi.confirm2_button.draw(self.display):
            self.question +=1
            fade(self.display)
            self.data_randomized = False
            self.question_start_time = None
            self.answer = ""

        if self.question == 1:
            self.data_rect = self.current_shape.get_rect()
            self.data_rect.center = width//2, 300
            self.display.blit(self.current_shape, self.data_rect)
            if self.answer == self.data_name:
                self.score = 1

        if self.question == 2:
            current_time = pygame.time.get_ticks()
            if self.question_start_time is None:
                self.question_start_time = current_time
                self.data_randomized = False
            if current_time - self.question_start_time > 1:
                self.question_start_time = current_time
                self.data_randomized = True

            self.data_rect = self.current_shape.get_rect()
            self.data_rect.center = width//2, 300
            self.display.blit(self.current_shape, self.data_rect)
            if self.answer == self.data_name:
                self.score = 2

        if self.question == 3:
            current_time = pygame.time.get_ticks()
            if self.question_start_time is None:
                self.question_start_time = current_time
                self.data_randomized = False
            if current_time - self.question_start_time > 1:
                self.question_start_time = current_time
                self.data_randomized = True

            self.data_rect = self.current_shape.get_rect()
            self.data_rect.center = width//2, 300
            self.display.blit(self.current_shape, self.data_rect)
            if self.answer == self.data_name:
                self.score = 3

        if self.question == 4:
            Save(database.userdata, "save1")
            self.gameStateManager.set_state("categorymenu")
            fade(self.display)

        CursorChanger.change_cursor(self.buttons)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() != "shapes":
            self.question = 1
            self.used_shapes = []

