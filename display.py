import pygame
import sys

def setup():
    # Set up the screen dimensions
    screen_width = 600
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("2048")
    return screen_width, screen_height, screen

def get_colors():
    # Set up colors
    colors = {
        'WHITE': (255, 255, 255),
        'BLUE': (0, 0, 255),
        'BLACK': (0, 0, 0),
    }
    return colors

def get_box_colors():
    boxColors = value_colors = {
        2: (128, 0, 0),
        4: (200, 200, 100),
        8: (255, 0, 0),
        16: (0, 255, 0),
        32: (0, 0, 255),
        64: (255, 0, 255),
        128: (255, 128, 0),
        256: (0, 255, 255),
        512: (128, 0, 255),
        1024: (255, 0, 128),
        2048: (0, 128, 255),
        4096: (128, 128, 128),
        8192: (128, 128, 0),
        16384: (128, 0, 128),
    }
    
    return boxColors

def get_locations(width, height):
    box_width = width * 0.85
    box_height = height * 0.75
    box_x = (width - box_width) // 2
    box_y = (height - box_height) - height // 25
    # Calculate the locations of the grid
    locations = {}
    count = 0
    for i in range(3):
        for j in range(3):
            if j == 0:
                locations[count] = (box_x + (j * box_width // 3) - width // 65, box_y + (i * box_height // 3))
            elif j == 2:
                locations[count] = (box_x + (j * box_width // 3) + width // 65, box_y + (i * box_height // 3))
            elif j == 1:
                locations[count] = (box_x + (j * box_width // 3), box_y + (i * box_height // 3))
            count += 1
    return locations


