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

class Stagemenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.power_button, bi.play_button, bi.save_button]
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.shapes = 0
        self.shapes_minigame = ""
        self.shapes_minigame_state = ""
        self.cursor = CustomCursor()

    def run(self):

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if self.gameStateManager.get_theme() == "shapes" :
            a.textframe3_rect.center = width//2, height//2
            self.display.blit(a.textframe3, a.textframe3_rect)
            a.shapes_rect.center = width//2, 210
            self.display.blit(a.shapes, a.shapes_rect)
            text.draw_text(self.shapes_minigame, (0, 0, 0), width//2, height//2, 70, self.display)
            if bi.play_button.draw(self.display):
                self.gameStateManager.set_state(self.shapes_minigame_state)
                fade(self.display)
            if self.shapes is 0:
                if data.userdata["shapespellingcheck"] is True:
                    a.zerostars_rect.center = width//2, 450
                    if data.userdata["shapespelling"] is 0:
                        self.display.blit(a.zerostars, a.zerostars_rect)
                    if data.userdata["shapespelling"] is 1:
                        self.display.blit(a.onestars, a.zerostars_rect)
                    if data.userdata["shapespelling"] is 2:
                        self.display.blit(a.twostars, a.zerostars_rect)
                    if data.userdata["shapespelling"] is 3:
                        self.display.blit(a.threestars, a.zerostars_rect)
                if bi.leftarrow_button in self.buttons:
                    self.buttons.remove(bi.leftarrow_button)
                if bi.rightarrow_button not in self.buttons:
                    self.buttons.append(bi.rightarrow_button)
                self.shapes_minigame = "spelling"
                self.shapes_minigame_state = "shapespelling"
            if self.shapes is 1:
                if data.userdata["shapenamingcheck"] is True:
                    a.zerostars_rect.center = width//2, 450
                    if data.userdata["shapenaming"] is 0:
                        self.display.blit(a.zerostars, a.zerostars_rect)
                    if data.userdata["shapenaming"] is 1:
                        self.display.blit(a.onestars, a.zerostars_rect)
                    if data.userdata["shapenaming"] is 2:
                        self.display.blit(a.twostars, a.zerostars_rect)
                    if data.userdata["shapenaming"] is 3:
                        self.display.blit(a.threestars, a.zerostars_rect)
                if bi.rightarrow_button is not self.buttons:
                    self.buttons.append(bi.rightarrow_button)
                if bi.leftarrow_button not in self.buttons:
                    self.buttons.append(bi.leftarrow_button)
                self.shapes_minigame = "naming"
                self.shapes_minigame_state = "shapenaming"
            if self.shapes is 2:
                if bi.rightarrow_button in self.buttons:
                    self.buttons.remove(bi.rightarrow_button)
                self.shapes_minigame = "matching"

            if self.shapes > 0:
                if bi.leftarrow_button.draw(self.display):
                    self.shapes -= 1
            if self.shapes is not 2:
                if bi.rightarrow_button.draw(self.display):
                    self.shapes += 1

        if self.gameStateManager.get_theme() == "colours" :
            text.draw_text("colours", (0, 0, 0), width//2, height//2, 50, self.display)

        if self.gameStateManager.get_theme() == "alphabet" :
            text.draw_text("alphabet", (0, 0, 0), width//2, height//2, 50, self.display)

        if bi.save_button.draw(self.display):
            self.gameStateManager.set_state("saves")
            fade(self.display)

        DefaultButtons(self.display, self.buttons)
        
        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 

        if self.gameStateManager.get_state() is not "stagemenu":
            self.fade_alpha = 255
