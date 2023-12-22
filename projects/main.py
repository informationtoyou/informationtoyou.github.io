import pygame
import random
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_SIZE = 30
TARGET_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aim Trainer")

# Functions
def spawn_target():
    x = random.randint(TARGET_SIZE, SCREEN_WIDTH - TARGET_SIZE)
    y = random.randint(TARGET_SIZE, SCREEN_HEIGHT - TARGET_SIZE)
    return x, y

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Game variables
targets = []
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for target in targets:
                if distance(target[0], target[1], event.pos[0], event.pos[1]) < TARGET_SIZE:
                    targets.remove(target)
                    score += 1

    if len(targets) < 5:
        targets.append(spawn_target())

    screen.fill(BACKGROUND_COLOR)

    for target in targets:
        pygame.draw.circle(screen, TARGET_COLOR, target, TARGET_SIZE)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
