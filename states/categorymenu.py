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
import functions.buttonfunction as bf

class Categorymenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.text = ""
        self.shapes_button = bi.shapes_button
        self.shapes_size = 0.65
        self.shapes_x = 400
        self.shapes_y = 300
        self.shapes_target_size = self.shapes_size
        self.shapes_target_x = self.shapes_x
        self.shapes_target_y = self.shapes_y
        self.colours_button = bi.colours_button
        self.colours_size = 0.65
        self.colours_x = width//2
        self.colours_y = 400
        self.colours_target_size = self.colours_size
        self.colours_target_x = self.colours_x
        self.colours_target_y = self.colours_y
        self.alphabet_button = bi.alphabet_button
        self.alphabet_size = 0.65
        self.alphabet_x = 820
        self.alphabet_y = 300
        self.alphabet_target_size = self.alphabet_size
        self.alphabet_target_x = self.alphabet_x
        self.alphabet_target_y = self.alphabet_y
        self.buttons = [bi.power_button, bi.save_button]
        self.onbutton = 0

    def run(self):

        pos = pygame.mouse.get_pos()

        self.text = f"Hello {data.userdata['username']}"

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        a.textframe2_rect.center = width // 2, height // 2
        self.display.blit(a.textframe2, a.textframe2_rect)
        
        text.draw_text(self.text, (0, 0, 0), width // 2, 120, 40, self.display)

        shapes_button_clicked = self.shapes_button.draw(self.display)
        colours_button_clicked = self.colours_button.draw(self.display)
        alphabet_button_clicked = self.alphabet_button.draw(self.display)

        current_time = pygame.time.get_ticks()

        if shapes_button_clicked and self.onbutton is 0:
            self.onbutton = 1
            self.button_click_time = current_time
        elif shapes_button_clicked and self.onbutton is 1:
            if current_time - self.button_click_time >= 200:
                self.gameStateManager.set_theme("shapes")
                self.gameStateManager.set_state("stagemenu")
                fade(self.display)
        elif self.shapes_button.rect.collidepoint(pos) == False and self.onbutton is 1:
            self.onbutton = 0
        if colours_button_clicked and self.onbutton is 0:
            self.onbutton = 2
            self.button_click_time = current_time
        elif colours_button_clicked and self.onbutton is 2:
            if current_time - self.button_click_time >= 200:
                self.gameStateManager.set_theme("colours")
                self.gameStateManager.set_state("stagemenu")
                fade(self.display)
        elif self.colours_button.rect.collidepoint(pos) == False and self.onbutton is 2:
            self.onbutton = 0
        if alphabet_button_clicked and self.onbutton is 0:
            self.onbutton = 3
            self.button_click_time = current_time
        elif shapes_button_clicked and self.onbutton is 3:
            if current_time - self.button_click_time >= 200:
                self.gameStateManager.set_theme("shapes")
                self.gameStateManager.set_state("stagemenu")
                fade(self.display)
        elif self.alphabet_button.rect.collidepoint(pos) == False and self.onbutton is 3:
            self.onbutton = 0


        if self.onbutton == 1:
            self.shapes_target_size = 1.2
            self.shapes_target_x = width // 2
            self.shapes_target_y = height // 2
            self.colours_target_size = 0.2
            self.colours_target_x = width//2
            self.colours_target_y = 480
            self.alphabet_target_size = 0.2
            self.alphabet_target_x = 820
            self.alphabet_target_y = 240
        elif self.onbutton == 2:
            self.shapes_target_size = 0.2
            self.shapes_target_x = 400
            self.shapes_target_y = 240
            self.colours_target_size = 1.2
            self.colours_target_x = width//2
            self.colours_target_y = height//2
            self.alphabet_target_size = 0.2
            self.alphabet_target_x = 820
            self.alphabet_target_y = 240
        elif self.onbutton == 3:
            self.shapes_target_size = 0.2
            self.shapes_target_x = 400
            self.shapes_target_y = 240
            self.colours_target_size = 0.2
            self.colours_target_x = width//2
            self.colours_target_y = 480
            self.alphabet_target_size = 1.2
            self.alphabet_target_x = width //2
            self.alphabet_target_y = height//2
        elif self.onbutton == 0:
            self.shapes_target_size = 0.65
            self.shapes_target_x = 400
            self.shapes_target_y = 300
            self.colours_target_size = 0.65
            self.colours_target_x = width//2
            self.colours_target_y = 400
            self.alphabet_target_size = 0.65
            self.alphabet_target_x = 820
            self.alphabet_target_y = 300

        # Smoothly interpolate to the target size and position
        self.shapes_size = self.lerp(self.shapes_size, self.shapes_target_size, 0.1)
        self.shapes_x = self.lerp(self.shapes_x, self.shapes_target_x, 0.1)
        self.shapes_y = self.lerp(self.shapes_y, self.shapes_target_y, 0.1)

        self.colours_size = self.lerp(self.colours_size, self.colours_target_size, 0.1)
        self.colours_x = self.lerp(self.colours_x, self.colours_target_x, 0.1)
        self.colours_y = self.lerp(self.colours_y, self.colours_target_y, 0.1)

        self.alphabet_size = self.lerp(self.alphabet_size, self.alphabet_target_size, 0.1)
        self.alphabet_x = self.lerp(self.alphabet_x, self.alphabet_target_x, 0.1)
        self.alphabet_y = self.lerp(self.alphabet_y, self.alphabet_target_y, 0.1)
        
        # Update shapes_button with the new size and position
        self.shapes_button = bf.Button(self.shapes_x, self.shapes_y, a.shapes_img, a.shapesdown_img, self.shapes_size)
        self.colours_button = bf.Button(self.colours_x, self.colours_y, a.colours_img, a.coloursdown_img, self.colours_size)
        self.alphabet_button = bf.Button(self.alphabet_x, self.alphabet_y, a.alphabet_img, a.alphabetdown_img, self.alphabet_size)

        if self.shapes_button not in self.buttons:
            self.buttons.append(self.shapes_button)
        if self.colours_button not in self.buttons:
            self.buttons.append(self.colours_button)
        if self.alphabet_button not in self.buttons:
            self.buttons.append(self.alphabet_button)

        if bi.save_button.draw(self.display):
            self.gameStateManager.set_theme("save")
            self.gameStateManager.set_state("loadsave")
            fade(self.display)

        DefaultButtons(self.display)
        
        CursorChanger.change_cursor(self.buttons)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() != "categorymenu":
            self.fade_alpha = 255
            self.onbutton = 0
    

    def lerp(self, start, end, t):
        return start + t * (end - start)
