# import necessary modules and classes
import utils.buttonfunction as bf
import assets.assets as a
from utils.window import width, height

# create instances of buttons with respective images and properties
start_button = bf.Button(width//2, 550, a.start_img, a.startdown_img, 0.2)
