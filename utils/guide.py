import pygame
import assets.assets as a
import functions.buttoninstance as bi
import utils.data as data
from utils.window import *
from functions.text import draw_text

guide = False
page = 1
scale = 0.7
button_storage = []

tint_surface = pygame.Surface((width, height))
tint_surface.set_alpha(128)
tint_surface.fill((0, 0, 0))

def button_disable(buttons):
    for button in buttons:
        if button not in [bi.close_button, bi.gleft_arrow, bi.gright_arrow]:
            button.disabled = True
            button_storage.append(button)

def Guide(display, buttons, state):
    global guide, page

    if not guide:
        if bi.guide_button not in buttons:
            buttons.append(bi.guide_button)
        for button in buttons:
            button.disabled = False
        button_storage.clear()
        if bi.guide_button.draw(display):
            guide = True

    if guide:
        button_disable(buttons)
        buttons.clear()
        buttons.append(bi.close_button)

        display.blit(tint_surface, (0, 0))
        
        a.settingsbox_rect.center = width // 2, height // 2
        display.blit(a.settingsbox, a.settingsbox_rect)
        
        a.guidetext_rect.center = width // 2, 140
        display.blit(a.guidetext, a.guidetext_rect)

        if state == "shapes":
            if page == 1:
                circle_resized = pygame.transform.scale(data.shapes["circle"], (int(data.shapes["circle"].get_width() * scale), int(data.shapes["circle"].get_height() * scale)))
                circle_rect = circle_resized.get_rect(center=(900, 215))
                display.blit(circle_resized, circle_rect)
                draw_text("circle", (255, 255, 255), 520, 215, 45, display, shadow=True, outline=True, outline_width=3)

                square_resized = pygame.transform.scale(data.shapes["square"], (int(data.shapes["square"].get_width() * scale), int(data.shapes["square"].get_height() * scale)))
                square_rect = square_resized.get_rect(center=(900, 315))
                display.blit(square_resized, square_rect)
                draw_text("square", (255, 255, 255), 520, 315, 45, display, shadow=True, outline=True, outline_width=3)

                rectangle_resized = pygame.transform.scale(data.shapes["rectangle"], (int(data.shapes["rectangle"].get_width() * scale), int(data.shapes["rectangle"].get_height() * scale)))
                rectangle_rect = rectangle_resized.get_rect(center=(900, 415))
                display.blit(rectangle_resized, rectangle_rect)
                draw_text("rectangle", (255, 255, 255), 520, 415, 45, display, shadow=True, outline=True, outline_width=3)

                star_resized = pygame.transform.scale(data.shapes["star"], (int(data.shapes["star"].get_width() * scale), int(data.shapes["star"].get_height() * scale)))
                star_rect = star_resized.get_rect(center=(900, 515))
                display.blit(star_resized, star_rect)
                draw_text("star", (255, 255, 255), 520, 515, 45, display, shadow=True, outline=True, outline_width=3)

                if bi.gright_arrow not in buttons:
                    buttons.append(bi.gright_arrow)
                if bi.gleft_arrow in buttons:
                    buttons.remove(bi.gleft_arrow)
                if bi.gright_arrow.draw(display):
                    page = 2

            if page == 2:
                diamond_resized = pygame.transform.scale(data.shapes["diamond"], (int(data.shapes["diamond"].get_width() * scale), int(data.shapes["diamond"].get_height() * scale)))
                diamond_rect = diamond_resized.get_rect(center=(900, 215))
                display.blit(diamond_resized, diamond_rect)
                draw_text("diamond", (255, 255, 255), 520, 215, 45, display, shadow=True, outline=True, outline_width=3)

                triangle_resized = pygame.transform.scale(data.shapes["triangle"], (int(data.shapes["triangle"].get_width() * scale), int(data.shapes["triangle"].get_height() * scale)))
                triangle_rect = triangle_resized.get_rect(center=(900, 315))
                display.blit(triangle_resized, triangle_rect)
                draw_text("triangle", (255, 255, 255), 520, 315, 45, display, shadow=True, outline=True, outline_width=3)

                pentagon_resized = pygame.transform.scale(data.shapes["pentagon"], (int(data.shapes["pentagon"].get_width() * scale), int(data.shapes["pentagon"].get_height() * scale)))
                pentagon_rect = pentagon_resized.get_rect(center=(900, 415))
                display.blit(pentagon_resized, pentagon_rect)
                draw_text("pentagon", (255, 255, 255), 520, 415, 45, display, shadow=True, outline=True, outline_width=3)

                oval_resized = pygame.transform.scale(data.shapes["oval"], (int(data.shapes["oval"].get_width() * scale), int(data.shapes["oval"].get_height() * scale)))
                oval_rect = oval_resized.get_rect(center=(900, 515))
                display.blit(oval_resized, oval_rect)
                draw_text("oval", (255, 255, 255), 520, 515, 45, display, shadow=True, outline=True, outline_width=3)

                if bi.gleft_arrow not in buttons:
                    buttons.append(bi.gleft_arrow)
                if bi.gright_arrow in buttons:
                    buttons.remove(bi.gright_arrow)
                if bi.gleft_arrow.draw(display):
                    page = 1
        else:
            pass

        if bi.close_button.draw(display):
            guide = False
            page = 1

    return buttons
