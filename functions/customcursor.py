import pygame

class CustomCursor:
    def __init__(self):
        pygame.mouse.set_visible(False)
        self.default_spr = pygame.transform.scale(pygame.image.load("assets/images/cursor/arrow.png"), (32, 32))
        self.hover_spr = pygame.transform.scale(pygame.image.load("assets/images/cursor/hand.png"), (32, 32))
        self.spr = self.default_spr
        self.root = pygame.display.get_surface()
        self.x = 0
        self.y = 0

    def draw(self):
        self.root.blit(self.spr, (self.x, self.y))

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()

    def set_hover(self, is_hover):
        self.spr = self.hover_spr if is_hover else self.default_spr
