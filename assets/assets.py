import pygame
import pygame.locals

pygame.mixer.init()

#bg
unscroll_bg = pygame.image.load("assets/images/bg/bg.png")
unscroll_bg = pygame.transform.scale(unscroll_bg, (1280, 720))

#sound
bgmusic1 = "assets/sound/music/bgmusic1.mp3"
bgmusic2 = "assets/sound/music/bgmusic2.mp3"
button_hover = pygame.mixer.Sound("assets/sound/ui/button_hover.wav")
button_click = pygame.mixer.Sound("assets/sound/ui/button_click.wav")

#buttons
start_img = pygame.image.load("assets/images/buttons/placeholder_button.png").convert_alpha()
startdown_img = pygame.image.load("assets/images/buttons/placeholder_buttondown.png").convert_alpha()
confirm_img = pygame.image.load("assets/images/buttons/confirm.png").convert_alpha()
confirmdown_img = pygame.image.load("assets/images/buttons/confirmdown.png").convert_alpha()
unconfirm_img = pygame.image.load("assets/images/buttons/x.png").convert_alpha()
unconfirmdown_img = pygame.image.load("assets/images/buttons/xdown.png").convert_alpha()
back_img = pygame.image.load("assets/images/buttons/back.png").convert_alpha()
backdown_img = pygame.image.load("assets/images/buttons/backdown.png").convert_alpha()
back_img = pygame.image.load("assets/images/buttons/back.png").convert_alpha()
backdown_img = pygame.image.load("assets/images/buttons/backdown.png").convert_alpha()
shapes_img = pygame.image.load("assets/images/buttons/shapes.png").convert_alpha()
shapesdown_img = pygame.image.load("assets/images/buttons/shapesdown.png").convert_alpha()
colours_img = pygame.image.load("assets/images/buttons/colours.png").convert_alpha()
coloursdown_img = pygame.image.load("assets/images/buttons/coloursdown.png").convert_alpha()
alphabet_img = pygame.image.load("assets/images/buttons/alphabet.png").convert_alpha()
alphabetdown_img = pygame.image.load("assets/images/buttons/alphabetdown.png").convert_alpha()
power_img = pygame.image.load("assets/images/buttons/power.png").convert_alpha()
powerdown_img = pygame.image.load("assets/images/buttons/powerdown.png").convert_alpha()
emptyslot1_img = pygame.image.load("assets/images/buttons/emptyslot1.png").convert_alpha()
emptyslot1down_img = pygame.image.load("assets/images/buttons/emptyslot1down.png").convert_alpha()
emptyslot2_img = pygame.image.load("assets/images/buttons/emptyslot2.png").convert_alpha()
emptyslot2down_img = pygame.image.load("assets/images/buttons/emptyslot2down.png").convert_alpha()
emptyslot3_img = pygame.image.load("assets/images/buttons/emptyslot3.png").convert_alpha()
emptyslot3down_img = pygame.image.load("assets/images/buttons/emptyslot3down.png").convert_alpha()
slot1_img = pygame.image.load("assets/images/buttons/slot1.png").convert_alpha()
slot1down_img = pygame.image.load("assets/images/buttons/slot1down.png").convert_alpha()
slot2_img = pygame.image.load("assets/images/buttons/slot2.png").convert_alpha()
slot2down_img = pygame.image.load("assets/images/buttons/slot2down.png").convert_alpha()
slot3_img = pygame.image.load("assets/images/buttons/slot3.png").convert_alpha()
slot3down_img = pygame.image.load("assets/images/buttons/slot3down.png").convert_alpha()
save_img = pygame.image.load("assets/images/buttons/save.png").convert_alpha()
savedown_img = pygame.image.load("assets/images/buttons/savedown.png").convert_alpha()
delete1_img = pygame.image.load("assets/images/buttons/delete1.png").convert_alpha()
delete1down_img = pygame.image.load("assets/images/buttons/delete1down.png").convert_alpha()
delete2_img = pygame.image.load("assets/images/buttons/delete2.png").convert_alpha()
delete2down_img = pygame.image.load("assets/images/buttons/delete2down.png").convert_alpha()
delete3_img = pygame.image.load("assets/images/buttons/delete3.png").convert_alpha()
delete3down_img = pygame.image.load("assets/images/buttons/delete3down.png").convert_alpha()
play1_img = pygame.image.load("assets/images/buttons/play1.png").convert_alpha()
play1down_img = pygame.image.load("assets/images/buttons/play1down.png").convert_alpha()
play2_img = pygame.image.load("assets/images/buttons/play2.png").convert_alpha()
play2down_img = pygame.image.load("assets/images/buttons/play2down.png").convert_alpha()
play3_img = pygame.image.load("assets/images/buttons/play3.png").convert_alpha()
play3down_img = pygame.image.load("assets/images/buttons/play3down.png").convert_alpha()
leftarrow_img = pygame.image.load("assets/images/buttons/arrowleft.png").convert_alpha()
leftarrowdown_img = pygame.image.load("assets/images/buttons/arrowleftdown.png").convert_alpha()
rightarrow_img = pygame.image.load("assets/images/buttons/arrowright.png").convert_alpha()
rightarrowdown_img = pygame.image.load("assets/images/buttons/arrowrightdown.png").convert_alpha()
play_img = pygame.image.load("assets/images/buttons/play.png").convert_alpha()
playdown_img = pygame.image.load("assets/images/buttons/playdown.png").convert_alpha()
save_img = pygame.image.load("assets/images/buttons/save.png").convert_alpha()
savedown_img = pygame.image.load("assets/images/buttons/savedown.png").convert_alpha()
delete1_img = pygame.image.load("assets/images/buttons/delete1.png").convert_alpha()
delete1down_img = pygame.image.load("assets/images/buttons/delete1down.png").convert_alpha()
delete2_img = pygame.image.load("assets/images/buttons/delete2.png").convert_alpha()
delete2down_img = pygame.image.load("assets/images/buttons/delete2down.png").convert_alpha()
delete3_img = pygame.image.load("assets/images/buttons/delete3.png").convert_alpha()
delete3down_img = pygame.image.load("assets/images/buttons/delete3down.png").convert_alpha()
play1_img = pygame.image.load("assets/images/buttons/play1.png").convert_alpha()
play1down_img = pygame.image.load("assets/images/buttons/play1down.png").convert_alpha()
play2_img = pygame.image.load("assets/images/buttons/play2.png").convert_alpha()
play2down_img = pygame.image.load("assets/images/buttons/play2down.png").convert_alpha()
play3_img = pygame.image.load("assets/images/buttons/play3.png").convert_alpha()
play3down_img = pygame.image.load("assets/images/buttons/play3down.png").convert_alpha()
settings_img = pygame.image.load("assets/images/buttons/settings.png").convert_alpha()
settingsdown_img = pygame.image.load("assets/images/buttons/settingsdown.png").convert_alpha()
choose_img = pygame.image.load("assets/images/buttons/choose.png").convert_alpha()
choosedown_img = pygame.image.load("assets/images/buttons/choosedown.png").convert_alpha()
fullscreen_img = pygame.image.load("assets/images/buttons/fullscreenbutton.png").convert_alpha()
minimize_img = pygame.image.load("assets/images/buttons/minimizebutton.png").convert_alpha()
autosaveoff_img = pygame.image.load("assets/images/buttons/autosaveoff.png").convert_alpha()
autosaveon_img = pygame.image.load("assets/images/buttons/autosaveon.png").convert_alpha()
autosave_img = pygame.image.load("assets/images/buttons/autosave.png").convert_alpha()
autosavedown_img = pygame.image.load("assets/images/buttons/autosavedown.png").convert_alpha()
close_img = pygame.image.load("assets/images/buttons/close.png").convert_alpha()
closedown_img = pygame.image.load("assets/images/buttons/closedown.png").convert_alpha()
toggleoff_img = pygame.image.load("assets/images/buttons/toggleoff.png").convert_alpha()
toggleoffdown_img = pygame.image.load("assets/images/buttons/toggleoffdown.png").convert_alpha()
toggleon_img = pygame.image.load("assets/images/buttons/toggleon.png").convert_alpha()
toggleondown_img = pygame.image.load("assets/images/buttons/toggleondown.png").convert_alpha()
quit_img = pygame.image.load("assets/images/buttons/quit.png").convert_alpha()
quitdown_img = pygame.image.load("assets/images/buttons/quitdown.png").convert_alpha()
guide_img = pygame.image.load("assets/images/buttons/guide.png").convert_alpha()
guidedown_img = pygame.image.load("assets/images/buttons/guidedown.png").convert_alpha()

