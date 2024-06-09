import pygame

class Button:
    def __init__(self, x, y, imagedefault, imageclicked, scale):
        self.imagedefault = imagedefault
        self.imageclicked = imageclicked
        self.scale = scale

        self.image = pygame.transform.scale(imagedefault, (int(imagedefault.get_width() * scale), int(imagedefault.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.x = x
        self.y = y
        self.size = scale

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            self.image = pygame.transform.scale(self.imagedefault, (int(self.imagedefault.get_width() * self.size), int(self.imagedefault.get_height() * self.size)))

        if self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(self.imageclicked, (int(self.imageclicked.get_width() * self.size), int(self.imageclicked.get_height() * self.size)))
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True

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
    @staticmethod
    def change_cursor(cursor, buttons):
        mouse = pygame.mouse.get_pos()
        cursor_on_button = any(button.rect.collidepoint(mouse) for button in buttons)
        cursor.set_hover(cursor_on_button)
