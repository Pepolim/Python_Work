import pygame
import os
pygame.init()

#pygame.font.init()
#pygame.mixer.init()


#game window
screen_width, screen_height = 900, 500

WIN = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Game")

"""
Constants for the game:
"""
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(screen_width//2 - 5, 0, 10, screen_height)


BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

VOLUME = 0.2
BULLET_HIT_SOUND.set_volume(VOLUME)
BULLET_FIRE_SOUND.set_volume(VOLUME)


HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

#A custom pygame event that is posted when the spaceship is hit by a bullet.
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# os.path.join() is used to join the path of the image file with the current directory path. Works across all operating systems.
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (screen_width, screen_height))

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (screen_width - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()

# yellow movement
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < screen_height - 15: # DOWW
        yellow.y += VEL
        
# red movement
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < screen_width: # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < screen_height - 15 : # DOWW
        red.y += VEL
      
"""
    Handles the movement and collision detection of bullets fired by the yellow and red spaceships.
    
    For each bullet in the yellow_bullets list:
    - Moves the bullet to the right by the BULLET_VEL constant.
    - Checks if the bullet collides with the red spaceship. If so, posts a pygame.USEREVENT event and removes the bullet from the yellow_bullets list.
    - Checks if the bullet has gone off the right side of the screen. If so, removes the bullet from the yellow_bullets list.
"""
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > screen_width:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (screen_width/2 - draw_text.get_width()/2, screen_height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)


# MAIN function
def main():
    yellow = pygame.Rect(150, 220, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(750, 220, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    yellow_bullets = []
    red_bullets = []
    
    yellow_health = 10
    red_health = 10
    
    # Creates a clock object to control the frame rate of the game loop.
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                        yellow_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()
                        # print(bullets)
                    if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                        red_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()
                        # print(bullets)
                    
                        
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
                # print(red_health)
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
                # print(yellow_health)
                
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        
        if winner_text != "":
            draw_winner(winner_text)
            break
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()
    
    #pygame.quit()
"""
Executes the main function when the script is run directly (not imported as a module).
"""
if __name__ == "__main__":
    main()