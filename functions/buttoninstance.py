# import necessary modules and classes
import functions.buttonfunction as bf
import assets.assets as a
from utils.window import width, height


# create instances of buttons with respective images and properties
start_button = bf.Button(width//2, 550, a.start_img, a.startdown_img, 0.2)
save_button = bf.Button(1180, 100, a.start_img, a.startdown_img, 0.2)
confirm_button = bf.Button(400, 500, a.confirm_img, a.confirmdown_img, 0.075)
confirm2_button = bf.Button(1080, 550, a.confirm_img, a.confirmdown_img, 0.075)
unconfirm_button = bf.Button(880, 500, a.unconfirm_img, a.unconfirmdown_img, 0.075)
back_button = bf.Button(65, 65, a.back_img, a.backdown_img, 0.14)
shapes_button = bf.Button(400, 300, a.shapes_img, a.shapesdown_img, 0.65)
alphabet_button = bf.Button(820, 300, a.alphabet_img, a.alphabetdown_img, 0.65)
colours_button = bf.Button(width//2, 400, a.colours_img, a.coloursdown_img, 0.65)
emptyslot1_button = bf.Button(380, height//2, a.emptyslot1_img, a.emptyslot1down_img, 0.65)
emptyslot2_button = bf.Button(width//2, height//2, a.emptyslot2_img, a.emptyslot2down_img, 0.65)
emptyslot3_button = bf.Button(900, height//2, a.emptyslot3_img, a.emptyslot3down_img, 0.65)
slot1_button = bf.Button(380, height//2, a.slot1_img, a.slot1down_img, 0.65)
slot2_button = bf.Button(width//2, height//2, a.slot2_img, a.slot2down_img, 0.65)
slot3_button = bf.Button(900, height//2, a.slot3_img, a.slot3down_img, 0.65)
save_button = bf.Button(1215, 65, a.save_img, a.savedown_img, 0.16)
delete1_button = bf.Button(380, height//2, a.delete1_img, a.delete1down_img, 0.1)
delete2_button = bf.Button(width//2, height//2, a.delete2_img, a.delete2down_img, 0.1)
delete3_button = bf.Button(900, height//2, a.delete3_img, a.delete3down_img, 0.1)
play1_button = bf.Button(380, height//2, a.play1_img, a.play1down_img, 0.1)
play2_button = bf.Button(width//2, height//2, a.play2_img, a.play2down_img, 0.1)
play3_button = bf.Button(900, height//2, a.play3_img, a.play3down_img, 0.1)
leftarrow_button = bf.Button(330, height//2, a.leftarrow_img, a.leftarrowdown_img, 0.08)
rightarrow_button = bf.Button(950, height//2, a.rightarrow_img, a.rightarrowdown_img, 0.08)
play_button = bf.Button(width//2, 600, a.play_img, a.playdown_img, 0.2)

#defaultbuttons
settings_button = bf.Button(1230, 670, a.settings_img, a.settingsdown_img, 0.1)
power_button = bf.Button(1230, 570, a.power_img, a.powerdown_img, 0.1)
