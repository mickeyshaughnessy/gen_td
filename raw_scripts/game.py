# Import necessary modules
import pygame

# Initialize the game
pygame.init()

# Set up the game window and background color
win = pygame.display.set_mode((600, 600))
win.fill((255, 255, 255))
pygame.display.set_caption("Tower Defense")

# Load the tower image and set its rect
tower_img = pygame.image.load("tower.png")
tower_rect = tower_img.get_rect()
tower_rect.center = (400, 300)  # Set the rect's center to the center of the window

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        # Check for closing the game window
        if event.type == pygame.QUIT:
            running = False

        # Check for player clicking the mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Move the tower to the mouse position
            tower_rect.center = event.pos    
        # Check to see if the player placed towers or troops
        # Check to see if the server updated the game
        
         
    # Update the game state

    # Draw the game
    win.blit(tower_img, tower_rect)  # Draw the tower image on the game window

    # Update the display
    pygame.display.update()

# Shut down the game
#pygame.quit()

