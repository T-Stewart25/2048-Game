import pygame
import sys
import random
from display import *
from components import *

def run():
    # Get start values
    width, height, screen = setup()
    colors = get_colors()
    boxColors = get_box_colors()
    locations = get_locations(width, height)
    score = 0
    
    # Choose a random index initially
    index = random.randint(0, 8)
    overall_Locations = locations
    locations = {locations[index]: [index,2]}
    
    # Run the game
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the boxes to the right
                    locations = move_right(locations, overall_Locations)
                    # Check if the game is over
                    if game_over(locations, overall_Locations):
                        running = False
                elif event.key == pygame.K_LEFT:
                    # Move the boxes to the left
                    locations = move_left(locations, overall_Locations)
                    # Check if the game is over
                    if game_over(locations, overall_Locations):
                        running = False
                elif event.key == pygame.K_UP:
                    # Move the boxes up
                    locations = move_up(locations, overall_Locations)
                    # Check if the game is over
                    if game_over(locations, overall_Locations):
                        running = False
                elif event.key == pygame.K_DOWN:
                    # Move the boxes down
                    locations = move_down(locations, overall_Locations)
                    # Check if the game is over
                    if game_over(locations, overall_Locations):
                        running = False

        # Clear the screen
        screen.fill(colors['WHITE'])
        
        game_background(width, height, screen, colors)
        
        draw_score(screen, colors, width, height, score)
        
        draw_boxes(screen, colors, locations, width, boxColors)
        
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
