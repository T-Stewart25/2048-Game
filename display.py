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

