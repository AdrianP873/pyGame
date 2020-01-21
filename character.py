import pygame

from spritesheetFunctions import SpriteSheet

# Use constants to define the sprites you want from the sheet

WALK_RIGHT = (0, 0, 100, 100)
WALK_LEFT = (150, 100, 100, 100)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # -- ATTRIBUTES
        # Set speed vectors
        self.change_x = 0
        self.change_y = 0s
        
        # This holds all images for the animated walk left/right of our player
        self.walkingFramesL = []
        self.walkingFramesR = []

        # What direction is player facing?
        self.direction = "R"

        # Load sprite sheet
        spriteSheet = SpriteSheet("images/dk1.png")

        # Load sprites that you want
        image = spriteSheet.getImage(0, 0, 100, 90)
        self.walkingFramesR.append(image)

        # Set the image the player starts with
        self.image = self.walkingFramesR[0]

        self.rect = self.image.get_rect()



    