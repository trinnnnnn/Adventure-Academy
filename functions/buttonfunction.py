import pygame
import assets.assets as a

class Button:
    def __init__(self, x, y, imagedefault, imageclicked, scale):
        self.imagedefault = imagedefault
        self.imageclicked = imageclicked
        self.scale = scale

        self.image = pygame.transform.scale(imagedefault, (int(imagedefault.get_width() * scale), int(imagedefault.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hovered = False
        self.mouse_down = False
        self.x = x
        self.y = y
        self.size = scale
        self.disabled = False
        self.sound_played = False

    def draw(self, screen, locked=False):
        action = False
        pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        previously_hovered = self.hovered
        self.hovered = self.rect.collidepoint(pos)

        if self.disabled:
            self.image = pygame.transform.scale(self.imagedefault, (int(self.imagedefault.get_width() * self.size), int(self.imagedefault.get_height() * self.size)))
        else:
            if self.hovered and not previously_hovered and not locked:
                pygame.mixer.Sound.play(a.button_hover)
                self.sound_played = True

            if self.hovered and not locked:
                self.image = pygame.transform.scale(self.imageclicked, (int(self.imageclicked.get_width() * self.size), int(self.imageclicked.get_height() * self.size)))

                if mouse_pressed and not self.mouse_down:
                    pygame.mixer.Sound.play(a.button_click)
                    action = True
            else:
                self.image = pygame.transform.scale(self.imagedefault, (int(self.imagedefault.get_width() * self.size), int(self.imagedefault.get_height() * self.size)))

            self.mouse_down = mouse_pressed

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

    def update(self):
        self.image = pygame.transform.scale(self.imagedefault, (int(self.imagedefault.get_width() * self.size), int(self.imagedefault.get_height() * self.size)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def change_image(self, imagedefault, imageclicked):
        self.imagedefault = imagedefault
        self.imageclicked = imageclicked
        self.image = pygame.transform.scale(imagedefault, (int(imagedefault.get_width() * self.size), int(imagedefault.get_height() * self.size)))

class CursorChanger:
    def change_cursor(cursor, buttons):
        mouse = pygame.mouse.get_pos()
        cursor_on_button = any(button.rect.collidepoint(mouse) for button in buttons)
        cursor.set_hover(cursor_on_button)