#shapes
circle_original = pygame.image.load("assets/images/shapes/circle.png").convert_alpha()
square_original = pygame.image.load("assets/images/shapes/square.png").convert_alpha()
rectangle_original = pygame.image.load("assets/images/shapes/rectangle.png").convert_alpha()
star_original = pygame.image.load("assets/images/shapes/star.png").convert_alpha()
pentagon_original = pygame.image.load("assets/images/shapes/pentagon.png").convert_alpha()
diamond_original = pygame.image.load("assets/images/shapes/diamond.png").convert_alpha()
oval_original = pygame.image.load("assets/images/shapes/oval.png").convert_alpha()
triangle_original = pygame.image.load("assets/images/shapes/triangle.png").convert_alpha()

#shapes scaling
circle = pygame.transform.scale(circle_original, (int(circle_original.get_width() * 0.4), int(circle_original.get_height() * 0.4))).convert_alpha()
circle_rect = circle.get_rect()
square = pygame.transform.scale(square_original, (int(square_original.get_width() * 0.4), int(square_original.get_height() * 0.4))).convert_alpha()
square_rect = square.get_rect()
rectangle = pygame.transform.scale(rectangle_original, (int(rectangle_original.get_width() * 0.4), int(rectangle_original.get_height() * 0.4))).convert_alpha()
rectangle_rect = rectangle.get_rect()
star = pygame.transform.scale(star_original, (int(star_original.get_width() * 0.4), int(star_original.get_height() * 0.4))).convert_alpha()
star_rect = star.get_rect()
pentagon = pygame.transform.scale(pentagon_original, (int(pentagon_original.get_width() * 0.4), int(pentagon_original.get_height() * 0.4))).convert_alpha()
pentagon_rect = pentagon.get_rect()
oval = pygame.transform.scale(oval_original, (int(oval_original.get_width() * 0.4), int(oval_original.get_height() * 0.4))).convert_alpha()
oval_rect = oval.get_rect()
diamond = pygame.transform.scale(diamond_original, (int(diamond_original.get_width() * 0.4), int(diamond_original.get_height() * 0.4))).convert_alpha()
diamond_rect = diamond.get_rect()
triangle = pygame.transform.scale(triangle_original, (int(triangle_original.get_width() * 0.4), int(triangle_original.get_height() * 0.4))).convert_alpha()
triangle_rect = triangle.get_rect()

