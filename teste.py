import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blocking Object Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player setup
player_width, player_height = 50, 50
player = pygame.Rect(100, 100, player_width, player_height)
player_speed = 5

# Blocking object setup
block = pygame.Rect(300, 200, 100, 100)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Move left
        player.x -= player_speed
        # Check for collision and undo movement if colliding
        if player.colliderect(block):
            player.x += player_speed  # Undo movement
    elif keys[pygame.K_d]:  # Move right
        player.x += player_speed
        # Check for collision and undo movement if colliding
        if player.colliderect(block):
            player.x -= player_speed
    if keys[pygame.K_w]:  # Move up
        player.y -= player_speed
        # Check for collision and undo movement if colliding
        if player.colliderect(block):
            player.y += player_speed
    elif keys[pygame.K_s]:  # Move down
        player.y += player_speed
        # Check for collision and undo movement if colliding
        if player.colliderect(block):
            player.y -= player_speed

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)  # Draw player
    pygame.draw.rect(screen, RED, block)   # Draw block

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
