import pygame

# function to draw text on the screen
def draw_text(text_string, text_col, x, y, size, screen, align="center"):
    # setting the font
    font = pygame.font.Font("assets/font/pixel.ttf", size)

    # setting the text uppercase because the font doesn't have any lowercase letters
    text_string = text_string.upper()

    # rendering text and changing the text anchor point based on alignment
    lines = text_string.splitlines()
    for i, line in enumerate(lines):
        # render each line of text
        line_text = font.render(line, True, text_col)

        # set the position of each line based on the alignment
        if align == "center":
            line_rect = line_text.get_rect(center=(x, y + i * (size * 1.3)))
        elif align == "left":
            line_rect = line_text.get_rect(topleft=(x, y + i * (size * 1.3)))
        elif align == "right":
            line_rect = line_text.get_rect(topright=(x, y + i * (size * 1.3)))

        # display the text
        screen.blit(line_text, line_rect.topleft)

# function to change text color when mouse is over a button
def mousetextcolorchange(button, textcol1, textcol2):
    mouse = pygame.mouse.get_pos()
    if button.rect.collidepoint(mouse):
        return textcol1
    else:
        return textcol2
