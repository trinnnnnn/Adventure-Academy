# import necessary modules and classes
import functions.buttonfunction as bf
import assets.assets as a
from utils.window import width, height

# create instances of buttons with respective images and properties
start_button = bf.Button(width//2, 550, a.placeholder_img, a.placeholderdown_img, 0.2)
save_button = bf.Button(1100, 100, a.placeholder_img, a.placeholderdown_img, 0.2)
