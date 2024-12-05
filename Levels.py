import pygame
import main
from function_manager import check_next_level_collision


PLAYER_SIZE = 50
PLAYER_SPEED = 8  # Reduced speed for smoother movement
ACCELERATION = 1.5  # Acceleration factor
MAX_SPEED = 13  # Maximum speed cap

GROUND_HEIGHT = 50

GRAVITY = 1 # Gravity constant
JUMP_POWER = -20 # Jump strength (negative because y-axis is inverted)

player = pygame.Rect((100,385,PLAYER_SIZE,PLAYER_SIZE))

def screen_boundry(player, velocity_x = 0):
# Keep player within screen bounds
    if player.left < 0:
        player.left = 0
        velocity_x = 0  # Stop momentum when hitting wall
    elif player.right > main.SCREEN_WIDTH:
        player.right = main.SCREEN_WIDTH
        velocity_x = 0  # Stop momentum when hitting wall

class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        # Add player
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE))  # Starting position
        # Add exit
        self.cube = pygame.Rect(1100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, 50, 50)  # Create cube with position and size
        # Add ground rectangle
        self.ground = pygame.Rect(0, main.SCREEN_HEIGHT - GROUND_HEIGHT, main.SCREEN_WIDTH, GROUND_HEIGHT)
        
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        
    
    def run(self):
        self.display.fill('black')
        # Draw the ground
        pygame.draw.rect(self.display, (100, 100, 100), self.ground)  # Gray color
        # Draw the player
        pygame.draw.rect(self.display, (255,0,0), self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level2')
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.player.x -= PLAYER_SPEED + 5
        elif keys[pygame.K_d]:
            self.player.x += PLAYER_SPEED + 5
        """
        elif keys[pygame.K_w]:
            self.player.y -= PLAYER_SPEEED
        elif keys[pygame.K_s]:
            self.player.y += PLAYER_SPEEED
        """
        # Keep player within screen bounds
        screen_boundry(self.player)

        pygame.display.update()
        

class Level2:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        # Add player
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE))  # Starting position
        # Add exit
        self.cube = pygame.Rect(1100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, 50, 50)  # Create cube with position and size
        # Add ground rectangle
        self.ground = pygame.Rect(0, main.SCREEN_HEIGHT - GROUND_HEIGHT, main.SCREEN_WIDTH, GROUND_HEIGHT)
        
        # Add velocity attributes
        self.velocity_x = 0
    
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
    
    def run(self):
        self.display.fill('black')
        
        # Draw the ground
        pygame.draw.rect(self.display, (100, 100, 100), self.ground)  # Gray color
        # Draw the player
        pygame.draw.rect(self.display, (255,0,0), self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level3')
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.velocity_x -= ACCELERATION
        elif keys[pygame.K_d]:
            self.velocity_x += ACCELERATION
        else:
            # Deceleration when no keys are pressed
            if self.velocity_x > 0:
                self.velocity_x -= ACCELERATION
            elif self.velocity_x < 0:
                self.velocity_x += ACCELERATION
            
            # Stop completely if velocity is very small
            if abs(self.velocity_x) < ACCELERATION:
                self.velocity_x = 0
                
        # Clamp velocity to maximum speed
        self.velocity_x = max(min(self.velocity_x, MAX_SPEED), -MAX_SPEED)
        
        # Apply velocity to position
        self.player.x += self.velocity_x
        
        # Keep player within screen bounds
        screen_boundry(self.player, self.velocity_x)
            
        pygame.display.update()
        


class Level3:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        # Add player
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE))  # Starting position
        # Add exit
        self.cube = pygame.Rect(1100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, 50, 50)  # Create cube with position and size
        # Add ground rectangle
        self.ground = pygame.Rect(0, main.SCREEN_HEIGHT - GROUND_HEIGHT, main.SCREEN_WIDTH, GROUND_HEIGHT)
        
        # Add velocity attributes
        self.velocity_x = 0
        
        self.velocity_y = 0  # Add vertical velocity
        self.gravity = GRAVITY   # Gravity constant
        self.jump_power = JUMP_POWER  # Jump strength (negative because y-axis is inverted)
        self.is_jumping = False
        
    
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
        self.velocity_y = 0  # Reset vertical velocity
        self.is_jumping = False
    
    def run(self):
        self.display.fill('black')
        
        # Draw the ground
        pygame.draw.rect(self.display, (100, 100, 100), self.ground)  # Gray color
        # Draw the player
        pygame.draw.rect(self.display, (255,0,0), self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'start')
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.velocity_x -= ACCELERATION
        elif keys[pygame.K_d]:
            self.velocity_x += ACCELERATION
        else:
            # Deceleration when no keys are pressed
            if self.velocity_x > 0:
                self.velocity_x -= ACCELERATION
            elif self.velocity_x < 0:
                self.velocity_x += ACCELERATION
            
            # Stop completely if velocity is very small
            if abs(self.velocity_x) < ACCELERATION:
                self.velocity_x = 0
                
        # Jump when space is pressed and not already jumping
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = self.jump_power
            self.is_jumping = True
        
        # Handle horizontal deceleration
        if not (keys[pygame.K_a] or keys[pygame.K_d]):
            if self.velocity_x > 0:
                self.velocity_x -= ACCELERATION
            elif self.velocity_x < 0:
                self.velocity_x += ACCELERATION
            if abs(self.velocity_x) < ACCELERATION:
                self.velocity_x = 0
        
        # Apply gravity
        self.velocity_y += self.gravity
        
        # Update positions
        self.player.x += self.velocity_x
        self.player.y += self.velocity_y
        
        # Ground collision
        if self.player.bottom > main.SCREEN_HEIGHT - GROUND_HEIGHT:
            self.player.bottom = main.SCREEN_HEIGHT - GROUND_HEIGHT
            self.velocity_y = 0
            self.is_jumping = False
        
        
        # Clamp velocity to maximum speed
        self.velocity_x = max(min(self.velocity_x, MAX_SPEED), -MAX_SPEED)
        
        # Keep player within screen bounds
        screen_boundry(self.player, self.velocity_x)
            
        pygame.display.update()