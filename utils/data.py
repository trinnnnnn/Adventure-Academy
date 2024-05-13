import assets.assets as a
import pygame

userdata = {
    "username" : "",
    "score" : 0
}

# Load your images
circle_img = pygame.image.load("assets/images/shapes/circleplaceholder.png").convert_alpha()

shapes = {
    "circle": circle_img,
}
