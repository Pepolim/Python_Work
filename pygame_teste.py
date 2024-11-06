import pygame
import os

#game window
screen_width, screen_height = 900, 500

WIN = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Game")

WHITE = (255,255,255)

FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load('assets/spaceship_yellow.png')

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    # Creates a clock object to control the frame rate of the game loop.
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

"""
Executes the main function when the script is run directly (not imported as a module).
"""
if __name__ == "__main__":
    main()