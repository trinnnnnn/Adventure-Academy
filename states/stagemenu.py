import functions.buttoninstance as bi
import assets.assets as a
import utils.defaultbutton as df
from functions.buttonfunction import CursorChanger
from utils.window import width, height
from functions.transition import *
import functions.text as text
import utils.data as data
import utils.guide as g
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor
from functions.floatanim import FloatAnim

class Stagemenu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = []
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.shapes = 0
        self.shapes_minigame = ""
        self.shapes_minigame_state = ""
        self.cursor = CustomCursor()
        self.float_anim = FloatAnim(0.01, 10)
        self.text_col = (200, 200, 200)
        self.shadow = (120, 120, 120)

    def scorecheck(self, score):
        a.zerostars_rect.center = width//2, 450 + self.float_offset
        if data.userdata[score] == 0:
            self.display.blit(a.zerostars, a.zerostars_rect)
        if data.userdata[score] == 1:
            self.display.blit(a.onestars, a.zerostars_rect)
        if data.userdata[score] == 2:
            self.display.blit(a.twostars, a.zerostars_rect)
        if data.userdata[score] == 3:
            self.display.blit(a.threestars, a.zerostars_rect)
            self.text_col = (255, 255, 0)
            self.shadow = (120, 120, 0)

    def run(self):

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        if bi.play_button not in self.buttons:
            self.buttons.append(bi.play_button)
        if bi.save_button not in self.buttons:
            self.buttons.append(bi.save_button)
        if bi.back_button not in self.buttons:
            self.buttons.append(bi.back_button)

        if bi.back_button.draw(self.display):
            self.gameStateManager.set_state("categorymenu")
            fade(self.display)
        
        if g.guide:
            if bi.settings_button.draw(self.display):
                pass
        if df.settings:
            if bi.guide_button.draw(self.display):
                pass

        if self.gameStateManager.get_theme() == "shapes" :
            self.float_offset = self.float_anim.update()
            a.textframe3_rect.center = width//2, height//2 + self.float_offset
            self.display.blit(a.textframe3, a.textframe3_rect)
            a.shapes_rect.center = width//2, 210 + self.float_offset
            self.display.blit(a.shapes, a.shapes_rect)
            text.draw_text(self.shapes_minigame, self.text_col, width//2, height//2 + self.float_offset, 70, self.display, shadow=True, outline=True, shadow_color=self.shadow)
            if bi.play_button.draw(self.display):
                self.gameStateManager.set_state(self.shapes_minigame_state)
                fade(self.display)
            if self.shapes == 0:
                if data.userdata["shapenamingcheck"] is True:
                    self.text_col = (255, 255, 255)
                    self.shadow = (120, 120, 120)
                    self.scorecheck("shapenaming")
                else:
                    self.text_col = (200, 200, 200)
                    self.shadow = (120, 120, 120)
                if bi.leftarrow_button in self.buttons:
                    self.buttons.remove(bi.leftarrow_button)
                if bi.rightarrow_button not in self.buttons:
                    self.buttons.append(bi.rightarrow_button)
                self.shapes_minigame = "naming"
                self.shapes_minigame_state = "shapenaming"
            if self.shapes == 1:
                if data.userdata["shapematchingcheck"] is True:
                    self.text_col = (255, 255, 255)
                    self.shadow = (120, 120, 120)
                    self.scorecheck("shapematching")
                else:
                    self.text_col = (200, 200, 200)
                    self.shadow = (120, 120, 120)
                if bi.rightarrow_button not in self.buttons:
                    self.buttons.append(bi.rightarrow_button)
                if bi.leftarrow_button not in self.buttons:
                    self.buttons.append(bi.leftarrow_button)
                self.shapes_minigame = "matching"
                self.shapes_minigame_state = "shapematching"
            if self.shapes == 2:
                if data.userdata["shapespellingcheck"] is True:
                    self.text_col = (255, 255, 255)
                    self.shadow = (120, 120, 120)
                    self.scorecheck("shapespelling")
                else:
                    self.text_col = (200, 200, 200)
                    self.shadow = (120, 120, 120)
                if bi.rightarrow_button in self.buttons:
                    self.buttons.remove(bi.rightarrow_button)
                self.shapes_minigame = "spelling"
                self.shapes_minigame_state = "shapespelling"

            if self.shapes > 0:
                if bi.leftarrow_button.draw(self.display):
                    self.shapes -= 1
                    
            if self.shapes != 2:
                if bi.rightarrow_button.draw(self.display):
                    self.shapes += 1

            if not df.settings:
                g.Guide(self.display, self.buttons, "shapes")

        if self.gameStateManager.get_theme() == "colours" :
            text.draw_text("colours", (0, 0, 0), width//2, height//2, 50, self.display)

            if not df.settings:
                g.Guide(self.display, self.buttons, "colours")

        if self.gameStateManager.get_theme() == "alphabet" :
            text.draw_text("alphabet", (0, 0, 0), width//2, height//2, 50, self.display)

            if not df.settings:
                g.Guide(self.display, self.buttons, "alphabet")

        if bi.save_button.draw(self.display):
            self.gameStateManager.set_state("saves")
            fade(self.display)

        if not g.guide:
            df.DefaultButtons(self.display, self.buttons)


        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5 

        if self.gameStateManager.get_state() != "stagemenu":
            self.fade_alpha = 255
            if (self.gameStateManager.get_state() != "shapematching" and 
                self.gameStateManager.get_state() != "shapenaming" and 
                self.gameStateManager.get_state() != "shapespelling"):
                self.shapes = 0
