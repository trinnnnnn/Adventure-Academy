from utils.window import width, height
import os
import pygame
import functions.text as text
import functions.buttoninstance as bi
import assets.assets as a
import utils.defaultbutton as df
from functions.buttonfunction import CursorChanger
from functions.transition import *
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor
from functions.floatanim import FloatAnim

class MainMenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.loadcheck = False
        self.tint_surface = pygame.Surface((width, height))
        self.tint_surface.set_alpha(128)
        self.tint_surface.fill((0, 0, 0))
        self.dbuttons = None
        self.buttons = []
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.cursor = CustomCursor()
        self.float_anim = FloatAnim(0.01, 15)
        self.click = False
        self.clickcheck = False
        self.pause = False

    def check_save_files(self):
        return any(os.path.isfile(f"saves/save{i}.txt") for i in range(1, 4)) or os.path.isfile("saves/saveauto.txt")

    def run_load_check(self):
        self.display.blit(self.tint_surface, (0, 0))
        a.textframe_rect.center = width // 2, height // 2
        self.display.blit(a.textframe, a.textframe_rect)
        text.draw_text("A save file has\nbeen detected. Would you\nlike to load it\nor create a new save?", (0, 0, 0), width // 2, 230, 50, self.display)

        if bi.confirm_button.draw(self.display):
            self.gameStateManager.set_state("loads")
            fade(self.display)
        if bi.unconfirm_button.draw(self.display):
            self.gameStateManager.set_state("newsave")
            fade(self.display)

        self.buttons = [bi.confirm_button, bi.unconfirm_button]

    def run(self):
        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if not self.loadcheck:
            text.draw_text("...press your left mouse button to continue...", (0, 0, 0), width // 2, 600, 40, self.display)
            logo_float_offset = self.float_anim.update()
            a.logo_rect.center = width // 2, 340 + logo_float_offset
            self.display.blit(a.logo, a.logo_rect)

            if df.settings:
                self.pause = True
                self.pause_start_time = pygame.time.get_ticks()
            else:
                if self.pause and pygame.time.get_ticks() - self.pause_start_time >= 500:
                    self.pause = False

            mouse_pressed = pygame.mouse.get_pressed()[0]
            if mouse_pressed and not self.pause and not self.click and not bi.settings_button.rect.collidepoint(pygame.mouse.get_pos()) and not df.settings:
                self.clickcheck = True
            if self.clickcheck and not mouse_pressed:
                self.click = True

            if self.click:
                pygame.mixer.Sound.play(a.button_click)
                if self.check_save_files():
                    self.loadcheck = True
                else:
                    self.gameStateManager.set_state("newsave")
                    fade(self.display)

            if df.autosave:
                df.autosave = False

            df.DefaultButtons(self.display, self.buttons, False)
        elif self.gameStateManager.get_state() == "mainmenu":
            self.run_load_check()

        if self.gameStateManager.get_state() != "mainmenu":
            self.loadcheck = False

        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() != "mainmenu":
            self.fade_alpha = 255
            self.click = False
            self.clickcheck = False
