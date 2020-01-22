import pygame

from spritesheetFunctions import SpriteSheet

# Use constants to define the sprites you want from the sheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # -- ATTRIBUTES
        # Set speed vectors
        self.changeX = 0
        self.changeY = 0
        
        # This holds all images for the animated walk left/right of our player
        self.walkingFramesL = []
        self.walkingFramesR = []

        # List to hold punch animation
        self.punchFrames = []

        # What direction is player facing?
        self.direction = "R"

        # Load sprite sheet
        spriteSheet = SpriteSheet("images/dkArt.png")

        # Load sprites that you want. 
        # Pass in x and y coordinates of sprite, and size of sprite from spritesheet.
        # Load all player walking sprites facing right

        image = [spriteSheet.getImage(259, 223, 35, 37),
                 spriteSheet.getImage(21, 223, 38, 37),
                 spriteSheet.getImage(64, 222, 40, 38),
                 spriteSheet.getImage(110, 221, 41, 39),
                 spriteSheet.getImage(161, 221, 40, 39),
                 spriteSheet.getImage(213, 223, 38, 37)]

        # Add sprites to list containing sprites walking right
        for item in image:
            self.walkingFramesR.append(item)
                 
        # Loop through all sprites, flip them to face left, add to list for walking left
        for item in image:
            item = pygame.transform.flip(item, True, False)
            self.walkingFramesL.append(item)


        # Punch 1 Sprites
        punchImage = [spriteSheet.getImage(30, 712, 42, 45),
                      spriteSheet.getImage(78, 713, 41, 44),
                      spriteSheet.getImage(130, 713, 40, 44),
                      spriteSheet.getImage(189, 712, 54, 43),
                      spriteSheet.getImage(252, 712, 52, 43),
                      spriteSheet.getImage(321, 712, 52, 43),
                      spriteSheet.getImage(391, 712, 52, 43),
                      spriteSheet.getImage(462, 715, 39, 42)]

        for item in punchImage:
            self.punchFrames.append(item)

        # Information for for punch sprites
        self.action = "P0"
        self.actionFrame = 0
        self.actionFrameMax = len(punchImage)

        # Set the image the player starts with
        self.image = self.walkingFramesR[0]

        # Set a reference to the image rect. This allows you to set rect.x and rect.y which is the location of the sprite
        self.rect = self.image.get_rect()
    
    def punch(self):
        # Change players action
        self.action = "P1"
            
    def update(self):
        # This function gets called 60 times per second in our main game.
        # Move left / right
        self.rect.x += self.changeX
        pos = self.rect.x

        # Change sprites to use depending on which direction player is facing
        if self.direction == "R":
            frame = (pos // 30) % len(self.walkingFramesR)
            self.image = self.walkingFramesR[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walkingFramesL)
            self.image = self.walkingFramesL[frame]
        
        # Change image to punching animations
        if self.action == "P1":
            self.actionFrame += 1
            if self.actionFrame == self.actionFrameMax:
                self.action = "P0"
                self.actionFrame = 0
            self.image = self.punchFrames[actionFrame]

            
    def goLeft(self):
        self.changeX = -3
        self.direction = "L"

    def goRight(self):
        self.changeX = 3
        self.direction = "R"

    def stop(self):
        # Call this when the user lets up a key
        self.changeX = 0

    
    




    # play punch sound

    #def slam():

    # def cheer()




       

   # def attack(self):
        # To be complete. The self here allows this method to reference attributes





    