import pygame, random
import utils.data as database
import functions.buttoninstance as bi
import functions.text as text
import functions.keypress as k
import assets.assets as a
import utils.defaultbutton as df
from utils.window import width, height
from functions.saveloadmanager import Save
from functions.buttonfunction import CursorChanger
from functions.transition import *
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor

class ShapeSpelling:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.answer = ""
        self.score = 0
        self.tint_surface = pygame.Surface((width, height))
        self.tint_surface.set_alpha(128)
        self.tint_surface.fill((0, 0, 0))
        self.buttons = []
        self.last_keypress_time = pygame.time.get_ticks()
        self.fade_alpha = 255
        self.data_randomized = False
        self.question = 1
        self.confirm = False
        self.question_start_time = None
        self.return_pressed = False
        self.used_shapes = []
        self.cursor = CustomCursor()

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

        if pygame.mouse.get_pressed()[0]:
            self.confirm = True

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if not self.confirm:
            self.display.blit(self.tint_surface,(0, 0))
            a.textframe_rect.center = width//2, height//2
            self.display.blit(a.textframe, a.textframe_rect)
            a.pleaseread_rect.center = width//2, 150
            self.display.blit(a.pleaseread, a.pleaseread_rect)
            text.draw_text("Type the name of the\nshape using your keyboard\nand press the green button \nor enter key\nto confirm your answer", (0, 0, 0), width//2, 280, 35, self.display)
            text.draw_text("...press your left mousebutton to continue...", (0, 0, 0), width//2, 550, 20, self.display)

        if self.confirm:
            self.buttons.append(bi.confirm2_button)
            a.textinputframe_rect.center = width//2, 550
            self.display.blit(a.textinputframe, a.textinputframe_rect)
            text.draw_text(self.answer, (0, 0, 0), width//2, 550, 50, self.display)
            database.userdata["shapespellingcheck"] = True
            self.answer, self.return_pressed = k.Keypress(self, None, self.answer, None)

            if bi.confirm2_button.draw(self.display) or self.return_pressed:
                if self.answer == self.data_name:
                    self.score += 1
                self.question +=1
                fade(self.display)
                self.data_randomized = False
                self.question_start_time = None
                self.answer = ""
                self.fade_alpha = 255

            if self.question is 1:
                self.data_rect = self.current_shape.get_rect()
                self.data_rect.center = width//2, 300
                self.display.blit(self.current_shape, self.data_rect)

            if self.question is 2:
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

            if self.question is 3:
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

            if self.question is 4:
                database.userdata["shapespelling"] = self.score
                self.gameStateManager.set_state("stagemenu")
                fade(self.display)
                self.score = 0

            df.DefaultButtons(self.display, self.buttons)
            if self.gameStateManager.has_state_changed():
                if df.settings:
                    df.settings = False

        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() is not "shapespelling":
            self.question = 1
            self.used_shapes = []
            self.confirm = False

