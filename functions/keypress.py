import time
import pygame
from functions.transition import fade

error_start = 0
error = False  # Define error variable outside the function

def Keypress(self, state, text, max_len, error_duration=0):
    global error_start, error  # Access the global error variable
    return_pressed = False
    keys = pygame.key.get_pressed()
    keypress_delay = 220

    if keys[pygame.K_BACKSPACE] and pygame.time.get_ticks() - self.last_keypress_time >= keypress_delay:
        text = text[:-1]
        self.last_keypress_time = pygame.time.get_ticks()

    if max_len is None or max_len > len(text):
        for i in range(pygame.K_a, pygame.K_z + 1):
            if keys[i]:
                if pygame.time.get_ticks() - self.last_keypress_time >= keypress_delay:
                    text += chr(i)
                    self.last_keypress_time = pygame.time.get_ticks()
        for i in range(pygame.K_0, pygame.K_9 + 1):
            if keys[i]:
                if pygame.time.get_ticks() - self.last_keypress_time >= keypress_delay:
                    text += chr(i)
                    self.last_keypress_time = pygame.time.get_ticks()
    elif any(keys) and max_len == len(text):
        error = True  # Set error to True
        if error_start == 0:
            error_start = time.time()

    if error and time.time() - error_start >= error_duration:
        error = False
        error_start = 0

    if keys[pygame.K_RETURN]:
        return_pressed = True
        if state is not None:
            self.gameStateManager.set_state(state)
            fade(self.display)
    
    return text, return_pressed, error  # Return error variable as well
