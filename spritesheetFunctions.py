import pygame
import constants

class SpriteSheet(object):
    def __init__(self, fileName):
        #Constructor. Pass in the filename of the spritesheet

        #Load the spritesheet
        self.spriteSheet = pygame.image.load(fileName).convert()

    def getImage(self, x, y, width, height):
        # Get the image out of a larger sprite sheet. Pass in x and y coordinates of sprite, and dimensions of sprite.

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from large sheet onto the smaller image
        image.blit(self.spriteSheet, (0, 0), (x, y, width, height))

        # Assuming black works as transparent color
        image.set_colorkey(constants.BLACK)

        # Return image
        return image