import pygame
import functions.buttoninstance as bi
import functions.keypress as k
import functions.text as text
import utils.data as data
import assets.assets as a
import utils.defaultbutton as df
from utils.window import width
from functions.buttonfunction import CursorChanger
from functions.transition import *
from functions.scrollingbg import scroll_bg
from functions.xshake import x_shake
from functions.customcursor import CustomCursor
import itertools

class Newsave:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.name = ""
        self.namecheck = ""
        self.buttons = []
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.limit = False
        self.width = width // 2
        self.original_width = self.width
        self.shake_amplitude = 12
        self.shake_speed = 80
        self.shake_duration = 1.8
        self.shake_start_time = None
        self.return_pressed = False
        self.elapsed = 0
        self.text = "Enter your name"
        self.limit_start_time = 0
        self.cursor = CustomCursor()
        self.resetcheck = False
        self.offsetcheck = False

    def reset(self):
        self.name = ""
        self.namecheck = ""
        data.userdata.update({
            "username": "",
            "shapenamingcheck": False,
            "shapenaming": 0,
            "shapematchingcheck": False,
            "shapematching": 0,
            "shapespellingcheck": False,
            "shapespelling": 0,
        })

    def check_key_press(self, keys):
        for i in itertools.chain(range(pygame.K_a, pygame.K_z + 1), range(pygame.K_0, pygame.K_9 + 1)):
            if keys[i] and len(self.namecheck) == 14:
                self.offsetcheck = True
                self.limit = True
                self.limit_start_time = pygame.time.get_ticks()
                self.text = "Maximum characters\nhave been reached"
                return

    def draw_text(self, offset):
        a.textinputframe_rect.center = self.width, 400
        self.display.blit(a.textinputframe, a.textinputframe_rect)
        text.draw_text(self.text, (255, 255, 255), self.width, 220 - offset, 80, self.display, shadow=True, outline=True)
        text.draw_text(self.name, (0, 0, 0), self.width, 400, 70, self.display)

    def handle_limit(self):
        if self.limit:
            self.width, self.shake_start_time, self.elapsed = x_shake(
                self.width, self.original_width, self.shake_amplitude, 
                self.shake_speed, self.shake_duration, self.shake_start_time)
            if pygame.time.get_ticks() - self.limit_start_time >= 1500:
                self.limit = False

    def run(self):
        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)
        offset = 60 if self.offsetcheck else 0

        if not self.resetcheck:
            self.reset()
            self.resetcheck = True

        if bi.play_button not in self.buttons:
            self.buttons.append(bi.play_button)

        if bi.play_button.draw(self.display) or self.return_pressed:
            if not self.name:
                self.limit = True
                self.limit_start_time = pygame.time.get_ticks()
                self.text = "Please enter your name"
            else:
                self.gameStateManager.set_state("categorymenu")
                fade(self.display)

        keys = pygame.key.get_pressed()
        self.check_key_press(keys)

        if len(self.name) < 13 and self.name:
            self.text = "Enter your name"
            self.offsetcheck = False

        self.handle_limit()
        self.draw_text(offset)

        self.name, self.return_pressed = k.Keypress(self, None, self.name, 13)
        self.namecheck, _ = k.Keypress(self, None, self.name, 14)

        data.userdata["username"] = self.name

        df.DefaultButtons(self.display, self.buttons, False)

        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() != "newsave":
            self.fade_alpha = 255
            self.resetcheck = False
