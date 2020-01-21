"""
Pygame base template for opening a window, done with functions
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import constants
import spritesheetFunctions
import character

def main():
    """ Main function for the game. """
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    
    screen = pygame.display.set_mode([constants.screenWidth, constants.screenHeight])
 
    pygame.display.set_caption("Donkey Kong Country")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create the player
    player = Player()

    # Create sprite groups
    allSpriteList = pygame.sprite.Group()

    # Add sprite to spriteList
    allSpriteList.add(player)
 
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(constants.WHITE)
        allSpriteList.draw()

        
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
 
if __name__ == "__main__":
    main()