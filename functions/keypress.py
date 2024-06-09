import pygame
from functions.transition import fade

current_key_pressed = []

backspace_timer = 0
backspace_delay = 100

def Keypress(self, state, text, max_len):
    global current_key_pressed, backspace_timer

    return_pressed = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_BACKSPACE]:
        if pygame.time.get_ticks() - backspace_timer >= backspace_delay:
            text = text[:-1]
            backspace_timer = pygame.time.get_ticks()

    if max_len is None or max_len > len(text):
        for i in range(pygame.K_a, pygame.K_z + 1):
            if keys[i]:
                if chr(i) not in current_key_pressed:
                    current_key_pressed.clear()
                    text += chr(i)
                    current_key_pressed.append(chr(i))

        for i in range(pygame.K_0, pygame.K_9 + 1):
            if keys[i]:
                if chr(i) not in current_key_pressed:
                    text += chr(i)
                    current_key_pressed.append(chr(i))

    if not any(keys[i] for i in range(len(keys))):
        current_key_pressed.clear()

    if keys[pygame.K_RETURN]:
        return_pressed = True
        if state is not None:
            self.gameStateManager.set_state(state)
            fade(self.display)
    
    return text, return_pressed
