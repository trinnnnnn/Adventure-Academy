# import pygame module and button click sound module
import pygame

# button class definition
class Button():
    def __init__(self, x, y, imagedefault, imageclicked, scale):
        # set dimensions of the button images
        width = imageclicked.get_width()
        height = imageclicked.get_height()

        # scale button images
        self.imagedefault = pygame.transform.scale(imagedefault, (int(width * scale), int(height * scale)))
        self.imageclicked = pygame.transform.scale(imageclicked, (int(width * scale), int(height * scale)))

        # initialize button state and position
        self.image = self.imagedefault
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, screen, sound=True):
        action = False
        pos = pygame.mouse.get_pos()

        # Ensure button state is reset when not clicked
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            self.image = self.imagedefault

        # Handle button click
        if self.rect.collidepoint(pos):
            self.image = self.imageclicked
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                if sound:
                    pass  # Play button click sound
                action = True
                self.clicked = True
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

# cursor changer class definition
class CursorChanger():

    # change cursor function
    def change_cursor(buttons, screen):
        # get position of mouse and check if cursor is on the button or not
        mouse = pygame.mouse.get_pos()
        cursor_on_button = any(button.rect.collidepoint(mouse) for button in buttons)

        # change cursor to hand if on button, arrow if off button
        if cursor_on_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)