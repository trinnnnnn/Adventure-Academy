import pygame
import assets.assets as a
from functions.transition import fade

current_key_pressed = []
backspace_timer = 0
backspace_delay = 100

def Keypress(self, state, text, max_len):
    global current_key_pressed, backspace_timer

    return_pressed = False
    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()

    if keys[pygame.K_BACKSPACE]:
        if current_time - backspace_timer >= backspace_delay:
            text = text[:-1]
            backspace_timer = current_time

    if max_len is None or max_len > len(text):
        for i in range(pygame.K_a, pygame.K_z + 1):
            if keys[i]:
                char = chr(i)
                if char not in current_key_pressed:
                    text += char
                    current_key_pressed.append(char)

        for i in range(pygame.K_0, pygame.K_9 + 1):
            if keys[i]:
                char = chr(i)
                if char not in current_key_pressed:
                    text += char
                    current_key_pressed.append(char)

    current_key_pressed = [char for char in current_key_pressed if keys[ord(char)]]

    if keys[pygame.K_RETURN]:
        pygame.mixer.Sound.play(a.button_click)
        return_pressed = True
        if state is not None:
            self.gameStateManager.set_state(state)
            fade(self.display)
    
    return text, return_pressed
