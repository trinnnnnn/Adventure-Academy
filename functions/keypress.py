import pygame

def Keypress(self, state, text, max_len):
    
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

    if keys[pygame.K_RETURN]:
            return_pressed = True
            if state == None :
                pass
            else :
                self.gameStateManager.set_state(state)
    
    return text, return_pressed
