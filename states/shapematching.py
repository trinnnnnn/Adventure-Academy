import pygame
import random
import utils.data as database
import functions.buttoninstance as bi
import functions.text as text
import assets.assets as a
import utils.defaultbutton as df
from utils.window import width, height
from functions.buttonfunction import CursorChanger
from functions.transition import *
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor
from functions.floatanim import FloatAnim

class ShapeMatching:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.answer1 = 0
        self.answer2 = 0
        self.answer3 = 0
        self.answer4 = 0
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
        self.confirm_answer = False
        self.question_start_time = None
        self.used_shapes = []
        self.cursor = CustomCursor()
        self.float_anim = FloatAnim(0.01, 12)
        self.dragging_shape = None
        self.drag_offset_x = 0
        self.drag_offset_y = 0

        self.shapeframe1 = pygame.transform.scale(a.shapebox_original, (int(a.shapebox_original.get_width() * 0.35), int(a.shapebox_original.get_height() * 0.4))).convert_alpha()
        self.shapeframe1_rect = self.shapeframe1.get_rect()
        self.shapeframe2 = pygame.transform.scale(a.shapebox_original, (int(a.shapebox_original.get_width() * 0.35), int(a.shapebox_original.get_height() * 0.4))).convert_alpha()
        self.shapeframe2_rect = self.shapeframe2.get_rect()
        self.shapeframe3 = pygame.transform.scale(a.shapebox_original, (int(a.shapebox_original.get_width() * 0.35), int(a.shapebox_original.get_height() * 0.4))).convert_alpha()
        self.shapeframe3_rect = self.shapeframe3.get_rect()
        self.shapeframe4 = pygame.transform.scale(a.shapebox_original, (int(a.shapebox_original.get_width() * 0.35), int(a.shapebox_original.get_height() * 0.4))).convert_alpha()
        self.shapeframe4_rect = self.shapeframe4.get_rect()

        self.shapeframe1_rect.center = (500, 260)
        self.shapeframe2_rect.center = (500, 460)
        self.shapeframe3_rect.center = (780, 260)
        self.shapeframe4_rect.center = (780, 460)

    def set_data(self, data):
        self.data = data

    def data_randomizer(self, data):
        available_shapes = list(data.keys())
        available_positions = [(150, 144), (150, 288), (150, 432), (150, 576)]
        for used_shape in self.used_shapes:
            if used_shape in available_shapes:
                available_shapes.remove(used_shape)

        if not available_shapes:
            self.used_shapes = []
            available_shapes = list(data.keys())

        random.shuffle(available_shapes)
        random.shuffle(available_positions)

        self.data1_name = available_shapes[0]
        self.data2_name = available_shapes[1]
        self.data3_name = available_shapes[2]
        self.data4_name = available_shapes[3]
        self.current1_shape = data[self.data1_name]
        self.current2_shape = data[self.data2_name]
        self.current3_shape = data[self.data3_name]
        self.current4_shape = data[self.data4_name]

        self.shape_rects = {
            self.data1_name: self.current1_shape.get_rect(center=available_positions[0]),
            self.data2_name: self.current2_shape.get_rect(center=available_positions[1]),
            self.data3_name: self.current3_shape.get_rect(center=available_positions[2]),
            self.data4_name: self.current4_shape.get_rect(center=available_positions[3])
        }

        self.shapeframe_rects = {
            self.data1_name: self.shapeframe1_rect,
            self.data2_name: self.shapeframe2_rect,
            self.data3_name: self.shapeframe3_rect,
            self.data4_name: self.shapeframe4_rect
        }

    def drag_and_drop_randomizer(self):
        if not df.settings:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if mouse_pressed[0]:
                if self.dragging_shape is None:
                    for shape_name, shape_rect in self.shape_rects.items():
                        if shape_rect.collidepoint(mouse_x, mouse_y):
                            local_x = mouse_x - shape_rect.x
                            local_y = mouse_y - shape_rect.y
                            if self.data[shape_name].get_at((local_x, local_y))[3] != 0:
                                self.dragging_shape = shape_name
                                self.drag_offset_x = shape_rect.x - mouse_x
                                self.drag_offset_y = shape_rect.y - mouse_y
                                break
                else:
                    shape_rect = self.shape_rects[self.dragging_shape]
                    shape_rect.x = mouse_x + self.drag_offset_x
                    shape_rect.y = mouse_y + self.drag_offset_y
            else:
                if self.dragging_shape is not None:
                    shape_rect = self.shape_rects[self.dragging_shape]
                    if self.shapeframe1_rect.collidepoint(shape_rect.center) and self.dragging_shape == self.data1_name:
                        self.answer1 = 1
                    elif self.shapeframe1_rect.collidepoint(shape_rect.center) and self.dragging_shape != self.data1_name:
                        self.answer1 = 0
                    elif self.shapeframe2_rect.collidepoint(shape_rect.center) and self.dragging_shape == self.data2_name:
                        self.answer2 = 1
                    elif self.shapeframe2_rect.collidepoint(shape_rect.center) and self.dragging_shape != self.data2_name:
                        self.answer2 = 0
                    elif self.shapeframe3_rect.collidepoint(shape_rect.center) and self.dragging_shape == self.data3_name:
                        self.answer3 = 1
                    elif self.shapeframe3_rect.collidepoint(shape_rect.center) and self.dragging_shape != self.data3_name:
                        self.answer2 = 0
                    elif self.shapeframe4_rect.collidepoint(shape_rect.center) and self.dragging_shape == self.data4_name:
                        self.answer4 = 1
                    elif self.shapeframe4_rect.collidepoint(shape_rect.center) and self.dragging_shape != self.data4_name:
                        self.answer4 = 0

                    all_in_boxes = all(
                        any(target_rect.collidepoint(shape_rect.center) for target_rect in (self.shapeframe1_rect, self.shapeframe2_rect, self.shapeframe3_rect, self.shapeframe4_rect))
                        for shape_rect in self.shape_rects.values()
                    )

                    if all_in_boxes:
                        self.confirm_answer = True
                        
                    self.dragging_shape = None

    def reset(self):
        self.answer1 = 0
        self.answer2 = 0
        self.answer3 = 0
        self.answer4 = 0
        self.score = 0
        self.confirm = False
        self.confirm_answer = False
        self.data_randomized = False
        self.used_shapes.clear()

    def run(self):
        self.set_data(database.shapes)
        if not self.data_randomized:
            self.data_randomizer(self.data)
            self.data_randomized = True

        if pygame.mouse.get_pressed()[0] and self.confirm is False:
            self.confirm = True

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if not self.confirm:
            self.display.blit(self.tint_surface, (0, 0))
            self.float_offset = self.float_anim.update()
            a.textframe_rect.center = width // 2, height // 2 + self.float_offset
            self.display.blit(a.textframe, a.textframe_rect)
            a.pleaseread_rect.center = width // 2, 150 + self.float_offset
            self.display.blit(a.pleaseread, a.pleaseread_rect)
            text.draw_text("drag and drop the shapes\nto match them with their\ncorrect name", (0, 0, 0), width // 2, 300 + self.float_offset, 50, self.display)
            text.draw_text("...press your left mouse button to continue...", (0, 0, 0), width // 2, 550 + self.float_offset, 20, self.display)

        if self.confirm_answer:
            self.display.blit(self.tint_surface,(0, 0))
            a.textframe_rect.center = width // 2, 720 // 2
            self.display.blit(a.textframe, a.textframe_rect)
            text.draw_text("are you sure with\nyour answer?", (0, 0, 0), width//2, height//2.5, 60, self.display)
            if bi.confirm_button.draw(self.display):
                self.score = self.answer1 + self.answer2 + self.answer3 + self.answer4
                if self.score == 4:
                    self.score = 3
                elif self.score == 3:
                    self.score = 2
                database.userdata["shapematching"] = self.score
                self.gameStateManager.set_state("stagemenu")
                fade(self.display)
                self.score = 0
            if bi.unconfirm_button.draw(self.display):
                self.confirm_answer = False
            self.buttons.clear()
            self.buttons.extend({bi.confirm_button, bi.unconfirm_button})

        if self.confirm and self.confirm_answer is False:
            database.userdata["shapematchingcheck"] = True

            self.display.blit(self.shapeframe1, self.shapeframe1_rect)
            self.display.blit(self.shapeframe2, self.shapeframe2_rect)
            self.display.blit(self.shapeframe3, self.shapeframe3_rect)
            self.display.blit(self.shapeframe4, self.shapeframe4_rect)

            text.draw_text(self.data1_name, (0, 0 ,0), 500, 260, 30, self.display)
            text.draw_text(self.data2_name, (0, 0 ,0), 500, 460, 30, self.display)
            text.draw_text(self.data3_name, (0, 0 ,0), 780, 260, 30, self.display)
            text.draw_text(self.data4_name, (0, 0 ,0), 780, 460, 30, self.display)

            for shape_name, shape_rect in self.shape_rects.items():
                self.display.blit(self.data[shape_name], shape_rect.topleft)

            self.drag_and_drop_randomizer()
        
            df.DefaultButtons(self.display, self.buttons)

        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() != "shapematching":
            self.fade_alpha = 255
            self.reset()

