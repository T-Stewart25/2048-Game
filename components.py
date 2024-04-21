import pygame

def game_background(width, height, screen, colors):
    # Draw a blue box outline
    box_width = width * 0.9
    box_height = height * 0.7857
    box_x = (width - box_width) // 2
    box_y = (height - box_height) - height // 25
    pygame.draw.rect(screen, colors['BLACK'], (box_x, box_y, box_width, box_height), width=5) 
    
    # Calculate y positions for the horizontal lines
    line_y1 = box_y + box_height // 3
    line_y2 = box_y + 2 * (box_height // 3)
    # Calculate x positions for the vertical lines
    line_x1 = box_x + box_width // 3
    line_x2 = box_x + 2 * (box_width // 3)
    
    # Draw the lines
    pygame.draw.line(screen, colors['BLACK'], (box_x, line_y1), (box_x + box_width - 1 , line_y1), width=5)
    pygame.draw.line(screen, colors['BLACK'], (box_x, line_y2), (box_x + box_width -1, line_y2), width=5)
    pygame.draw.line(screen, colors['BLACK'], (line_x1, box_y), (line_x1, box_y + box_height - 1), width=5)
    pygame.draw.line(screen, colors['BLACK'], (line_x2, box_y), (line_x2, box_y + box_height - 1), width=5)

 
def draw_score(screen, colors, width, height, score):
    font = pygame.font.Font(None, width // 7)
    text = font.render(f'Score: {score}', True, colors['BLACK'])
    screen.blit(text, ((width - (width * 0.85)), height // 20))
    
def draw_boxes(screen, colors, locations, width, boxColor):
    for location, value in locations.items():
        box_width = width * 0.85 // 3
        box_height = (width * 0.85 // 3) * 0.9
        box_x = location[0]
        box_y = location[1]
        pygame.draw.rect(screen, boxColor[value[1]], (box_x, box_y, box_width, box_height))
        
        # Draw the number
        font = pygame.font.Font(None, width // 7)
        text = font.render(str(value[1]), True, colors['WHITE'])  # Use the value from the dictionary
        text_rect = text.get_rect(center=(box_x + box_width // 2, box_y + box_height // 2))
        screen.blit(text, text_rect)
        
        # Draw the box outline
        pygame.draw.rect(screen, colors['BLACK'], (box_x, box_y, box_width, box_height), width=5)

def move_right(locations, overall_Locations):
    new_locations = {}
    keys = list(overall_Locations.keys())
    # Iterate through each row
    for location, value in locations.items():
        if value[0] in [0, 1, 2]:
            location = overall_Locations[value[0]]
            value = value
            for i in [0, 1, 2]:
                if overall_Locations[i] not in locations and i > value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
        elif value[0] in [3, 4, 5]:
            location = overall_Locations[value[0]]
            value = value
            for i in [3,4,5]:
                if overall_Locations[i] not in locations and i > value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
        elif value[0] in [6,7,8]:
            location = overall_Locations[value[0]]
            value = value
            for i in [6,7,8]:
                if overall_Locations[i] not in locations and i > value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
    return new_locations

def move_left(locations, overall_Locations):
    new_locations = {}
    keys = list(overall_Locations.keys())
    # Iterate through each row
    for location, value in locations.items():
        if value[0] in [2,1,0]:
            location = overall_Locations[value[0]]
            value = value
            for i in [2,1,0]:
                if overall_Locations[i] not in locations and i < value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
        elif value[0] in [5,4,3]:
            location = overall_Locations[value[0]]
            value = value
            for i in [5,4,3]:
                if overall_Locations[i] not in locations and i < value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
        elif value[0] in [8,7,6]:
            location = overall_Locations[value[0]]
            value = value
            for i in [8,7,6]:
                if overall_Locations[i] not in locations and i < value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
    return new_locations

def move_up(locations, overall_Locations):
    new_locations = {}
    keys = list(overall_Locations.keys())
    # Iterate through each row
    for location, value in locations.items():
        if value[0] in [6,3,0]:
            location = overall_Locations[value[0]]
            value = value
            for i in [6,3,0]:
                if overall_Locations[i] not in locations and i < value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
        elif value[0] in [7,4,1]:
            location = overall_Locations[value[0]]
            value = value
            for i in [7,4,1]:
                if overall_Locations[i] not in locations and i < value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
        elif value[0] in [8,5,2]:
            location = overall_Locations[value[0]]
            value = value
            for i in [8,5,2]:
                if overall_Locations[i] not in locations and i < value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
    return new_locations

def move_down(locations, overall_Locations):
    new_locations = {}
    keys = list(overall_Locations.keys())
    # Iterate through each row
    for location, value in locations.items():
        if value[0] in [0,3,6]:
            location = overall_Locations[value[0]]
            value = value
            for i in [0,3,6]:
                if overall_Locations[i] not in locations and i > value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
        elif value[0] in [1 , 4, 7]:
            location = overall_Locations[value[0]]
            value = value
            for i in [1,4,7]:
                if overall_Locations[i] not in locations and i > value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
        elif value[0] in [2,5,8]:
            location = overall_Locations[value[0]]
            value = value
            for i in [2,5,8]:
                if overall_Locations[i] not in locations and i > value[0]:
                    location = overall_Locations[i]
                    value = [i, value[1]]
            new_locations[location] = value
    return new_locations



def game_over(locations, overall_Locations):
    if len(locations) == 9:
        return True
    return False