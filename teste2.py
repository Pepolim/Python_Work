import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity and Blocking Object")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player setup
player_width, player_height = 50, 50
player = pygame.Rect(100, HEIGHT - player_height - 50, player_width, player_height)
player_speed = 5

# Gravity variables
gravity = 1  # Acceleration due to gravity
velocity_y = 0  # Vertical velocity
is_jumping = False
ground_y = HEIGHT - 50  # Ground level

# Blocking object setup
blocks = [
    pygame.Rect(300, HEIGHT - 150, 100, 100),  # block1
    pygame.Rect(500, HEIGHT - 150, 100, 100)   # block2
]



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement (horizontal)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Move left
        player.x -= player_speed
        for block in blocks:
            if player.colliderect(block):
                player.x += player_speed  # Undo movement
                break
    elif keys[pygame.K_d]:  # Move right
        player.x += player_speed
        for block in blocks:
            if player.colliderect(block):
                player.x -= player_speed  # Undo movement
                break

    # Jumping
    if keys[pygame.K_SPACE] and not is_jumping:
        velocity_y = -15  # Jump force
        is_jumping = True

    # Apply gravity
    velocity_y += gravity
    player.y += velocity_y

    # Check for collisions with the ground
    if player.y + player_height >= ground_y:
        player.y = ground_y - player_height
        is_jumping = False
        velocity_y = 0

    # Check for collisions with the block (vertical)
    for block in blocks:
        if player.colliderect(block):
            if velocity_y > 0:  # Falling down
                player.y = block.y - player_height
                velocity_y = 0
                is_jumping = False
            elif velocity_y < 0:  # Jumping up
                player.y = block.y + block.height
                velocity_y = 0

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)  # Draw player
    for block in blocks:
        pygame.draw.rect(screen, RED, block)  # Draw blocks
    pygame.draw.line(screen, RED, (0, ground_y), (WIDTH, ground_y), 2)  # Ground line
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
