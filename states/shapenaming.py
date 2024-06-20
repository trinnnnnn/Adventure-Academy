import pygame, random
import utils.data as database
import functions.buttoninstance as bi
import functions.text as text
import assets.assets as a
import utils.defaultbutton as df
from utils.window import width, height
from functions.saveloadmanager import Save
from functions.buttonfunction import CursorChanger
from functions.transition import *
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor
from functions.floatanim import FloatAnim

class ShapeNaming:
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
        self.used_shapes = []
        self.cursor = CustomCursor()
        self.mouseclick_delay = pygame.time.get_ticks()
        self.float_anim = FloatAnim(0.01, 12)

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
        self.data1_name = available_shapes[0]
        self.data2_name = available_shapes[1]
        self.data3_name = available_shapes[2]
        self.data4_name = available_shapes[3]
        self.current_shape = data[self.data1_name]
        self.used_shapes.append(self.data1_name)

        options_set = {self.data1_name, self.data2_name, self.data3_name, self.data4_name}
        self.option1 = random.choice(list(options_set))
        options_set.remove(self.option1)
        self.option2 = random.choice(list(options_set))
        options_set.remove(self.option2)
        self.option3 = random.choice(list(options_set))
        options_set.remove(self.option3)
        self.option4 = random.choice(list(options_set))

    def reset(self):
        self.question = 1
        self.used_shapes = []
        self.confirm = False
        self.data_randomized = False

    def run(self):
        self.set_data(database.shapes)
        if not self.data_randomized:
            self.data_randomizer(self.data)
            self.data_randomized = True

        current_time = pygame.time.get_ticks()

        if pygame.mouse.get_pressed()[0] and self.confirm is False:
            if current_time - self.mouseclick_delay >= 1000:
                self.confirm = True

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if not self.confirm:
            if bi.choose1_button in self.buttons:
                self.buttons.remove(bi.choose1_button)
            if bi.choose2_button in self.buttons:
                self.buttons.remove(bi.choose2_button)
            if bi.choose3_button in self.buttons:
                self.buttons.remove(bi.choose3_button)
            if bi.choose4_button in self.buttons:
                self.buttons.remove(bi.choose4_button)
            self.float_offset = self.float_anim.update()
            self.display.blit(self.tint_surface,(0, 0))
            a.textframe_rect.center = width//2, height//2 + self.float_offset
            self.display.blit(a.textframe, a.textframe_rect)
            a.pleaseread_rect.center = width//2, 150 + self.float_offset
            self.display.blit(a.pleaseread, a.pleaseread_rect)
            text.draw_text("choose the correct name\nof the shape displayed\nfrom the given options", (0, 0, 0), width//2, 300 + self.float_offset, 35, self.display)
            text.draw_text("...press your left mousebutton to continue...", (0, 0, 0), width//2, 550 + self.float_offset, 20, self.display)

        if self.confirm:
            if bi.choose1_button not in self.buttons:
                self.buttons.append(bi.choose1_button)
            if bi.choose2_button not in self.buttons:
                self.buttons.append(bi.choose2_button)
            if bi.choose3_button not in self.buttons:
                self.buttons.append(bi.choose3_button)
            if bi.choose4_button not in self.buttons:
                self.buttons.append(bi.choose4_button)
            database.userdata["shapenamingcheck"] = True
            a.textframe2_rect.center = width//2, 550
            self.display.blit(a.textframe2, a.textframe2_rect)
            if self.question != 4:
                self.data_rect = self.current_shape.get_rect()
                self.data_rect.center = width//2, 250
                self.display.blit(self.current_shape, self.data_rect)
                text.draw_text(self.option1, (0, 0, 0), 350, 600, 35, self.display, "left")
                text.draw_text(self.option2, (0, 0, 0), 350, 460, 35, self.display, "left")
                text.draw_text(self.option3, (0, 0, 0), 750, 600, 35, self.display, "left")
                text.draw_text(self.option4, (0, 0, 0), 750, 460, 35, self.display, "left")
                for i in range(1, 5):
                    if getattr(bi, f'choose{i}_button').draw(self.display):
                        selected_option = getattr(self, f"option{i}")
                        if selected_option == self.data1_name:
                            self.score += 1
                        self.question += 1
                        fade(self.display)
                        self.fade_alpha = 255
                        self.data_randomized = False
                        break

            if self.question == 4:
                database.userdata["shapenaming"] = self.score
                self.gameStateManager.set_state("stagemenu")
                fade(self.display)
                self.score = 0

            df.DefaultButtons(self.display, self.buttons)

        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() != "shapenaming":
            self.reset()