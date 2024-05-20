from utils.window import width

def scroll_bg(display, bg, bg_x, scroll_speed):
    bg_x += scroll_speed
    if bg_x > width:
        bg_x = 0
    display.blit(bg, (bg_x - width, 0))
    display.blit(bg, (bg_x, 0))
    return bg_x
