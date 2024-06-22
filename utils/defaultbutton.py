import pygame
import sys
import os
import configparser
import assets.assets as a
import functions.buttoninstance as bi
from functions.transition import fade
from utils.window import *
from functions.text import draw_text

pygame.mixer.init()

fscreen = False
settings = False
autosave = False
autosave_disable_click_time = None
autosave_enable_click_time = None
autosave_delay = 200
button_storage = []

tint_surface = pygame.Surface((width, height))
tint_surface.set_alpha(128)
tint_surface.fill((0, 0, 0))

slider_track_img = a.slider_track
slider_handle_img = a.slider_handle

track_width, track_height = slider_track_img.get_width(), slider_track_img.get_height()
handle_width, handle_height = slider_handle_img.get_width(), slider_handle_img.get_height()

music_slider_x = 830
music_slider_y = 370
music_min_x = music_slider_x
music_max_x = music_slider_x + track_width - handle_width

if music_max_x <= music_min_x:
    music_max_x = music_min_x + 1

music_volume = 1.0
music_handle_x = music_min_x
music_dragging = False

sound_effects_slider_x = 830
sound_effects_slider_y = 440
sound_effects_min_x = sound_effects_slider_x
sound_effects_max_x = sound_effects_slider_x + track_width - handle_width

if sound_effects_max_x <= sound_effects_min_x:
    sound_effects_max_x = sound_effects_min_x + 1

sound_effects_volume = 1.0
sound_effects_handle_x = sound_effects_min_x
sound_effects_dragging = False

config_dir = "saves"
config_file = os.path.join(config_dir, "config.ini")

def load_settings():
    global fscreen, music_volume, sound_effects_volume, music_handle_x, sound_effects_handle_x
    
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        if config.has_section('Settings'):
            fscreen_str = config.get('Settings', 'fullscreen', fallback='False')
            fscreen = fscreen_str.lower() == 'true'
            music_volume = config.getfloat('Settings', 'music_volume', fallback=1.0)
            sound_effects_volume = config.getfloat('Settings', 'sound_effects_volume', fallback=1.0)
            music_volume = min(music_volume, 1.0)
            sound_effects_volume = min(sound_effects_volume, 1.0)
        else:
            fscreen = False
            music_volume = 1.0
            sound_effects_volume = 1.0
        
        update_volume()

    except (ValueError, configparser.Error) as e:
        print(f"Error loading settings: {e}")
        fscreen = False
        music_volume = 1.0
        sound_effects_volume = 1.0
        music_handle_x = music_max_x
        sound_effects_handle_x = sound_effects_max_x

def update_volume():
    global music_handle_x, sound_effects_handle_x
    music_handle_x = music_min_x + (music_max_x - music_min_x) * music_volume
    sound_effects_handle_x = sound_effects_min_x + (sound_effects_max_x - sound_effects_min_x) * sound_effects_volume
    
    pygame.mixer.music.set_volume(music_volume)
    a.button_click.set_volume(sound_effects_volume)
    a.button_hover.set_volume(sound_effects_volume)

def save_settings():
    global fscreen, music_volume, sound_effects_volume
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    config = configparser.ConfigParser()
    config['Settings'] = {
        'fullscreen': str(fscreen),
        'music_volume': str(music_volume),
        'sound_effects_volume': str(sound_effects_volume)
    }
    with open(config_file, 'w') as configfile:
        config.write(configfile)

load_settings()

if fscreen:
    pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
    pygame.display.toggle_fullscreen()

music_handle_y = music_slider_y + (track_height - handle_height) // 2
sound_effects_handle_y = sound_effects_slider_y + (track_height - handle_height) // 2

def button_disable(buttons):
    for button in buttons:
        if button not in [bi.close_button, bi.toggle_fullscreenoff, bi.toggle_fullscreenon, bi.toggle_asoff, bi.toggle_ason, bi.quit_button]:
            button.disabled = True
            button_storage.append(button)

