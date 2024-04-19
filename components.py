import pygame
import sys

def game_background(width, height, screen, colors):
    # Draw a blue box outline
    box_width = 550
    box_height = 550
    box_x = (width - box_width) // 2
    box_y = (height - box_height) - height // 25
    pygame.draw.rect(screen, colors['BLACK'], (box_x, box_y, box_width, box_height), width=5)  # Adjust the width as needed
    
    # Calculate y positions for the horizontal lines
    line_y1 = box_y + box_height // 3
    line_y2 = box_y + 2 * (box_height // 3)
    
    # Draw the horizontal lines
    pygame.draw.line(screen, colors['BLACK'], (box_x, line_y1), (box_x + box_width, line_y1), width=5)
    pygame.draw.line(screen, colors['BLACK'], (box_x, line_y2), (box_x + box_width, line_y2), width=5)
