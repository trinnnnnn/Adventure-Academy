# import necessary modules and classes
import functions.buttonfunction as bf
import assets.assets as a
from utils.window import width, height

# create instances of buttons with respective images and properties
start_button = bf.Button(width//2, 550, a.start_img, a.startdown_img, 0.2)
save_button = bf.Button(1100, 100, a.start_img, a.startdown_img, 0.2)
confirm_button = bf.Button(400, 500, a.confirm_img, a.confirmdown_img, 0.075)
unconfirm_button = bf.Button(880, 500, a.unconfirm_img, a.unconfirmdown_img, 0.075)
shapes_button = bf.Button(400, 300, a.shapes_img, a.shapesdown_img, 0.65)
alphabet_button = bf.Button(820, 300, a.alphabet_img, a.alphabetdown_img, 0.65)
colours_button = bf.Button(width//2, 400, a.colours_img, a.coloursdown_img, 0.65)
emptyslot1_button = bf.Button(380, height//2, a.emptyslot1_img, a.emptyslot1down_img, 0.65)
emptyslot2_button = bf.Button(width//2, height//2, a.emptyslot2_img, a.emptyslot2down_img, 0.65)
emptyslot3_button = bf.Button(900, height//2, a.emptyslot3_img, a.emptyslot3down_img, 0.65)
slot1_button = bf.Button(380, height//2, a.slot1_img, a.slot1down_img, 0.65)
slot2_button = bf.Button(width//2, height//2, a.slot2_img, a.slot2down_img, 0.65)
slot3_button = bf.Button(900, height//2, a.slot3_img, a.slot3down_img, 0.65)

#defaultbuttons
power_button = bf.Button(65, 65, a.power_img, a.powerdown_img, 0.1)
