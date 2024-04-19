import pygame
from display import *
from components import *

def run():
    width, height, screen = setup()
    colors = get_colors()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(colors['WHITE'])
        
        game_background(width, height, screen, colors)
        
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(30)
        
    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    print('This is the game module')
    pygame.init()
    run()