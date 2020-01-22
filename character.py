import pygame

from spritesheetFunctions import SpriteSheet

# Use constants to define the sprites you want from the sheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Set speed vectors
        self.changeX = 0
        self.changeY = 0
        
        # This holds all images for the animated walk left/right of our player
        self.walkingFramesL = []
        self.walkingFramesR = []

        # List to hold punch animation
        self.punchFramesR = []
        self.punchFramesL = []
 
        # Initilize list to hold spin sprites
        self.spinFrames = []

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
            item = pygame.transform.scale2x(item)
            self.walkingFramesR.append(item)
                 
        # Loop through all sprites, flip them to face left, add to list for walking left
        for item in image:
            item = pygame.transform.flip(item, True, False)
            item = pygame.transform.scale2x(item)
            self.walkingFramesL.append(item)

        # Punch Right Sprites. Duplicated to slow down animation.
        punchImage = [spriteSheet.getImage(30, 712, 42, 45),
                      spriteSheet.getImage(30, 712, 42, 45),
                      spriteSheet.getImage(78, 713, 41, 44),
                      spriteSheet.getImage(78, 713, 41, 44),
                      spriteSheet.getImage(130, 713, 40, 44),
                      spriteSheet.getImage(130, 713, 40, 44),
                      spriteSheet.getImage(189, 712, 54, 43),
                      spriteSheet.getImage(189, 712, 54, 43),
                      spriteSheet.getImage(252, 712, 52, 43),
                      spriteSheet.getImage(252, 712, 52, 43),
                      spriteSheet.getImage(321, 712, 52, 43),
                      spriteSheet.getImage(321, 712, 52, 43),
                      spriteSheet.getImage(391, 712, 52, 43),
                      spriteSheet.getImage(391, 712, 52, 43),
                      spriteSheet.getImage(462, 715, 39, 42),
                      spriteSheet.getImage(462, 715, 39, 42)
                      ]

        # Information for for punch sprites
        self.action = "P0"
        self.actionFrame = 0
        self.actionFrameMax = len(punchImage)

        # Add punch right sprites to list
        for item in punchImage:
            item = pygame.transform.scale2x(item)
            self.punchFramesR.append(item)

        # Flip punch sprites and add to punch left list
        for item in punchImage:
            item = pygame.transform.flip(item, True, False)
            item = pygame.transform.scale2x(item)
            self.punchFramesL.append(item)

        spinImage = [spriteSheet.getImage(600, 2086, 33, 44),
                     spriteSheet.getImage(600, 2086, 33, 44),
                     spriteSheet.getImage(645, 2085, 52, 45),
                     spriteSheet.getImage(645, 2085, 52, 45),
                     spriteSheet.getImage(710, 2082, 66, 47),
                     spriteSheet.getImage(710, 2082, 66, 47),
                     spriteSheet.getImage(780, 2082, 65, 47),
                     spriteSheet.getImage(780, 2082, 65, 47),
                     spriteSheet.getImage(855, 2082, 64, 47),
                     spriteSheet.getImage(855, 2082, 64, 47),
                     spriteSheet.getImage(933, 2082, 64, 47),
                     spriteSheet.getImage(933, 2082, 64, 47),
                     spriteSheet.getImage(1007, 2082, 65, 47),
                     spriteSheet.getImage(1007, 2082, 65, 47),
                     spriteSheet.getImage(1076, 2082, 66, 47),
                     spriteSheet.getImage(1076, 2082, 66, 47),
                     spriteSheet.getImage(1206, 2083, 33, 44),
                     spriteSheet.getImage(1206, 2083, 33, 44)
                    ]

        # Information for spin sprites
        self.spinAction = "S0"
        self.spinFrame = 0
        self.spinFrameMax = len(spinImage)

        for item in spinImage:
            item = pygame.transform.scale2x(item)
            self.spinFrames.append(item)

       
        # Set the image the player starts with
        self.image = self.walkingFramesR[0]

        # Set a reference to the image rect. This allows you to set rect.x and rect.y which is the location of the sprite
        self.rect = self.image.get_rect()
    
    def punch(self):
        # Change players action
        self.action = "P1"

    def spin(self):
        self.spinAction = "S1"
            
    def update(self):
        # This function gets called 60 times per second in our main game.
        # Move left / right
        self.rect.x += self.changeX
        self.rect.y += self.changeY
        pos = self.rect.x

        # Change sprites to use depending on which direction player is facing
        if self.direction == "R":
            frame = (pos // 30) % len(self.walkingFramesR)
            self.image = self.walkingFramesR[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walkingFramesL)
            self.image = self.walkingFramesL[frame]

        # Change to punch animation
        if self.action == "P1" and self.direction == "R":
            self.actionFrame += 1
            if self.actionFrame == self.actionFrameMax:
                self.action = "P0"
                self.actionFrame = 0
            self.image = self.punchFramesR[self.actionFrame]        
        if self.action == "P1" and self.direction == "L":
            self.actionFrame += 1
            if self.actionFrame == self.actionFrameMax:
                self.action = "P0"
                self.actionFrame = 0
            self.image = self.punchFramesL[self.actionFrame]

        # Change to spin animation
        if self.spinAction == "S1":
            self.spinFrame += 1
            if self.spinFrame == self.spinFrameMax:
                self.spinAction = "S0"
                self.spinFrame = 0
            self.image = self.spinFrames[self.spinFrame]
            
    def goLeft(self):
        self.changeX = -4
        self.direction = "L"
        self.action = "P0"

    def goRight(self):
        self.changeX = 4
        self.direction = "R"
        self.action = "P0"

    def goDown(self):
        self.changeY = 4

    def goUp(self):
        self.changeY = -4

    def stop(self):
        # Call this when the user lets up a key
        self.changeX = 0
        self.changeY = 0

    


        

    





    #def slam():

    # def cheer()




      





    