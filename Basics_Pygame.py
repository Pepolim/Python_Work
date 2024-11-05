import pygame


pygame.init()

#game window
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

#Rect(x,y,width,height)
player = pygame.Rect((485,385,30,30))

#game loop
run = True
while run:
    #refresh the screen background
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,0,0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.x -= 1
    elif key[pygame.K_d]:
        player.x += 1
    elif key[pygame.K_w]:
        player.y -= 1
    elif key[pygame.K_s]:
        player.y += 1
    
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #refresh screen
    pygame.display.update()
pygame.quit()
