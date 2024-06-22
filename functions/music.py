import pygame
import assets.assets as a

pygame.mixer.init()

bgmusic1 = a.bgmusic1
bgmusic2 = a.bgmusic2

current_track = bgmusic2

def background_music():
    global current_track

    if not pygame.mixer.music.get_busy():
        if current_track == bgmusic1:
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load(bgmusic2)
            current_track = bgmusic2
        else:
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load(bgmusic1)
            current_track = bgmusic1

        pygame.mixer.music.play(fade_ms=1000)