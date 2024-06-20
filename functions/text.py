import pygame

def draw_text(text_string, text_col, x, y, size, screen, align="center"):

    font = pygame.font.Font("assets/font/pixel.ttf", size)

    text_string = text_string.upper()

    lines = text_string.splitlines()
    for i, line in enumerate(lines):
        line_text = font.render(line, True, text_col)

        if align == "center":
            line_rect = line_text.get_rect(center=(x, y + i * (size * 1.3)))
        elif align == "left":
            line_rect = line_text.get_rect(topleft=(x, y + i * (size * 1.3)))
        elif align == "right":
            line_rect = line_text.get_rect(topright=(x, y + i * (size * 1.3)))

        screen.blit(line_text, line_rect.topleft)

def mousetextcolorchange(button, textcol1, textcol2):
    mouse = pygame.mouse.get_pos()
    if button.rect.collidepoint(mouse):
        return textcol1
    else:
        return textcol2
