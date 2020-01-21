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
from character import Player



def main():
    """ Main function for the game. """
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    
    screen = pygame.display.set_mode([constants.screenWidth, constants.screenHeight])
 
    pygame.display.set_caption("Donkey Kong Country")

    # Create the player
    player = Player()
    
    # Create Sprite Group
    allSpritesList = pygame.sprite.Group()

    # Add player sprite to list of all sprites
    allSpritesList.add(player)

    player.rect.x = 350
    player.rect.y = 450


    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # If user presses a key down
            elif event.type == pygame.KEYDOWN:
                # Figure what key it was, adjust change_x
                if event.key == pygame.K_RIGHT:
                    player.goRight()
                if event.key == pygame.K_LEFT:
                    player.goLeft()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.punch()
            
            # If user lets up a key
            elif event.type == pygame.KEYUP:
                # If an arrow key, reset vector
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.stop()
                
        


        

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        allSpritesList.update()
 
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(constants.WHITE)
        allSpritesList.draw(screen)


        
 
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