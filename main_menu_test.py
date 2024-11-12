import pygame
import button


pygame.init()

#Create the screen
SCREN_WIDTH, SCREEN_HEIGHT = 900, 500

screen = pygame.display.set_mode((SCREN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#Game variables
game_paused = False
menu_state = "main"

#Define fonts
font = pygame.font.SysFont("arialblack", 40)

#Define colors
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load('Assets/button_resume.png').convert_alpha()
back_img = pygame.image.load('Assets/button_back.png').convert_alpha()
options_img = pygame.image.load('Assets/button_options.png').convert_alpha()
quit_img = pygame.image.load('Assets/button_quit.png').convert_alpha()
audio_img = pygame.image.load('Assets/button_audio.png').convert_alpha()
video_img = pygame.image.load('Assets/button_video.png').convert_alpha()
keys_img = pygame.image.load('Assets/button_keys.png').convert_alpha()
play_img = pygame.image.load('Assets/button_play.png').convert_alpha()

#create button instances
play_button = button.Button(325, 100, play_img, 0.8)
resume_button = button.Button(304, 200, resume_img, 0.8)
options_button = button.Button(300, 300, options_img, 0.8)
back_button = button.Button(325, 400, back_img, 0.8)
quit_button = button.Button(325, 400, quit_img, 0.8)

audio_button = button.Button(250, 100, audio_img, 0.8)
video_button = button.Button(250, 200, video_img, 0.8)
keys_button = button.Button(270, 300, keys_img, 0.8)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
#Game loop
run = True
while run:
    
    screen.fill((52, 78, 91))

    #check if game is paused
    if game_paused:
        #check menu state
        if menu_state == "main":
            # draw pause screen buttons
            # see if button has been pressed
            if play_button.draw(screen):
                print("play")   
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
                #game_paused = False
                #pygame_teste.main()
                
        #check if options menu is open
        elif menu_state == "options":
            # draw pause screen buttons
            # see if button has been pressed
            if video_button.draw(screen):
                print("video")
            if audio_button.draw(screen):
                print("audio")
            if keys_button.draw(screen):
                print("keys")
            if back_button.draw(screen):
                menu_state = "main"
                
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, SCREN_WIDTH/2 - 250, SCREEN_HEIGHT/2 - 50)
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
    
    pygame.display.update()
    
pygame.quit()