import functions.buttoninstance as bi
import functions.text as text
import assets.assets as a
import os
import utils.defaultbutton as df
from utils.window import width, height
from functions.buttonfunction import CursorChanger
from functions.saveloadmanager import *
from functions.transition import *
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor

class Loads:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.power_button, bi.back_button]
        self.bg_x = 0
        self.bg_y = 0
        self.scroll_speed = 0.5
        self.fade_alpha = 255
        self.confirm = False
        self.onbutton = 0
        self.empty1 = False
        self.empty2 = False
        self.empty3 = False

        self.slot1_button = bi.slot1_button
        self.slot1_button.x = 380
        self.slot1_button.y = height//2
        self.slot1_button.size = 0.65
        self.slot1_target = (0.65, 380, height//2)

        self.play1_button = bi.play1_button
        self.play1_button.x = self.slot1_button.x
        self.play1_button.y = self.slot1_button.y
        self.play1_button.size = 0
        self.play1_target = (0, self.slot1_button.x, self.slot1_button.y)

        self.slot2_button = bi.slot2_button
        self.slot2_button.x = width//2
        self.slot2_button.y = height//2
        self.slot2_button.size = 0.65
        self.slot2_target = (0.65, width//2, height//2)

        self.play2_button = bi.play2_button
        self.play2_button.x = self.slot2_button.x
        self.play2_button.y = self.slot2_button.y
        self.play2_button.size = 0
        self.play2_target = (0, self.slot2_button.x, self.slot2_button.y)

        self.slot3_button = bi.slot3_button
        self.slot3_button.x = 900
        self.slot3_button.y = height//2
        self.slot3_button.size = 0.65
        self.slot3_target = (0.65, 900, height//2)

        self.play3_button = bi.play3_button
        self.play3_button.x = self.slot3_button.x
        self.play3_button.y = self.slot3_button.y
        self.play3_button.size = 0
        self.play3_target = (0, self.slot3_button.x, self.slot3_button.y)

        self.tint_surface = pygame.Surface((width, height))
        self.tint_surface.set_alpha(128)
        self.tint_surface.fill((0, 0, 0))
        self.del_true = False
        self.onbutton = 0
        self.warn_text = None
        self.save_num = 0
        self.cursor = CustomCursor()

    def run(self):

        current_time = pygame.time.get_ticks()

        pos = pygame.mouse.get_pos()

        save1check = os.path.isfile("saves/save1.txt")
        save2check = os.path.isfile("saves/save2.txt")
        save3check = os.path.isfile("saves/save3.txt")

        self.bg_x, self.bg_y = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.bg_y, self.scroll_speed)

        a.textframe_rect.center = width//2, height//2
        self.display.blit(a.textframe, a.textframe_rect)

        s1_button_clicked = self.slot1_button.draw(self.display)
        s2_button_clicked = self.slot2_button.draw(self.display)
        s3_button_clicked = self.slot3_button.draw(self.display)

        p1_button_clicked = self.play1_button.draw(self.display)
        p2_button_clicked = self.play2_button.draw(self.display)
        p3_button_clicked = self.play3_button.draw(self.display)

        if self.play1_button in self.buttons:
            self.buttons.remove(self.play1_button)
        if self.play2_button in self.buttons:
            self.buttons.remove(self.play2_button)
        if self.play3_button in self.buttons:
            self.buttons.remove(self.play3_button)

        if self.slot1_button in self.buttons:
            self.buttons.remove(self.slot1_button)
        if self.slot2_button in self.buttons:
            self.buttons.remove(self.slot2_button)
        if self.slot3_button in self.buttons:
            self.buttons.remove(self.slot3_button)
 
        if save1check:
            self.slot1_button.change_image(a.slot1_img, a.slot1down_img)
            if not self.confirm:
                if self.slot1_button not in self.buttons:
                    self.buttons.append(self.slot1_button)
                if s1_button_clicked and self.onbutton is 0:
                    self.onbutton = 1
                    self.button_click_time = current_time
                if self.onbutton is 1 and p1_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.load = True
                        self.confirm = True
                        self.save_num = 1
                if self.slot1_button.rect.collidepoint(pos) is False and self.onbutton is 1:
                    self.onbutton = 0
        else:
            if not self.confirm:
                if self.slot1_button in self.buttons:
                    self.buttons.remove(self.slot1_button)
                self.slot1_button.change_image(a.emptyslot1down_img, a.emptyslot1down_img)
                if s1_button_clicked and self.onbutton is 0:
                    pass

        if save2check:
            self.slot2_button.change_image(a.slot2_img, a.slot2down_img)
            if not self.confirm:
                if self.slot2_button not in self.buttons:
                    self.buttons.append(self.slot2_button)
                if s2_button_clicked and self.onbutton is 0:
                    if self.slot2_button in self.buttons:
                        self.buttons.remove(self.slot2_button)
                    self.onbutton = 2
                    self.button_click_time = current_time
                elif self.onbutton is 2 and p2_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.load = True
                        self.confirm = True
                        self.save_num = 2
                elif self.slot2_button.rect.collidepoint(pos) is False and self.onbutton is 2:
                    self.onbutton = 0
        else:
            if not self.confirm:
                if self.slot2_button in self.buttons:
                    self.buttons.remove(self.slot2_button)
                self.slot2_button.change_image(a.emptyslot2down_img, a.emptyslot2down_img)
                if s2_button_clicked and self.onbutton is 0:
                    pass

        if save3check:
            self.slot3_button.change_image(a.slot3_img, a.slot3down_img)
            if not self.confirm:
                if self.slot3_button not in self.buttons:
                    self.buttons.append(self.slot3_button)                
                if s3_button_clicked and self.onbutton is 0:
                    if self.slot3_button in self.buttons:
                        self.buttons.remove(self.slot3_button)
                    self.onbutton = 3
                    self.button_click_time = current_time
                elif self.onbutton is 3 and p3_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.load = True
                        self.confirm = True
                        self.save_num = 3
                elif self.slot3_button.rect.collidepoint(pos) is False and self.onbutton is 3:
                    self.onbutton = 0
        else:
            if not self.confirm:
                if self.slot3_button in self.buttons:
                    self.buttons.remove(self.slot3_button)
                self.slot3_button.change_image(a.emptyslot3down_img, a.emptyslot3down_img)
                if s3_button_clicked and self.onbutton is 0:
                    pass

        if self.onbutton == 1:
            self.play1_target = (0.2, width//2, height//2)
            self.slot1_target = (1.2, width//2, height//2)
            self.slot2_target = (0.1, width//2, 550)
            self.slot3_target = (0.1, 900, 170)
        elif self.onbutton == 2:
            self.slot1_target = (0.1, 380, 170)
            self.play2_target = (0.2, width//2, height//2)
            self.slot2_target = (1.2, width//2, height//2)
            self.slot3_target = (0.1, 900, 550)
        elif self.onbutton == 3:
            self.slot1_target = (0.1, 380, 550)
            self.slot2_target = (0.1, width//2, 170)
            self.play3_target = (0.2, width//2, height//2)
            self.slot3_target = (1.2, width//2, height//2)
        elif self.onbutton == 0:
            self.slot1_target = (0.65, 380, height//2)
            self.play1_target = (0, 380, height//2)
            self.slot2_target = (0.65, width//2, height//2)
            self.play2_target = (0, width//2, height//2)
            self.slot3_target = (0.65, 900, height//2)
            self.play3_target = (0, 900, height//2)

        self.update_button(self.slot1_button, self.slot1_target)
        self.update_button(self.slot2_button, self.slot2_target)
        self.update_button(self.slot3_button, self.slot3_target)

        self.update_button(self.play1_button, self.play1_target)
        self.update_button(self.play2_button, self.play2_target)
        self.update_button(self.play3_button, self.play3_target)

        if self.confirm:
            self.display.blit(self.tint_surface,(0, 0))
            a.textframe_rect.center = width // 2, 720 // 2
            self.display.blit(a.textframe, a.textframe_rect)
            text.draw_text(f"are you sure\nyou want to load\nsave number {self.save_num}?", (0, 0, 0), width//2, height//2.5, 36, self.display)
            if bi.confirm_button.draw(self.display):
                Load(f"save{self.save_num}")
                self.gameStateManager.set_state("categorymenu")
                self.confirm = False
                self.del_done = True
                self.onbutton = 0
                fade(self.display)
            if bi.unconfirm_button.draw(self.display):
                self.onbutton = 0
                self.confirm = False
            self.buttons.clear()
            self.buttons.extend({bi.confirm_button, bi.unconfirm_button})

        if not self.confirm:
            if bi.back_button.draw(self.display):
                self.gameStateManager.set_state("mainmenu")
                fade(self.display)

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

        if self.gameStateManager.get_state() is not "loads" or self.del_true == True:
            self.fade_alpha = 255
            self.del_true = False
        if self.gameStateManager.get_state() is not "loads":
            self.onbutton = 0
            self.confirm = False

    def update_button(self, button, target, speed=0.1):
        size, x, y = target
        button.size = self.lerp(button.size, size, speed)
        button.x = self.lerp(button.x, x, speed)
        button.y = self.lerp(button.y, y, speed)
        button.update()

    def lerp(self, start, end, t):
        return start + t * (end - start)