#utility
textframe_original = pygame.image.load("assets/images/util/textframe.png").convert_alpha()
textinputframe_original = pygame.image.load("assets/images/util/textinputframe.png").convert_alpha()
gameframe_original = pygame.image.load("assets/images/buttons/smallframe.png").convert_alpha()
shapes_original = pygame.image.load("assets/images/buttons/shapes.png").convert_alpha()
pleaseread_original = pygame.image.load("assets/images/util/pleaseread.png").convert_alpha()
zerostars_original = pygame.image.load("assets/images/util/zerostars.png").convert_alpha()
onestars_original = pygame.image.load("assets/images/util/onestars.png").convert_alpha()
twostars_original = pygame.image.load("assets/images/util/twostars.png").convert_alpha()
threestars_original = pygame.image.load("assets/images/util/threestars.png").convert_alpha()
shapebox_original = pygame.image.load("assets/images/util/shapebox.png").convert_alpha()
logo_original = pygame.image.load("assets/images/util/logo.png").convert_alpha()
settingstext_original = pygame.image.load("assets/images/util/settingstext.png").convert_alpha()
settingsbox_original = pygame.image.load("assets/images/util/settingsbox.png").convert_alpha()
slider_track_original = pygame.image.load('assets/images/util/slider_track.png')
slider_handle_original = pygame.image.load('assets/images/util/slider_handle.png')
loadtext_original = pygame.image.load("assets/images/util/loadtext.png").convert_alpha()
loadsavetext_original = pygame.image.load("assets/images/util/loadsavetext.png").convert_alpha()
guidetext_original = pygame.image.load("assets/images/util/guidetext.png").convert_alpha()

