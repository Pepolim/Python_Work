import main
import Levels


def get_font(size): # Returns Press-Start in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def check_next_level_collision(object1, object2, gameStateManager, reset_function, next_state):
    if object1.colliderect(object2):
        if gameStateManager.can_change_state():
            reset_function()
            gameStateManager.set_state(next_state)
            
def screen_boundry(player, gameStateManager, reset_function, next_state, velocity_x = 0):
# Keep player within screen bounds
    if player.left < 0:
        player.left = 0
        velocity_x = 0  # Stop momentum when hitting wall
    elif player.right > main.SCREEN_WIDTH:
        player.right = main.SCREEN_WIDTH
        velocity_x = 0  # Stop momentum when hitting wall
    elif player.bottom > main.SCREEN_HEIGHT + (Levels.PLAYER_SIZE * 10 ):
        reset_function()
        gameStateManager.set_state(next_state)
        
