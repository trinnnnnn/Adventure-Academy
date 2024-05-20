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

class Loadsave:
    def __init__(self, display, gameStateManager):
        # Initialize the display and game state
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = [bi.power_button, bi.back_button]
        self.bg_x = 0
        self.scroll_speed = 0.6
        self.fade_alpha = 255
        self.confirm = False
        self.onbutton = 0
        self.empty1 = False
        self.empty2 = False
        self.empty3 = False
        self.s1_img = a.slot1_img
        self.s1_img2 = self.s1_img
        self.s2_img = a.slot2_img
        self.s2_img2 = self.s2_img
        self.s3_img = a.slot3_img
        self.s3_img2 = self.s3_img
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
        
    def run(self):

        save1check = os.path.isfile("saves/save1.txt")
        save2check = os.path.isfile("saves/save2.txt")
        save3check = os.path.isfile("saves/save3.txt")

        self.bg_x = scroll_bg(self.display, a.unscroll_bg, self.bg_x, self.scroll_speed)

        # Draw the scrolling background
        self.display.blit(a.unscroll_bg, (self.bg_x - width, 0))
        self.display.blit(a.unscroll_bg, (self.bg_x, 0))

        a.textframe_rect.center = width//2, height//2
        self.display.blit(a.textframe, a.textframe_rect)

        if self.gameStateManager.get_theme() == "load":

            pos = pygame.mouse.get_pos()

            if self.delete1_button in self.buttons:
                self.buttons.remove(self.delete1_button)
            if self.delete2_button in self.buttons:
                self.buttons.remove(self.delete2_button)
            if self.delete3_button in self.buttons:
                self.buttons.remove(self.delete3_button)

            if self.onbutton == 1:
                self.p1_target_size = 0.2
                self.s1_target_size = 1.2
                self.s1_target_x = width//2
                self.s1_target_y = height//2
                self.p2_target_size = 0
                self.s2_target_size = 0.1
                self.s2_target_y = 550
                self.p3_target_size = 0
                self.s3_target_size = 0.1
                self.s3_target_y = 170
            elif self.onbutton == 2:
                self.p1_target_size = 0
                self.s1_target_size = 0.1
                self.s1_target_y = 170
                self.p2_target_size = 0.2
                self.s2_target_size = 1.2
                self.p3_target_size = 0
                self.s3_target_size = 0.1
                self.s3_target_y = 550
            elif self.onbutton == 3:
                self.p1_target_size = 0
                self.s1_target_size = 0.1
                self.s1_target_y = 550
                self.p2_target_size = 0
                self.s2_target_size = 0.1
                self.s2_target_y = 170
                self.p3_target_size = 0.2
                self.s3_target_size = 1.2
                self.s3_target_x = width//2
            else:
                self.p1_target_size = 0
                self.s1_target_size = 0.65
                self.s1_target_x = 380
                self.s1_target_y = height//2
                self.p2_target_size = 0
                self.s2_target_size = 0.65
                self.s2_target_x = width//2
                self.s2_target_y = height//2
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
            
            self.s1_button = bf.Button(self.s1_x, self.s1_y, self.s1_img, self.s1_img2, self.s1_size)
            self.s2_button = bf.Button(self.s2_x, self.s2_y, self.s2_img, self.s2_img2, self.s2_size)
            self.s3_button = bf.Button(self.s3_x, self.s3_y, self.s3_img, self.s3_img2, self.s3_size)
            self.play1_button = bf.Button(self.s1_x, self.s1_y, a.play1_img, a.play1down_img, self.p1_size)
            self.play2_button = bf.Button(self.s2_x, self.s2_y, a.play2_img, a.play2down_img, self.p2_size)
            self.play3_button = bf.Button(self.s3_x, self.s3_y, a.play3_img, a.play3down_img, self.p3_size)

            if self.s1_button.rect.collidepoint(pos):
                self.onbutton = 1
            elif self.s2_button.rect.collidepoint(pos):
                self.onbutton = 2
            elif self.s3_button.rect.collidepoint(pos):
                self.onbutton = 3
            else:
                self.onbutton = 0

            if bi.back_button.draw(self.display):
                self.gameStateManager.set_state("mainmenu")
                fade(self.display)
                     
            if save1check:
                self.s1_img = a.slot1_img
                self.s1_img2 = a.slot1down_img
                if self.s1_button.draw(self.display):
                    pass
                if self.play1_button.draw(self.display):
                        self.confirm = True
                        self.save_num = 1
                if self.play1_button not in self.buttons:
                    self.buttons.append(self.play1_button)
            else:
                self.s1_img = a.emptyslot1down_img
                self.s1_img2 = a.emptyslot1down_img
                if self.s1_button.draw(self.display):
                    pass
            if save2check:
                self.s2_img = a.slot2down_img
                self.s2_img2 = a.slot2down_img
                if self.s2_button.draw(self.display):
                    pass
                if self.play2_button.draw(self.display):
                    self.confirm = True
                    self.save_num = 2
                if self.play2_button not in self.buttons:
                    self.buttons.append(self.play2_button)
            else:
                self.s2_img = a.emptyslot2down_img
                self.s2_img2 = a.emptyslot2down_img
                if self.s2_button.draw(self.display):
                    pass
            if save3check:
                self.s3_img = a.slot3down_img
                self.s3_img2 = a.slot3down_img
                if self.s3_button.draw(self.display):
                    pass
                if self.play3_button.draw(self.display):
                    self.confirm = True
                    self.save_num = 3
                if self.play3_button not in self.buttons:
                    self.buttons.append(self.play3_button)
            else:
                self.s3_img = a.emptyslot3down_img
                self.s3_img2 = a.emptyslot3down_img
                if self.s3_button.draw(self.display):
                    pass

            if self.confirm:
                self.display.blit(self.tint_surface,(0, 0))
                a.textframe_rect.center = width // 2, 720 // 2
                self.display.blit(a.textframe, a.textframe_rect)
                text.draw_text(f"are you sure\nyou want to load\nsave number {self.save_num}?", (0, 0, 0), width//2, height//2.5, 36, self.display)
                if bi.confirm_button.draw(self.display):
                    Load(f"save{self.save_num}")
                    self.confirm = False
                    self.del_done = True
                    self.gameStateManager.set_state("categorymenu")
                    fade(self.display)
                if bi.unconfirm_button.draw(self.display):
                    self.confirm = False 

        if self.gameStateManager.get_theme() == "save":

            if bi.back_button.draw(self.display):
                self.gameStateManager.set_state("categorymenu")
                fade(self.display)

            if self.delete1_button in self.buttons:
                self.buttons.remove(self.delete1_button)
            if self.delete2_button in self.buttons:
                self.buttons.remove(self.delete2_button)
            if self.delete3_button in self.buttons:
                self.buttons.remove(self.delete3_button)

            pos = pygame.mouse.get_pos()
            
            if not self.confirm:  # Only check button collision if not confirming
                if self.s1_button.rect.collidepoint(pos) and not self.empty1:
                    self.onbutton = 1
                elif self.s2_button.rect.collidepoint(pos) and not self.empty2:
                    self.onbutton = 2
                elif self.s3_button.rect.collidepoint(pos) and not self.empty3:
                    self.onbutton = 3
                else:
                    self.onbutton = 0

            if self.onbutton == 1:
                self.d1_target_size = 0.2
                self.s1_target_size = 1.2
                self.s1_target_x = width//2
                self.s1_target_y = height//2
                self.d2_target_size = 0
                self.s2_target_size = 0.1
                self.s2_target_y = 550
                self.d3_target_size = 0
                self.s3_target_size = 0.1
                self.s3_target_y = 170
            elif self.onbutton == 2:
                self.d1_target_size = 0
                self.s1_target_size = 0.1
                self.s1_target_y = 170
                self.d2_target_size = 0.2
                self.s2_target_size = 1.2
                self.d3_target_size = 0
                self.s3_target_size = 0.1
                self.s3_target_y = 550
            elif self.onbutton == 3:
                self.d1_target_size = 0
                self.s1_target_size = 0.1
                self.s1_target_y = 550
                self.d2_target_size = 0
                self.s2_target_size = 0.1
                self.s2_target_y = 170
                self.d3_target_size = 0.2
                self.s3_target_size = 1.2
                self.s3_target_x = width//2
            else:
                self.d1_target_size = 0
                self.s1_target_size = 0.65
                self.s1_target_x = 380
                self.s1_target_y = height//2
                self.d2_target_size = 0
                self.s2_target_size = 0.65
                self.s2_target_x = width//2
                self.s2_target_y = height//2
                self.d3_target_size = 0
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

            self.d1_size = self.lerp(self.d1_size, self.d1_target_size, 0.1)
            self.d2_size = self.lerp(self.d2_size, self.d2_target_size, 0.1)
            self.d3_size = self.lerp(self.d3_size, self.d3_target_size, 0.1)
            
            self.s1_button = bf.Button(self.s1_x, self.s1_y, self.s1_img, self.s1_img2, self.s1_size)
            self.s2_button = bf.Button(self.s2_x, self.s2_y, self.s2_img, self.s2_img2, self.s2_size)
            self.s3_button = bf.Button(self.s3_x, self.s3_y, self.s3_img, self.s3_img2, self.s3_size)
            self.delete1_button = bf.Button(self.s1_x, self.s1_y, a.delete1_img, a.delete1down_img, self.d1_size)
            self.delete2_button = bf.Button(self.s2_x, self.s2_y, a.delete2_img, a.delete2down_img, self.d2_size)
            self.delete3_button = bf.Button(self.s3_x, self.s3_y, a.delete3_img, a.delete3down_img, self.d3_size)

            if save1check:
                self.empty1 = False
                self.s1_img = a.slot1_img
                self.s1_img2 = a.slot1down_img
                if self.s1_button.draw(self.display):
                    pass
                if self.delete1_button.draw(self.display):
                        self.confirm = True
                        self.save_num = 1
                if self.delete1_button not in self.buttons:
                    self.buttons.append(self.delete1_button)
                if self.s1_button in self.buttons:
                    self.buttons.remove(self.s1_button)
            else:
                self.empty1 = True
                self.s1_img = a.emptyslot1_img
                self.s1_img2 = a.emptyslot1down_img
                if self.s1_button.draw(self.display):
                    Save(data.userdata, "save1")
            if save2check:
                self.empty2 = False
                self.s2_img = a.slot2_img
                self.s2_img2 = a.slot2down_img
                if self.s2_button.draw(self.display):
                    pass
                if self.delete2_button.draw(self.display):
                    self.confirm = True
                    self.save_num = 2
                if self.delete2_button not in self.buttons:
                    self.buttons.append(self.delete2_button)
                if self.s2_button in self.buttons:
                    self.buttons.remove(self.s2_button)
            else:
                self.empty2 = True
                self.s2_img = a.emptyslot2_img
                self.s2_img2 = a.emptyslot2down_img
                if self.s2_button.draw(self.display):
                    Save(data.userdata, "save2")
            if save3check:
                self.empty3 = False
                self.s3_img = a.slot3_img
                self.s3_img2 = a.slot3down_img
                if self.s3_button.draw(self.display):
                    pass
                if self.delete3_button.draw(self.display):
                    self.confirm = True
                    self.save_num = 3
                if self.delete3_button not in self.buttons:
                    self.buttons.append(self.delete3_button)
                if self.s3_button in self.buttons:
                    self.buttons.remove(self.s3_button)
            else:
                self.empty3 = True
                self.s3_img = a.emptyslot3_img
                self.s3_img2 = a.emptyslot3down_img
                if self.s3_button.draw(self.display):
                    Save(data.userdata, "save3")

            if self.confirm:
                self.display.blit(self.tint_surface,(0, 0))
                a.textframe_rect.center = width // 2, 720 // 2
                self.display.blit(a.textframe, a.textframe_rect)
                text.draw_text(f"are you sure\nyou want to delete\save number {self.save_num}?", (0, 0, 0), width//2, height//2.5, 36, self.display)
                if bi.confirm_button.draw(self.display):
                    os.remove(f"saves/save{self.save_num}.txt")
                    self.confirm = False
                    self.del_done = True
                    fade(self.display)
                if bi.unconfirm_button.draw(self.display):
                    self.confirm = False    

        DefaultButtons(self.display)

        CursorChanger.change_cursor(self.buttons)

        if self.fade_alpha > 0:
            fadein(self.display, self.fade_alpha)
            self.fade_alpha -= 5

        if self.gameStateManager.get_state() != "loadsave" or self.del_true == True:
            self.fade_alpha = 255
            self.del_true = False

    def lerp(self, start, end, t):
        return start + t * (end - start)