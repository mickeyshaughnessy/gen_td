# Import necessary modules
import pygame

# Initialize the game
pygame.init()

# Set up the game window and background color
win = pygame.display.set_mode((800, 600))
win.fill((255, 255, 255))
pygame.display.set_caption("Tower Defense")

# Load the tower image and set its rect
tower_img = pygame.image.load("tower.png")
tower_rect = tower_img.get_rect()

# Set the initial position of the tower
tower_pos = (400, 300)
tower_rect.center = tower_pos  # Set the rect's center to the initial position

# Set the speed of the tower
tower_speed = 2

import random

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        # Check for closing the game window
        if event.type == pygame.QUIT:
            running = False

    # Update the game state
    if random.random() > 0.5:
        tower_pos = (tower_pos[0] + tower_speed, tower_pos[1] + tower_speed)  # Move the tower to the right
    else: 
        tower_pos = (tower_pos[0] - tower_speed, tower_pos[1] - tower_speed)  # Move the tower to the right
    tower_rect.center = tower_pos  # Set the rect's center to the updated position

    # Draw the game
    win.blit(tower_img, tower_rect)  # Draw the tower image on the game window

    # Update the display
    pygame.display.update()

# Shut down the game
#pygame.quit()

