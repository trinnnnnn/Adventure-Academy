import pygame
import functions.buttoninstance as bi
import assets.assets as a
from functions.buttonfunction import CursorChanger
from utils.window import width, height
from utils.defaultbutton import DefaultButtons
from functions.transition import *
import functions.text as text
import utils.data as data
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor

class Categorymenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.text = f"Hello {data.userdata['username']}"
        self.tint_surface = pygame.Surface((width, height))
        self.tint_surface.set_alpha(128)
        self.tint_surface.fill((0, 0, 0))
        self.confirm = False

        self.shapes_button = bi.shapes_button
        self.shapes_button.x = 400
        self.shapes_button.y = 300
        self.shapes_button.size = 0.65
        self.shapes_target = (0.65, 400, 300)

        self.colours_button = bi.colours_button
        self.colours_button.x = width // 2
        self.colours_button.y = 400
        self.colours_button.size = 0.65
        self.colours_target = (0.65, width // 2, 400)

        self.alphabet_button = bi.alphabet_button
        self.alphabet_button.x = 820
        self.alphabet_button.y = 300
        self.alphabet_button.size = 0.65
        self.alphabet_target = (0.65, 820, 300)

        self.buttons = []
        self.onbutton = 0
        self.cursor = CustomCursor()

    def lerp(self, start, end, t):
        return start + t * (end - start)
        
    def update_button(self, button, target):
        size, x, y = target
        button.size = self.lerp(button.size, size, 0.1)
        button.x = self.lerp(button.x, x, 0.1)
        button.y = self.lerp(button.y, y, 0.1)
        button.update()

    def run(self):
        pos = pygame.mouse.get_pos()
        self.text = f"Hello {data.userdata['username']}"

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if self.confirm:
            self.display.blit(self.tint_surface,(0, 0))
            a.textframe_rect.center = width // 2, 720 // 2
            self.display.blit(a.textframe, a.textframe_rect)
            text.draw_text("are you sure\nyou want to exit\nto the main menu?", (0, 0, 0), width//2, height//2.5, 50, self.display)
            if bi.confirm_button.draw(self.display):
                self.gameStateManager.set_state("mainmenu")
                fade(self.display)
            if bi.unconfirm_button.draw(self.display):
                self.confirm = False
            self.buttons.clear()
            self.buttons.extend({bi.confirm_button, bi.unconfirm_button})

        if not self.confirm:
            self.buttons.extend({bi.back_button, bi.save_button, self.shapes_button, self.colours_button, self.alphabet_button})

            a.textframe2_rect.center = width // 2, height // 2
            self.display.blit(a.textframe2, a.textframe2_rect)

            text.draw_text(self.text, (255, 255, 255), width // 2, 120, 80, self.display, shadow=True, outline=True)

            shapes_button_clicked = self.shapes_button.draw(self.display)
            colours_button_clicked = self.colours_button.draw(self.display)
            alphabet_button_clicked = self.alphabet_button.draw(self.display)

            current_time = pygame.time.get_ticks()

            if shapes_button_clicked and self.onbutton == 0:
                self.onbutton = 1
                self.button_click_time = current_time
            elif shapes_button_clicked and self.onbutton == 1:
                if current_time - self.button_click_time >= 200:
                    self.gameStateManager.set_theme("shapes")
                    self.gameStateManager.set_state("stagemenu")
                    fade(self.display)
            elif not self.shapes_button.rect.collidepoint(pos) and self.onbutton == 1:
                if current_time - self.button_click_time >= 1000:
                    self.onbutton = 0

            if colours_button_clicked and self.onbutton == 0:
                self.onbutton = 2
                self.button_click_time = current_time
            elif colours_button_clicked and self.onbutton == 2:
                if current_time - self.button_click_time >= 200:
                    self.gameStateManager.set_theme("colours")
                    self.gameStateManager.set_state("stagemenu")
                    fade(self.display)
            elif not self.colours_button.rect.collidepoint(pos) and self.onbutton == 2:
                if current_time - self.button_click_time >= 1000:
                    self.onbutton = 0

            if alphabet_button_clicked and self.onbutton == 0:
                self.onbutton = 3
                self.button_click_time = current_time
            elif alphabet_button_clicked and self.onbutton == 3:
                if current_time - self.button_click_time >= 200:
                    self.gameStateManager.set_theme("alphabet")
                    self.gameStateManager.set_state("stagemenu")
                    fade(self.display)
            elif not self.alphabet_button.rect.collidepoint(pos) and self.onbutton == 3:
                if current_time - self.button_click_time >= 1000:
                    self.onbutton = 0

            if self.onbutton == 1:
                self.shapes_target = (1.2, width // 2, height // 2)
                self.colours_target = (0.2, width // 2, 480)
                self.alphabet_target = (0.2, 820, 240)
            elif self.onbutton == 2:
                self.shapes_target = (0.2, 400, 240)
                self.colours_target = (1.2, width // 2, height // 2)
                self.alphabet_target = (0.2, 820, 240)
            elif self.onbutton == 3:
                self.shapes_target = (0.2, 400, 240)
                self.colours_target = (0.2, width // 2, 480)
                self.alphabet_target = (1.2, width // 2, height // 2)
            elif self.onbutton == 0:
                self.shapes_target = (0.65, 400, 300)
                self.colours_target = (0.65, width // 2, 400)
                self.alphabet_target = (0.65, 820, 300)

            self.update_button(self.shapes_button, self.shapes_target)
            self.update_button(self.colours_button, self.colours_target)
            self.update_button(self.alphabet_button, self.alphabet_target)

            if bi.save_button.draw(self.display):
                self.gameStateManager.set_state("saves")
                fade(self.display)

            if bi.back_button.draw(self.display):
                self.confirm = True

            DefaultButtons(self.display, self.buttons)

        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() != "categorymenu":
            self.fade_alpha = 255
            self.onbutton = 0
            self.confirm = False