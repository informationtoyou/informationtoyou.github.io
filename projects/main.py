import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cat Running")

# Load the cat sprite
cat_image = pygame.image.load("Scratchcat.png")  # Make sure you have an image of the cat

# Set up initial cat position and movement variables
cat_x = 0
cat_speed = 5
moving_right = True
round_trip = 0

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update cat position
    if moving_right:
        cat_x += cat_speed
    else:
        cat_x -= cat_speed

    # Check if the cat reaches the right end
    if cat_x >= SCREEN_WIDTH:
        moving_right = False
        round_trip += 1
    elif cat_x <= 0:
        moving_right = True
        if round_trip > 0:
            print("Meow")  # Print "Meow" after each round trip

    # Blit the cat on the screen
    screen.blit(cat_image, (cat_x, 300))  # 300 is the y-coordinate for the floor

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
