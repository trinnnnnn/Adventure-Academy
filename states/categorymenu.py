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
        self.scroll_speed = 0.6
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
        

    def run(self):

        self.onbutton = 0
        
        pos = pygame.mouse.get_pos()

        self.text = f"Hello {data.userdata['username']}"

        self.bg_x = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.scroll_speed)

        a.textframe2_rect.center = width // 2, height // 2
        self.display.blit(a.textframe2, a.textframe2_rect)
        
        text.draw_text(self.text, (0, 0, 0), width // 2, 120, 40, self.display)

        if self.shapes_button.rect.collidepoint(pos):
            self.onbutton = 1
        if self.colours_button.rect.collidepoint(pos):
            self.onbutton = 2
        if self.alphabet_button.rect.collidepoint(pos):
            self.onbutton = 3


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

        if self.shapes_button.draw(self.display):
            self.gameStateManager.set_theme("shapes")
            self.gameStateManager.set_state("stagemenu")
            fade(self.display)

        if self.colours_button.draw(self.display):
            self.gameStateManager.set_theme("colours")
            self.gameStateManager.set_state("stagemenu")
            fade(self.display)

        if self.alphabet_button.draw(self.display):
            self.gameStateManager.set_theme("alphabet")
            self.gameStateManager.set_state("stagemenu")
            fade(self.display)

        if bi.save_button.draw(self.display):
            self.gameStateManager.set_theme("save")
            self.gameStateManager.set_state("loadsave")
            fade(self.display)

        DefaultButtons(self.display)
        
        CursorChanger.change_cursor(self.buttons)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

    def lerp(self, start, end, t):
        return start + t * (end - start)
