from utils.window import *

def scroll_bg(display, bg, bg_x, bg_y, scroll_speed):
    bg_x += scroll_speed
    bg_y -= scroll_speed

    if bg_x >= width:
        bg_x = 0
    if bg_y <= -height:
        bg_y = 0

    display.blit(bg, (bg_x - width, bg_y + height))
    display.blit(bg, (bg_x, bg_y + height))
    display.blit(bg, (bg_x + width, bg_y + height))
    display.blit(bg, (bg_x - width, bg_y))
    display.blit(bg, (bg_x, bg_y))
    display.blit(bg, (bg_x + width, bg_y))
    display.blit(bg, (bg_x - width, bg_y - height))
    display.blit(bg, (bg_x, bg_y - height))
    display.blit(bg, (bg_x + width, bg_y - height))
    
    return bg_x, bg_y