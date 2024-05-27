from utils.window import width, height
import functions.buttoninstance as bi
import functions.buttonfunction as bf
import functions.text as text
import utils.data as data
import assets.assets as a
import os
from functions.buttonfunction import CursorChanger
from functions.saveloadmanager import *
from functions.transition import *
from utils.defaultbutton import DefaultButtons
from functions.scrollingbg import scroll_bg
from functions.customcursor import CustomCursor

class Saves:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
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
        self.s1_img = a.slot1_img
        self.s1_img2 = a.slot1down_img
        self.s2_img = a.slot2_img
        self.s2_img2 = a.slot2down_img
        self.s3_img = a.slot3_img
        self.s3_img2 = a.slot3down_img
        self.s1_button = bi.slot1_button
        self.s2_button = bi.slot2_button
        self.s3_button = bi.slot3_button
        self.delete1_button = bi.delete1_button
        self.delete2_button = bi.delete2_button
        self.delete3_button = bi.delete3_button
        self.play1_button = bi.play1_button
        self.play2_button = bi.play2_button
        self.play3_button = bi.play3_button
        self.d1_size = 0
        self.d2_size = 0
        self.d3_size = 0
        self.p1_size = 0
        self.p2_size = 0
        self.p3_size = 0
        self.s1_size = 0.65
        self.s2_size = 0.65
        self.s3_size = 0.65
        self.s1_x = 380
        self.s2_x = width//2
        self.s3_x = 900
        self.s1_y = height//2
        self.s2_y = height//2
        self.s3_y = height//2
        self.s1_target_size = self.s1_size
        self.s2_target_size = self.s2_size
        self.s3_target_size = self.s3_size
        self.d1_target_size = self.d1_size
        self.d2_target_size = self.d2_size
        self.d3_target_size = self.d3_size
        self.p1_target_size = self.p1_size
        self.p2_target_size = self.p2_size
        self.p3_target_size = self.p3_size
        self.s1_target_x = self.s1_x
        self.s2_target_x = self.s2_x
        self.s3_target_x = self.s3_x
        self.s1_target_y = self.s1_y
        self.s2_target_y = self.s2_y
        self.s3_target_y = self.s3_y
        self.tint_surface = pygame.Surface((width, height))
        self.tint_surface.set_alpha(128)
        self.tint_surface.fill((0, 0, 0))
        self.del_true = False
        self.onbutton = 0
        self.prev_state = None
        self.warn_text = None
        self.save_num = 0
        self.load = False
        self.delete = False
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

        if self.onbutton is 1:
            self.s1_target_size = 1.2
            self.s1_target_x = width//2
            self.s1_target_y = height//2
            self.s2_target_size = 0.1
            self.s2_target_y = 550
            self.s3_target_size = 0.1
            self.s3_target_y = 170
            if save1check:
                self.p1_target_size = 0.2
                self.d1_target_size = 0.2
                self.d2_target_size = 0
                self.d3_target_size = 0
        elif self.onbutton is 2:
            self.s1_target_size = 0.1
            self.s1_target_y = 170
            self.s2_target_size = 1.2
            self.s3_target_size = 0.1
            self.s3_target_y = 550
            if save2check:
                self.d1_target_size = 0
                self.d2_target_size = 0.2
                self.d3_target_size = 0
                self.p2_target_size = 0.2
        elif self.onbutton is 3:
            self.s1_target_size = 0.1
            self.s1_target_y = 550
            self.s2_target_size = 0.1
            self.s2_target_y = 170
            self.s3_target_size = 1.2
            self.s3_target_x = width//2
            if save3check:
                self.d1_target_size = 0
                self.d2_target_size = 0
                self.d3_target_size = 0.2
                self.p3_target_size = 0.2
        else:
            self.d1_target_size = 0
            self.p1_target_size = 0
            self.s1_target_size = 0.65
            self.s1_target_x = 380
            self.s1_target_y = height//2
            self.d2_target_size = 0
            self.p2_target_size = 0
            self.s2_target_size = 0.65
            self.s2_target_x = width//2
            self.s2_target_y = height//2
            self.d3_target_size = 0
            self.p3_target_size = 0
            self.s3_target_size = 0.65
            self.s3_target_x = 900
            self.s3_target_y = height//2

        self.s1_size = self.lerp(self.s1_size, self.s1_target_size, 0.1)
        self.s1_x = self.lerp(self.s1_x, self.s1_target_x, 0.1)
        self.s1_y = self.lerp(self.s1_y, self.s1_target_y, 0.1)

        self.s2_size = self.lerp(self.s2_size, self.s2_target_size, 0.1)
        self.s2_x = self.lerp(self.s2_x, self.s2_target_x, 0.1)
        self.s2_y = self.lerp(self.s2_y, self.s2_target_y, 0.1)

        self.s3_size = self.lerp(self.s3_size, self.s3_target_size, 0.1)
        self.s3_x = self.lerp(self.s3_x, self.s3_target_x, 0.1)
        self.s3_y = self.lerp(self.s3_y, self.s3_target_y, 0.1)

        self.p1_size = self.lerp(self.p1_size, self.p1_target_size, 0.1)
        self.p2_size = self.lerp(self.p2_size, self.p2_target_size, 0.1)
        self.p3_size = self.lerp(self.p3_size, self.p3_target_size, 0.1)

        self.d1_size = self.lerp(self.d1_size, self.d1_target_size, 0.1)
        self.d2_size = self.lerp(self.d2_size, self.d2_target_size, 0.1)
        self.d3_size = self.lerp(self.d3_size, self.d3_target_size, 0.1)
        
        self.s1_button = bf.Button(self.s1_x, self.s1_y, self.s1_img, self.s1_img2, self.s1_size)
        self.s2_button = bf.Button(self.s2_x, self.s2_y, self.s2_img, self.s2_img2, self.s2_size)
        self.s3_button = bf.Button(self.s3_x, self.s3_y, self.s3_img, self.s3_img2, self.s3_size)
        self.play1_button = bf.Button(self.s1_x - 60, self.s1_y, a.play1_img, a.play1down_img, self.p1_size)
        self.play2_button = bf.Button(self.s2_x - 60, self.s2_y, a.play2_img, a.play2down_img, self.p2_size)
        self.play3_button = bf.Button(self.s3_x - 60, self.s3_y, a.play3_img, a.play3down_img, self.p3_size)
        self.delete1_button = bf.Button(self.s1_x + 60, self.s1_y, a.delete1_img, a.delete1down_img, self.d1_size)
        self.delete2_button = bf.Button(self.s2_x + 60, self.s2_y, a.delete2_img, a.delete2down_img, self.d2_size)
        self.delete3_button = bf.Button(self.s3_x + 60, self.s3_y, a.delete3_img, a.delete3down_img, self.d3_size)


        if self.play1_button in self.buttons:
            self.buttons.remove(self.play1_button)
        if self.play2_button in self.buttons:
            self.buttons.remove(self.play2_button)
        if self.play3_button in self.buttons:
            self.buttons.remove(self.play3_button)

        if self.s1_button in self.buttons:
            self.buttons.remove(self.s1_button)
        if self.s2_button in self.buttons:
            self.buttons.remove(self.s2_button)
        if self.s3_button in self.buttons:
            self.buttons.remove(self.s3_button)

        s1_button_clicked = self.s1_button.draw(self.display)
        s2_button_clicked = self.s2_button.draw(self.display)
        s3_button_clicked = self.s3_button.draw(self.display)

        p1_button_clicked = self.play1_button.draw(self.display)
        p2_button_clicked = self.play2_button.draw(self.display)
        p3_button_clicked = self.play3_button.draw(self.display)

        d1_button_clicked = self.delete1_button.draw(self.display)
        d2_button_clicked = self.delete2_button.draw(self.display)
        d3_button_clicked = self.delete3_button.draw(self.display)

        if save1check:
            self.s1_img = a.slot1_img
            self.s1_img2 = a.slot1down_img
            if not self.confirm:
                if self.s1_button not in self.buttons:
                    self.buttons.append(self.s1_button)
                if s1_button_clicked and self.onbutton is 0:
                    self.onbutton = 1
                    self.button_click_time = current_time
                if self.onbutton is 1 and d1_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.delete = True
                        self.confirm = True
                        self.save_num = 1
                elif self.onbutton is 1 and p1_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.confirm = True
                        self.load = True
                        self.save_num = 1
                if self.s1_button.rect.collidepoint(pos) is False and self.onbutton is 1:
                    self.onbutton = 0

        else:
            if not self.confirm:
                if self.s1_button in self.buttons:
                    self.buttons.remove(self.s1_button)
                self.s1_img = a.emptyslot1_img
                self.s1_img2 = a.emptyslot1down_img
                if s1_button_clicked and self.onbutton is 0:
                    self.onbutton = 1
                    self.button_click_time = current_time
                if self.onbutton is 1 and s1_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        Save(data.userdata, "save1")
                if self.s1_button.rect.collidepoint(pos) is False and self.onbutton is 1:
                    self.onbutton = 0


        if save2check:
            self.s2_img = a.slot2_img
            self.s2_img2 = a.slot2down_img
            if not self.confirm:
                if self.s2_button not in self.buttons:
                    self.buttons.append(self.s2_button)
                if s2_button_clicked and self.onbutton is 0:
                    if self.s2_button in self.buttons:
                        self.buttons.remove(self.s2_button)
                    self.onbutton = 2
                    self.button_click_time = current_time
                elif self.onbutton is 2 and d2_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.delete = True
                        self.confirm = True
                        self.save_num = 2
                elif self.onbutton is 2 and p2_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.confirm = True
                        self.load = True
                        self.save_num = 2
                elif self.s2_button.rect.collidepoint(pos) is False and self.onbutton is 2:
                    self.onbutton = 0
        else:
            if not self.confirm:
                if self.s2_button in self.buttons:
                    self.buttons.remove(self.s2_button)
                self.s2_img = a.emptyslot2_img
                self.s2_img2 = a.emptyslot2down_img
                if s2_button_clicked and self.onbutton is 0:
                    if self.s2_button in self.buttons:
                        self.buttons.remove(self.s2_button)
                    self.onbutton = 2
                    self.button_click_time = current_time
                elif self.onbutton is 2 and s2_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        Save(data.userdata, "save2")
                elif self.s2_button.rect.collidepoint(pos) is False and self.onbutton is 2:
                    self.onbutton = 0

        if save3check:
            self.s3_img = a.slot3_img
            self.s3_img2 = a.slot3down_img
            if not self.confirm:
                if self.s3_button not in self.buttons:
                    self.buttons.append(self.s3_button)
                if s3_button_clicked and self.onbutton is 0:
                    if self.s3_button in self.buttons:
                        self.buttons.remove(self.s3_button)
                    self.onbutton = 3
                    self.button_click_time = current_time
                elif self.onbutton is 3 and d3_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.delete = True
                        self.confirm = True
                        self.save_num = 3
                elif self.onbutton is 3 and p3_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        self.confirm = True
                        self.load = True
                        self.save_num = 3
                elif self.s3_button.rect.collidepoint(pos) is False and self.onbutton is 3:
                    self.onbutton = 0
        else:
            if not self.confirm:
                if self.s3_button in self.buttons:
                    self.buttons.remove(self.s3_button)
                self.s3_img = a.emptyslot3_img
                self.s3_img2 = a.emptyslot3down_img
                if s3_button_clicked and self.onbutton is 0:
                    if self.s3_button in self.buttons:
                        self.buttons.remove(self.s3_button)
                    self.onbutton = 3
                    self.button_click_time = current_time
                elif self.onbutton is 3 and s3_button_clicked:
                    if current_time - self.button_click_time >= 200:
                        Save(data.userdata, "save3")
                        self.onbutton = 0
                elif self.s3_button.rect.collidepoint(pos) is False and self.onbutton is 3:
                    self.onbutton = 0
        
        if self.confirm:
            if self.delete:
                self.warn_text = f"are you sure\nyou want to delete\nsave number {self.save_num}?"
            if self.load:
                self.warn_text = f"are you sure\nyou want to load\nsave number {self.save_num}?"
            self.display.blit(self.tint_surface,(0, 0))
            a.textframe_rect.center = width // 2, 720 // 2
            self.display.blit(a.textframe, a.textframe_rect)
            text.draw_text(self.warn_text, (0, 0, 0), width//2, height//2.5, 36, self.display)
            if bi.confirm_button.draw(self.display):
                if self.delete:
                    os.remove(f"saves/save{self.save_num}.txt")
                elif self.load:
                    Load(f"save{self.save_num}")
                    self.gameStateManager.set_state("categorymenu")
                self.confirm = False
                self.delete = False
                self.load = False
                self.onbutton = 0
                fade(self.display)
            if bi.unconfirm_button.draw(self.display):
                self.onbutton = 0
                self.confirm = False
                self.delete = False
                self.load = False
            self.buttons.clear()
            self.buttons.extend({bi.confirm_button, bi.unconfirm_button})

            if not self.confirm:
                if bi.back_button.draw(self.display):
                    self.gameStateManager.set_state(self.prev_state)
                    fade(self.display)

        DefaultButtons(self.display)

        self.cursor.update()
        CursorChanger.change_cursor(self.cursor, self.buttons)
        self.cursor.draw()

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() is not "saves" or self.del_true == True:
            self.fade_alpha = 255
            self.del_true = False
        if self.gameStateManager.get_state() is not "saves":
            self.onbutton = 0
            self.confirm = False

    def lerp(self, start, end, t):
        return start + t * (end - start)