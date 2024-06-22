import pygame

text_cache = {}

def draw_text(text_string, text_col, x, y, size, screen, align="center", shadow=False, shadow_color=(120, 120, 120), shadow_offset=(0, 5), outline=False, outline_color=(0, 0, 0), outline_width=5):

    cache_key = (text_string, text_col, size, align, shadow, shadow_color, shadow_offset, outline, outline_color, outline_width)
    
    font = pygame.font.Font("assets/font/Minecraft.ttf", size)
    text_string = text_string.upper()
    lines = text_string.splitlines()
    
    if cache_key not in text_cache:
        rendered_lines = []
        for line in lines:
            line_text = font.render(line, True, text_col)
            rendered_lines.append((line, line_text))

        text_cache[cache_key] = rendered_lines
    else:
        rendered_lines = text_cache[cache_key]

    for i, (line, line_text) in enumerate(rendered_lines):
        line_rect = None

        if align == "center":
            line_rect = line_text.get_rect(center=(x, y + i * (size * 1.3)))
        elif align == "left":
            line_rect = line_text.get_rect(topleft=(x, y + i * (size * 1.3)))
        elif align == "right":
            line_rect = line_text.get_rect(topright=(x, y + i * (size * 1.3)))

        if outline:
            for dx in [-outline_width, 0, outline_width]:
                for dy in [-outline_width, 0, outline_width]:
                    if dx != 0 or dy != 0:
                        outline_text = font.render(line, True, outline_color)
                        outline_rect = line_rect.copy()
                        outline_rect.topleft = (line_rect.left + dx, line_rect.top + dy)
                        screen.blit(outline_text, outline_rect.topleft)

        if shadow:
            shadow_text = font.render(line, True, shadow_color)
            shadow_rect = line_rect.copy()
            shadow_rect.topleft = (shadow_rect.left + shadow_offset[0], shadow_rect.top + shadow_offset[1])
            
            if outline:
                for dx in [-outline_width, 0, outline_width]:
                    for dy in [-outline_width, 0, outline_width]:
                        if dx != 0 or dy != 0:
                            outline_shadow_text = font.render(line, True, outline_color)
                            outline_shadow_rect = shadow_rect.copy()
                            outline_shadow_rect.topleft = (shadow_rect.left + dx, shadow_rect.top + dy)
                            screen.blit(outline_shadow_text, outline_shadow_rect.topleft)
            
            screen.blit(shadow_text, shadow_rect.topleft)

        screen.blit(line_text, line_rect.topleft)

def mousetextcolorchange(button, textcol1, textcol2):
    mouse = pygame.mouse.get_pos()
    if button.rect.collidepoint(mouse):
        return textcol1
    else:
        return textcol2