#utility scaling
textframe = pygame.transform.scale(textframe_original, (int(textframe_original.get_width() * 0.33), int(textframe_original.get_height() * 0.33))).convert_alpha()
textframe_rect = textframe.get_rect()
textframe2 = pygame.transform.scale(textframe_original, (int(textframe_original.get_width() * 0.34), int(textframe_original.get_height() * 0.23))).convert_alpha()
textframe2_rect = textframe2.get_rect()
textframe3 = pygame.transform.scale(textframe_original, (int(textframe_original.get_width() * 0.22), int(textframe_original.get_height() * 0.22))).convert_alpha()
textframe3_rect = textframe3.get_rect()
textinputframe = pygame.transform.scale(textinputframe_original, (int(textinputframe_original.get_width() * 0.33), int(textinputframe_original.get_height() * 0.33))).convert_alpha()
textinputframe_rect = textinputframe.get_rect()
emptyslot1_scaled = pygame.transform.scale(emptyslot1_img, (int(emptyslot1_img.get_width() * 0.65), int(emptyslot1_img.get_height() * 0.65))).convert_alpha()
emptyslot1_scaled_rect = emptyslot1_scaled.get_rect()
emptyslot2_scaled = pygame.transform.scale(emptyslot2_img, (int(emptyslot2_img.get_width() * 0.65), int(emptyslot2_img.get_height() * 0.65))).convert_alpha()
emptyslot2_scaled_rect = emptyslot2_scaled.get_rect()
emptyslot3_scaled = pygame.transform.scale(emptyslot3_img, (int(emptyslot3_img.get_width() * 0.65), int(emptyslot3_img.get_height() * 0.65))).convert_alpha()
emptyslot3_scaled_rect = emptyslot3_scaled.get_rect()
emptyslot1down_scaled = pygame.transform.scale(emptyslot1down_img, (int(emptyslot1down_img.get_width() * 0.65), int(emptyslot1down_img.get_height() * 0.65))).convert_alpha()
emptyslot1down_scaled_rect = emptyslot1down_scaled.get_rect()
emptyslot2down_scaled = pygame.transform.scale(emptyslot2down_img, (int(emptyslot2down_img.get_width() * 0.65), int(emptyslot2down_img.get_height() * 0.65))).convert_alpha()
emptyslot2down_scaled_rect = emptyslot2down_scaled.get_rect()
emptyslot3down_scaled = pygame.transform.scale(emptyslot3down_img, (int(emptyslot3down_img.get_width() * 0.65), int(emptyslot3down_img.get_height() * 0.65))).convert_alpha()
emptyslot3down_scaled_rect = emptyslot3down_scaled.get_rect()
slot1_scaled = pygame.transform.scale(slot1_img, (int(slot1_img.get_width() * 0.65), int(slot1_img.get_height() * 0.65))).convert_alpha()
slot1_scaled_rect = slot1_scaled.get_rect()
slot2_scaled = pygame.transform.scale(slot2_img, (int(slot2_img.get_width() * 0.65), int(slot2_img.get_height() * 0.65))).convert_alpha()
slot2_scaled_rect = slot2_scaled.get_rect()
slot3_scaled = pygame.transform.scale(slot3_img, (int(slot3_img.get_width() * 0.65), int(slot3_img.get_height() * 0.65))).convert_alpha()
slot3_scaled_rect = slot3_scaled.get_rect()
slot1down_scaled = pygame.transform.scale(slot1down_img, (int(slot1down_img.get_width() * 0.65), int(slot1down_img.get_height() * 0.65))).convert_alpha()
slot1down_scaled_rect = slot1down_scaled.get_rect()
slot2down_scaled = pygame.transform.scale(slot2down_img, (int(slot2down_img.get_width() * 0.65), int(slot2down_img.get_height() * 0.65))).convert_alpha()
slot2down_scaled_rect = slot2down_scaled.get_rect()
slot3down_scaled = pygame.transform.scale(slot3down_img, (int(slot3down_img.get_width() * 0.65), int(slot3down_img.get_height() * 0.65))).convert_alpha()
slot3down_scaled_rect = slot3down_scaled.get_rect()
gameframe = pygame.transform.scale(gameframe_original, (int(gameframe_original.get_width() * 0.33), int(gameframe_original.get_height() * 0.33))).convert_alpha()
gameframe_rect = gameframe.get_rect()
shapes = pygame.transform.scale(shapes_original, (int(shapes_original.get_width() * 0.8), int(shapes_original.get_height() * 0.8))).convert_alpha()
shapes_rect = shapes.get_rect()
pleaseread = pygame.transform.scale(pleaseread_original, (int(pleaseread_original.get_width() * 0.5), int(pleaseread_original.get_height() * 0.5))).convert_alpha()
pleaseread_rect = pleaseread.get_rect()
zerostars = pygame.transform.scale(zerostars_original, (int(zerostars_original.get_width() * 0.15), int(zerostars_original.get_height() * 0.15))).convert_alpha()
zerostars_rect = zerostars.get_rect()
onestars = pygame.transform.scale(onestars_original, (int(onestars_original.get_width() * 0.15), int(onestars_original.get_height() * 0.15))).convert_alpha()
onestars_rect = onestars.get_rect()
twostars = pygame.transform.scale(twostars_original, (int(twostars_original.get_width() * 0.15), int(twostars_original.get_height() * 0.15))).convert_alpha()
twostars_rect = twostars.get_rect()
threestars = pygame.transform.scale(threestars_original, (int(threestars_original.get_width() * 0.15), int(threestars_original.get_height() * 0.15))).convert_alpha()
threestars_rect = threestars.get_rect()
logo = pygame.transform.scale(logo_original, (int(logo_original.get_width() * 0.8), int(logo_original.get_height() * 0.8))).convert_alpha()
logo_rect = logo.get_rect()
settingstext = pygame.transform.scale(settingstext_original, (int(settingstext_original.get_width() * 0.7), int(settingstext_original.get_height() * 0.7))).convert_alpha()
settingstext_rect = settingstext.get_rect()
settingsbox = pygame.transform.scale(settingsbox_original, (int(settingsbox_original.get_width() * 0.4), int(settingsbox_original.get_height() * 0.4))).convert_alpha()
settingsbox_rect = settingsbox.get_rect()
slider_track = pygame.transform.scale(slider_track_original, (int(slider_track_original.get_width() * 0.12), int(slider_track_original.get_height() * 0.12))).convert_alpha()
slider_track_rect = slider_track.get_rect()
slider_handle = pygame.transform.scale(slider_handle_original, (int(slider_handle_original.get_width() * 0.23), int(slider_handle_original.get_height() * 0.23))).convert_alpha()
slider_handle_rect = slider_handle.get_rect()
loadtext = pygame.transform.scale(loadtext_original, (int(loadtext_original.get_width() * 0.8), int(loadtext_original.get_height() * 0.8))).convert_alpha()
loadtext_rect = loadtext.get_rect()
loadsavetext = pygame.transform.scale(loadsavetext_original, (int(loadsavetext_original.get_width() * 0.8), int(loadsavetext_original.get_height() * 0.8))).convert_alpha()
loadsavetext_rect = loadsavetext.get_rect()
guidetext = pygame.transform.scale(guidetext_original, (int(guidetext_original.get_width() * 0.8), int(guidetext_original.get_height() * 0.8))).convert_alpha()
guidetext_rect = guidetext.get_rect()

settingsbox_width = settingsbox.get_width()
settingsbox_height = settingsbox.get_height()