def DefaultButtons(display, buttons, ascheck=True):
    global settings, fscreen, autosave, autosave_disable_click_time, autosave_enable_click_time, button_disable
    global music_dragging, music_handle_x, music_volume, sound_effects_dragging, sound_effects_handle_x, sound_effects_volume

    load_settings()

    if not settings:
        if bi.settings_button not in buttons:
            buttons.append(bi.settings_button)
        for button in buttons:
            button.disabled = False
        button_storage.clear()
        if bi.settings_button.draw(display):
            settings = True

    if settings:
        button_disable(buttons)
        buttons.clear()
        if buttons == []:
            buttons.extend([bi.close_button, bi.toggle_fullscreenoff, bi.quit_button])

        display.blit(tint_surface, (0, 0))
        a.settingsbox_rect.center = width // 2, height // 2
        display.blit(a.settingsbox, a.settingsbox_rect)
        a.settingstext_rect.center = width // 2, 140
        display.blit(a.settingstext, a.settingstext_rect)

        draw_text("fullscreen", (0, 0, 0), 520, 250, 50, display)
        draw_text("autosave", (0, 0, 0), 520, 320, 50, display)
        draw_text("music volume", (0, 0, 0), 520, 390, 50, display)
        draw_text("s. effects volume", (0, 0, 0), 520, 460, 50, display)

        if not fscreen:
            if bi.toggle_fullscreenoff.draw(display):
                pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
                pygame.display.toggle_fullscreen()
                fscreen = True
                save_settings()
        else:
            if bi.toggle_fullscreenon.draw(display):
                pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SHOWN, vsync=1)
                fscreen = False
                save_settings()

        if bi.close_button.draw(display):
            buttons.clear()
            buttons.extend(button_storage)
            settings = False

        if bi.quit_button.draw(display):
            fade(display)
            pygame.quit()
            sys.exit()

        if ascheck:
            buttons.append(bi.toggle_asoff)
            current_time = pygame.time.get_ticks()
            if not autosave:
                if bi.toggle_asoff.draw(display):
                    autosave_enable_click_time = current_time
            else:
                if bi.toggle_ason.draw(display):
                    autosave_disable_click_time = current_time

            if autosave_enable_click_time:
                if current_time - autosave_enable_click_time >= autosave_delay:
                    autosave = True
                    autosave_enable_click_time = None

            if autosave_disable_click_time:
                if current_time - autosave_disable_click_time >= autosave_delay:
                    autosave = False
                    autosave_disable_click_time = None

        else:
            if bi.toggle_aslocked.draw(display, True):
                pass

        screen.blit(a.slider_track, (music_slider_x, music_slider_y))
        music_handle_rect = screen.blit(a.slider_handle, (music_handle_x, music_handle_y))

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0] and music_handle_rect.collidepoint(mouse_pos) and not music_dragging:
            music_dragging = True

        if not mouse_pressed[0]:
            music_dragging = False

        if music_dragging:
            music_handle_x = mouse_pos[0] - handle_width // 2
            if music_handle_x < music_min_x:
                music_handle_x = music_min_x
            elif music_handle_x > music_max_x:
                music_handle_x = music_max_x

            if music_max_x - music_min_x != 0:
                music_volume = (music_handle_x - music_min_x) / (music_max_x - music_min_x)
                if music_volume < 0.0:
                    music_volume = 0.0
                elif music_volume > 1.0:
                    music_volume = 1.0
                pygame.mixer.music.set_volume(music_volume)
                save_settings()

        screen.blit(a.slider_track, (sound_effects_slider_x, sound_effects_slider_y))
        sound_effects_handle_rect = screen.blit(a.slider_handle, (sound_effects_handle_x, sound_effects_handle_y))

        if mouse_pressed[0] and sound_effects_handle_rect.collidepoint(mouse_pos) and not sound_effects_dragging:
            sound_effects_dragging = True

        if not mouse_pressed[0]:
            sound_effects_dragging = False

        if sound_effects_dragging:
            sound_effects_handle_x = mouse_pos[0] - handle_width // 2
            if sound_effects_handle_x < sound_effects_min_x:
                sound_effects_handle_x = sound_effects_min_x
            elif sound_effects_handle_x > sound_effects_max_x:
                sound_effects_handle_x = sound_effects_max_x

            if sound_effects_max_x - sound_effects_min_x != 0:
                sound_effects_volume = (sound_effects_handle_x - sound_effects_min_x) / (sound_effects_max_x - sound_effects_min_x)
                if sound_effects_volume < 0.0:
                    sound_effects_volume = 0.0
                elif sound_effects_volume > 1.0:
                    sound_effects_volume = 1.0

                a.button_click.set_volume(sound_effects_volume)
                a.button_hover.set_volume(sound_effects_volume)
                save_settings()

    return buttons

