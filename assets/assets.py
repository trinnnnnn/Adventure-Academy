import pygame
import pygame.locals

#bg
unscroll_bg = pygame.image.load("assets/images/bg/bg.jpg")

#buttons
start_img = pygame.image.load("assets/images/buttons/placeholder_button.png").convert_alpha()
startdown_img = pygame.image.load("assets/images/buttons/placeholder_buttondown.png").convert_alpha()
confirm_img = pygame.image.load("assets/images/buttons/confirm.png").convert_alpha()
confirmdown_img = pygame.image.load("assets/images/buttons/confirmdown.png").convert_alpha()
unconfirm_img = pygame.image.load("assets/images/buttons/x.png").convert_alpha()
unconfirmdown_img = pygame.image.load("assets/images/buttons/xdown.png").convert_alpha()
shapes_img = pygame.image.load("assets/images/buttons/shapes.png").convert_alpha()
shapesdown_img = pygame.image.load("assets/images/buttons/shapesdown.png").convert_alpha()
colours_img = pygame.image.load("assets/images/buttons/colours.png").convert_alpha()
coloursdown_img = pygame.image.load("assets/images/buttons/coloursdown.png").convert_alpha()
alphabet_img = pygame.image.load("assets/images/buttons/alphabet.png").convert_alpha()
alphabetdown_img = pygame.image.load("assets/images/buttons/alphabetdown.png").convert_alpha()
power_img = pygame.image.load("assets/images/buttons/power.png").convert_alpha()
powerdown_img = pygame.image.load("assets/images/buttons/powerdown.png").convert_alpha()
emptyslot1_img = pygame.image.load("assets/images/buttons/emptyslot1.png").convert_alpha()
emptyslot1down_img = pygame.image.load("assets/images/buttons/emptyslot1down.png").convert_alpha()
emptyslot2_img = pygame.image.load("assets/images/buttons/emptyslot2.png").convert_alpha()
emptyslot2down_img = pygame.image.load("assets/images/buttons/emptyslot2down.png").convert_alpha()
emptyslot3_img = pygame.image.load("assets/images/buttons/emptyslot3.png").convert_alpha()
emptyslot3down_img = pygame.image.load("assets/images/buttons/emptyslot3down.png").convert_alpha()
slot1_img = pygame.image.load("assets/images/buttons/slot1.png").convert_alpha()
slot1down_img = pygame.image.load("assets/images/buttons/slot1down.png").convert_alpha()
slot2_img = pygame.image.load("assets/images/buttons/slot2.png").convert_alpha()
slot2down_img = pygame.image.load("assets/images/buttons/slot2down.png").convert_alpha()
slot3_img = pygame.image.load("assets/images/buttons/slot3.png").convert_alpha()
slot3down_img = pygame.image.load("assets/images/buttons/slot3down.png").convert_alpha()

#shapes
circle_img = pygame.image.load("assets/images/shapes/circleplaceholder.png").convert_alpha()

#utility
textframe_original = pygame.image.load("assets/images/util/textframe.png").convert_alpha()

#utility scaling
textframe = pygame.transform.scale(textframe_original, (int(textframe_original.get_width() * 0.33), int(textframe_original.get_height() * 0.33))).convert_alpha()
textframe_rect = textframe.get_rect()
textframe2 = pygame.transform.scale(textframe_original, (int(textframe_original.get_width() * 0.34), int(textframe_original.get_height() * 0.23))).convert_alpha()
textframe2_rect = textframe2.get_rect()
scaleemptyslot1 = pygame.transform.scale(emptyslot1down_img, (int(emptyslot1down_img.get_width() * 0.65), int(emptyslot1down_img.get_height() * 0.65))).convert_alpha()
scaleemptyslot1_rect = scaleemptyslot1.get_rect()
scaleemptyslot2 = pygame.transform.scale(emptyslot2down_img, (int(emptyslot2down_img.get_width() * 0.65), int(emptyslot2down_img.get_height() * 0.65))).convert_alpha()
scaleemptyslot2_rect = scaleemptyslot2.get_rect()
scaleemptyslot3 = pygame.transform.scale(emptyslot3down_img, (int(emptyslot3down_img.get_width() * 0.65), int(emptyslot3down_img.get_height() * 0.65))).convert_alpha()
scaleemptyslot3_rect = scaleemptyslot3.get_rect()