import pygame
import main
from function_manager import check_next_level_collision, screen_boundry

PLAYER_SIZE = 50
PLAYER_SPEED = 8  # Reduced speed for smoother movement
ACCELERATION = 1.5  # Acceleration factor
MAX_SPEED = 13  # Maximum speed cap

GROUND_HEIGHT = 50

GRAVITY = 1 # Gravity constant
JUMP_POWER = -20 # Jump strength (negative because y-axis is inverted)

RED = (255, 0, 0)
GRAY = (128, 128, 128)

player = pygame.Rect((100,385,PLAYER_SIZE,PLAYER_SIZE))

def get_font(size): # Returns Press-Start in the desired size
    return pygame.font.Font("assets/font.ttf", size)

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
        # can show intrudoctory text
        self.show_text = True
        
        
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
    
    def run(self):
        
        self.display.fill('black')
        # Draw the ground
        pygame.draw.rect(self.display, GRAY, self.ground)  # Gray color
        # Draw the player
        pygame.draw.rect(self.display, RED, self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level2')
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
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
        screen_boundry(self.player, self.gameStateManager, self.reset_player, 'level1')
        
        # Apearing text
        if self.show_text:
            level_text = get_font(50).render(self.gameStateManager.get_state(), True, "White")
            text_rect = level_text.get_rect(center=(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2))
            self.display.blit(level_text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            self.show_text = False
        
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
        
        # can show intrudoctory text
        self.show_text = True
    
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
    
    def run(self):
        self.display.fill('black')
        
        # Draw the ground
        pygame.draw.rect(self.display, GRAY, self.ground)  # Gray color
        # Draw the player
        pygame.draw.rect(self.display, RED, self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level3')
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
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
        screen_boundry(self.player, self.gameStateManager, self.reset_player, 'level2', self.velocity_x)
        
        # Apearing text
        if self.show_text:
            level_text = get_font(50).render(self.gameStateManager.get_state(), True, "White")
            text_rect = level_text.get_rect(center=(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2))
            self.display.blit(level_text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            self.show_text = False
        
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
        
        # Blocking object setup
        self.blocks = [
            pygame.Rect(300, main.SCREEN_HEIGHT - 150, 100, 100),  # block1
            pygame.Rect(500, main.SCREEN_HEIGHT - 150, 100, 100)   # block2
        ]
        
        # Add velocity attributes
        self.velocity_x = 0
        
        self.velocity_y = 0  # Add vertical velocity
        self.gravity = GRAVITY   # Gravity constant
        self.jump_power = JUMP_POWER  # Jump strength (negative because y-axis is inverted)
        self.is_jumping = False
        
        # can show intrudoctory text
        self.show_text = True
        
    
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
        self.velocity_y = 0  # Reset vertical velocity
        self.is_jumping = False
    
    def run(self):
        self.display.fill('black')
        
        # Draw the ground
        pygame.draw.rect(self.display, GRAY, self.ground)  # Gray color
        # Draw the player
        pygame.draw.rect(self.display, RED, self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level4')
        
        for block in self.blocks:
            pygame.draw.rect(self.display, GRAY, block)  # Draw blocks

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.velocity_x -= ACCELERATION
            for block in self.blocks:
                if player.colliderect(block):
                    self.player.x += ACCELERATION  # Undo movement
                    break
        elif keys[pygame.K_d]:
            self.velocity_x += ACCELERATION
            for block in self.blocks:
                if self.player.colliderect(block):
                    player.x -= ACCELERATION  # Undo movement
                    break
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
        
        
        # Update horizontal position first
        self.player.x += self.velocity_x
        
        # Horizontal collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_x > 0:  # Moving right
                    self.player.right = block.left
                elif self.velocity_x < 0:  # Moving left
                    self.player.left = block.right
                self.velocity_x = 0
        
        # Update vertical position separately
        self.player.y += self.velocity_y
        
        # Vertical collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_y > 0:  # Moving down
                    self.player.bottom = block.top
                    self.is_jumping = False
                elif self.velocity_y < 0:  # Moving up
                    self.player.top = block.bottom
                self.velocity_y = 0
        
        
        # Ground collision
        if self.player.bottom > main.SCREEN_HEIGHT - GROUND_HEIGHT:
            self.player.bottom = main.SCREEN_HEIGHT - GROUND_HEIGHT
            self.velocity_y = 0
            self.is_jumping = False
        
        
        # Clamp velocity to maximum speed
        self.velocity_x = max(min(self.velocity_x, MAX_SPEED), -MAX_SPEED)
        
        # Keep player within screen bounds
        screen_boundry(self.player, self.gameStateManager, self.reset_player, 'level3' ,self.velocity_x)
        
        # Apearing text
        if self.show_text:
            level_text = get_font(50).render(self.gameStateManager.get_state(), True, "White")
            text_rect = level_text.get_rect(center=(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2))
            self.display.blit(level_text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            self.show_text = False
        
        pygame.display.update()


class Level4:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        # Add player
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE))  # Starting position
        # Add exit
        self.cube = pygame.Rect(1100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, 50, 50)  # Create cube with position and size
        
        
        # Blocking object setup
        self.blocks = [
            pygame.Rect(300, main.SCREEN_HEIGHT - 150, 100, 100),  # block1
            pygame.Rect(500, main.SCREEN_HEIGHT - 150, 100, 100),   # block2
            pygame.Rect(0, main.SCREEN_HEIGHT - GROUND_HEIGHT, main.SCREEN_WIDTH/2, GROUND_HEIGHT) # Add ground rectangle
        ]
        
        # Add velocity attributes
        self.velocity_x = 0
        
        self.velocity_y = 0  # Add vertical velocity
        self.gravity = GRAVITY   # Gravity constant
        self.jump_power = JUMP_POWER  # Jump strength (negative because y-axis is inverted)
        self.is_jumping = False
        
        # can show intrudoctory text
        self.show_text = True
        
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
        self.velocity_y = 0  # Reset vertical velocity
        self.is_jumping = False
    
    def run(self):
        self.display.fill('black')
        
        # Draw the player
        pygame.draw.rect(self.display, RED, self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level5')
        
        for block in self.blocks:
            pygame.draw.rect(self.display, GRAY, block)  # Draw blocks

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.velocity_x -= ACCELERATION
            for block in self.blocks:
                if player.colliderect(block):
                    self.player.x += ACCELERATION  # Undo movement
                    break
        elif keys[pygame.K_d]:
            self.velocity_x += ACCELERATION
            for block in self.blocks:
                if self.player.colliderect(block):
                    player.x -= ACCELERATION  # Undo movement
                    break
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
        
        
        # Update horizontal position first
        self.player.x += self.velocity_x
        
        # Horizontal collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_x > 0:  # Moving right
                    self.player.right = block.left
                elif self.velocity_x < 0:  # Moving left
                    self.player.left = block.right
                self.velocity_x = 0
        
        # Update vertical position separately
        self.player.y += self.velocity_y
        
        # Vertical collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_y > 0:  # Moving down
                    self.player.bottom = block.top
                    self.is_jumping = False
                elif self.velocity_y < 0:  # Moving up
                    self.player.top = block.bottom
                self.velocity_y = 0
        
        # Clamp velocity to maximum speed
        self.velocity_x = max(min(self.velocity_x, MAX_SPEED), -MAX_SPEED)
        
        # Keep player within screen bounds
        screen_boundry(self.player, self.gameStateManager, self.reset_player, 'level4', self.velocity_x)
        
        # Apearing text
        if self.show_text:
            level_text = get_font(50).render(self.gameStateManager.get_state(), True, "White")
            text_rect = level_text.get_rect(center=(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2))
            self.display.blit(level_text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            self.show_text = False
           
        pygame.display.update()

class Level5:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        # Add player
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE))  # Starting position
        
        # Add exit
        self.cube = pygame.Rect(1100, main.SCREEN_HEIGHT - GROUND_HEIGHT*12, 50, 50)  # Create cube with position and size
        
        # Blocking object setup
        self.blocks = [
            pygame.Rect(300, main.SCREEN_HEIGHT - 150, 80, 10),  # platform1
            pygame.Rect(500, main.SCREEN_HEIGHT - 300, 80, 10),  # platform2
            pygame.Rect(800, main.SCREEN_HEIGHT - 300, 80, 10),  # platform3
            pygame.Rect(250, main.SCREEN_HEIGHT - 400, 400, 10),  # platform4
            
            pygame.Rect(0, -1, main.SCREEN_WIDTH, 1), # Add celling invisible rectangle
            pygame.Rect(0, main.SCREEN_HEIGHT - GROUND_HEIGHT, main.SCREEN_WIDTH/2, GROUND_HEIGHT) # Add ground rectangle
        ]
        
        # Add velocity attributes
        self.velocity_x = 0
        
        self.velocity_y = 0  # Add vertical velocity
        self.gravity = GRAVITY   # Gravity constant
        self.jump_power = JUMP_POWER  # Jump strength (negative because y-axis is inverted)
        self.is_jumping = False
        
        # can show intrudoctory text
        self.show_text = True
    
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
        self.velocity_y = 0  # Reset vertical velocity
        self.is_jumping = False
    
    def run(self):
        self.display.fill('black')
        
        # Draw the player
        pygame.draw.rect(self.display, RED, self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level6')
        
        for block in self.blocks:
            pygame.draw.rect(self.display, GRAY, block)  # Draw blocks

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.velocity_x -= ACCELERATION
            for block in self.blocks:
                if player.colliderect(block):
                    self.player.x += ACCELERATION  # Undo movement
                    break
        elif keys[pygame.K_d]:
            self.velocity_x += ACCELERATION
            for block in self.blocks:
                if self.player.colliderect(block):
                    player.x -= ACCELERATION  # Undo movement
                    break
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
        
        
        # Update horizontal position first
        self.player.x += self.velocity_x
        
        # Horizontal collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_x > 0:  # Moving right
                    self.player.right = block.left
                elif self.velocity_x < 0:  # Moving left
                    self.player.left = block.right
                self.velocity_x = 0
        
        # Update vertical position separately
        self.player.y += self.velocity_y
        
        # Vertical collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_y > 0:  # Moving down
                    self.player.bottom = block.top
                    self.is_jumping = False
                elif self.velocity_y < 0:  # Moving up
                    self.player.top = block.bottom
                self.velocity_y = 0
        
        # Clamp velocity to maximum speed
        self.velocity_x = max(min(self.velocity_x, MAX_SPEED), -MAX_SPEED)
        
        # Keep player within screen bounds
        screen_boundry(self.player, self.gameStateManager, self.reset_player, 'level5', self.velocity_x)
        
        # Apearing text
        if self.show_text:
            level_text = get_font(50).render(self.gameStateManager.get_state(), True, "White")
            text_rect = level_text.get_rect(center=(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2))
            self.display.blit(level_text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            self.show_text = False
            
        pygame.display.update()
        
class Level6:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        # Add player
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE))  # Starting position
        
        # Add exit
        self.cube = pygame.Rect(1100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, 50, 50)  # Create cube with position and size
        
        # platform to change size
        self.size_changer = pygame.Rect(400, main.SCREEN_HEIGHT - GROUND_HEIGHT - 20, 100, 20)
        
        # Blocking object setup
        self.blocks = [
            pygame.Rect(main.SCREEN_WIDTH/2, 0, 80, main.SCREEN_HEIGHT - PLAYER_SIZE-40),  # wall
            self.size_changer,
            pygame.Rect(0, -1, main.SCREEN_WIDTH, 1), # Add celling invisible rectangle
            pygame.Rect(0, main.SCREEN_HEIGHT - GROUND_HEIGHT, main.SCREEN_WIDTH, GROUND_HEIGHT) # Add ground rectangle
        ]
        
        # Add velocity attributes
        self.velocity_x = 0
        
        self.velocity_y = 0  # Add vertical velocity
        self.gravity = GRAVITY   # Gravity constant
        self.jump_power = JUMP_POWER  # Jump strength (negative because y-axis is inverted)
        self.is_jumping = False
        
        # can show intrudoctory text
        self.show_text = True
    
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
        self.velocity_y = 0  # Reset vertical velocity
        self.is_jumping = False
        self.jump_power = JUMP_POWER
        
    def run(self):
        self.display.fill('black')
        
        # Draw the player
        pygame.draw.rect(self.display, RED, self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level7')
        
        for block in self.blocks:
            pygame.draw.rect(self.display, GRAY, block)  # Draw blocks

        pygame.draw.rect(self.display, (0, 255, 0), self.size_changer)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.velocity_x -= ACCELERATION
            for block in self.blocks:
                if player.colliderect(block):
                    self.player.x += ACCELERATION  # Undo movement
                    break
        elif keys[pygame.K_d]:
            self.velocity_x += ACCELERATION
            for block in self.blocks:
                if self.player.colliderect(block):
                    player.x -= ACCELERATION  # Undo movement
                    break
        else:
            # Deceleration when no keys are pressed
            if self.velocity_x > 0:
                self.velocity_x -= ACCELERATION
            elif self.velocity_x < 0:
                self.velocity_x += ACCELERATION
            
            # Stop completely if velocity is very small
            if abs(self.velocity_x) < ACCELERATION:
                self.velocity_x = 0
        #change size
        if self.player.bottom == self.size_changer.top and self.player.x < self.size_changer.right and self.player.right > self.size_changer.left:
            #show text above the size changer
            level_text = get_font(18).render("Press E", True, "White")
            text_rect = level_text.get_rect(center=(self.size_changer.centerx, self.size_changer.top - 65))
            self.display.blit(level_text, text_rect)
            
            if keys[pygame.K_e] and self.gameStateManager.can_change_state():
                # Size change logic here
                new_size = PLAYER_SIZE // 2 if self.player.width == PLAYER_SIZE else PLAYER_SIZE
                new_jump_power = JUMP_POWER // 1.5 if self.player.width == PLAYER_SIZE else JUMP_POWER
                bottom = self.player.bottom
                self.player.width = new_size
                self.player.height = new_size
                self.player.bottom = bottom
                self.jump_power = new_jump_power
                
                
                
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
        
        
        # Update horizontal position first
        self.player.x += self.velocity_x
        
        # Horizontal collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_x > 0:  # Moving right
                    self.player.right = block.left
                elif self.velocity_x < 0:  # Moving left
                    self.player.left = block.right
                self.velocity_x = 0
        
        # Update vertical position separately
        self.player.y += self.velocity_y
        
        # Vertical collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_y > 0:  # Moving down
                    self.player.bottom = block.top
                    self.is_jumping = False
                elif self.velocity_y < 0:  # Moving up
                    self.player.top = block.bottom
                self.velocity_y = 0
        
        
        
        # Clamp velocity to maximum speed
        if self.player.width == PLAYER_SIZE:
            self.velocity_x = max(min(self.velocity_x, MAX_SPEED), -MAX_SPEED)
        else:
            self.velocity_x = max(min(self.velocity_x, MAX_SPEED // 2), -MAX_SPEED // 2)
        
        # Keep player within screen bounds
        screen_boundry(self.player, self.gameStateManager, self.reset_player, 'level6', self.velocity_x)
        
        # Apearing text
        if self.show_text:
            level_text = get_font(50).render(self.gameStateManager.get_state(), True, "White")
            text_rect = level_text.get_rect(center=(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2))
            self.display.blit(level_text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            self.show_text = False
           
        pygame.display.update()
        
class Level7:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        # Add player
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE))  # Starting position
        
        # Add exit
        self.cube = pygame.Rect(1100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, 50, 50)  # Create cube with position and size
        # platform to change size
        self.size_changer = pygame.Rect(400, main.SCREEN_HEIGHT - GROUND_HEIGHT - 20, 100, 20)
        
        # Blocking object setup
        self.blocks = [
            pygame.Rect(main.SCREEN_WIDTH/2, 0, 80, main.SCREEN_HEIGHT - 300),  # wall
            pygame.Rect(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT - 260, 80, main.SCREEN_HEIGHT),  # wall
            self.size_changer,
            pygame.Rect(300, main.SCREEN_HEIGHT - 150, 70, 10), # Add platform
            pygame.Rect(200, main.SCREEN_HEIGHT - 230, 70, 10), # Add platform
            pygame.Rect(0, main.SCREEN_HEIGHT - 260, 70, 10),   # Add platform
            pygame.Rect(0, main.SCREEN_HEIGHT - 330, 30, 10),   # Add platform
            pygame.Rect(220, main.SCREEN_HEIGHT - 400, 70, 10), # Add platform
            pygame.Rect(420, main.SCREEN_HEIGHT - 470, 70, 10), # Add platform
            pygame.Rect(0, -1, main.SCREEN_WIDTH, 1), # Add celling "invisible" rectangle
            pygame.Rect(0, main.SCREEN_HEIGHT - GROUND_HEIGHT, main.SCREEN_WIDTH, GROUND_HEIGHT) # Add ground rectangle
        ]
        
        # Add velocity attributes
        self.velocity_x = 0
        
        self.velocity_y = 0  # Add vertical velocity
        self.gravity = GRAVITY   # Gravity constant
        self.jump_power = JUMP_POWER  # Jump strength (negative because y-axis is inverted)
        self.is_jumping = False
        
        # can show intrudoctory text
        self.show_text = True
    
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
        self.velocity_y = 0  # Reset vertical velocity
        self.is_jumping = False
        self.jump_power = JUMP_POWER
        
    def run(self):
        self.display.fill('black')
        
        # Draw the player
        pygame.draw.rect(self.display, RED, self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'level8')
        
        for block in self.blocks:
            pygame.draw.rect(self.display, GRAY, block)  # Draw blocks

        pygame.draw.rect(self.display, (0, 255, 0), self.size_changer)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.velocity_x -= ACCELERATION
            for block in self.blocks:
                if player.colliderect(block):
                    self.player.x += ACCELERATION  # Undo movement
                    break
        elif keys[pygame.K_d]:
            self.velocity_x += ACCELERATION
            for block in self.blocks:
                if self.player.colliderect(block):
                    player.x -= ACCELERATION  # Undo movement
                    break
        else:
            # Deceleration when no keys are pressed
            if self.velocity_x > 0:
                self.velocity_x -= ACCELERATION
            elif self.velocity_x < 0:
                self.velocity_x += ACCELERATION
            
            # Stop completely if velocity is very small
            if abs(self.velocity_x) < ACCELERATION:
                self.velocity_x = 0
        #change size
        if self.player.bottom == self.size_changer.top and self.player.x < self.size_changer.right and self.player.right > self.size_changer.left:
            #show text above the size changer
            level_text = get_font(18).render("Press E", True, "White")
            text_rect = level_text.get_rect(center=(self.size_changer.centerx, self.size_changer.top - 65))
            self.display.blit(level_text, text_rect)
            
            if keys[pygame.K_e] and self.gameStateManager.can_change_state():
                # Size change logic here
                new_size = PLAYER_SIZE // 2 if self.player.width == PLAYER_SIZE else PLAYER_SIZE
                new_jump_power = JUMP_POWER // 1.5 if self.player.width == PLAYER_SIZE else JUMP_POWER
                bottom = self.player.bottom
                self.player.width = new_size
                self.player.height = new_size
                self.player.bottom = bottom
                self.jump_power = new_jump_power
                
                
                
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
        
        
        # Update horizontal position first
        self.player.x += self.velocity_x
        
        # Horizontal collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_x > 0:  # Moving right
                    self.player.right = block.left
                elif self.velocity_x < 0:  # Moving left
                    self.player.left = block.right
                self.velocity_x = 0
        
        # Update vertical position separately
        self.player.y += self.velocity_y
        
        # Vertical collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_y > 0:  # Moving down
                    self.player.bottom = block.top
                    self.is_jumping = False
                elif self.velocity_y < 0:  # Moving up
                    self.player.top = block.bottom
                self.velocity_y = 0
        
        
        
        # Clamp velocity to maximum speed
        if self.player.width == PLAYER_SIZE:
            self.velocity_x = max(min(self.velocity_x, MAX_SPEED), -MAX_SPEED)
        else:
            self.velocity_x = max(min(self.velocity_x, MAX_SPEED // 2), -MAX_SPEED // 2)
        
        # Keep player within screen bounds
        screen_boundry(self.player, self.gameStateManager, self.reset_player, 'level7', self.velocity_x)
        
        # Apearing text
        if self.show_text:
            level_text = get_font(50).render(self.gameStateManager.get_state(), True, "White")
            text_rect = level_text.get_rect(center=(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2))
            self.display.blit(level_text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            self.show_text = False
            
        pygame.display.update()
        
class Level8:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        # Add player
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE))  # Starting position
        
        # Add exit
        self.cube = pygame.Rect(1100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, 50, 50)  # Create cube with position and size
        # platform to change gravity
        self.gravity_changer1 = pygame.Rect(400, main.SCREEN_HEIGHT - GROUND_HEIGHT - 20, 100, 20)
        self.gravity_changer2 = pygame.Rect(800, 0, 100, 20)
        # Blocking object setup
        self.blocks = [
            pygame.Rect(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT - 260, 80, main.SCREEN_HEIGHT),  # wall
            pygame.Rect(0, 0, main.SCREEN_WIDTH, 0),  # top
            self.gravity_changer1,
            self.gravity_changer2,
            pygame.Rect(0, -1, main.SCREEN_WIDTH, 1), # Add celling "invisible" rectangle
            pygame.Rect(0, main.SCREEN_HEIGHT - GROUND_HEIGHT, main.SCREEN_WIDTH, GROUND_HEIGHT) # Add ground rectangle
        ]
        
        # Add velocity attributes
        self.velocity_x = 0
        
        self.velocity_y = 0  # Add vertical velocity
        self.gravity = GRAVITY   # Gravity constant
        self.is_gravity_inverted = False
        self.jump_power = JUMP_POWER  # Jump strength (negative because y-axis is inverted)
        self.is_jumping = False
        
        # can show intrudoctory text
        self.show_text = True
    
    def reset_player(self):
        self.player = pygame.Rect((100, main.SCREEN_HEIGHT - GROUND_HEIGHT*2, PLAYER_SIZE, PLAYER_SIZE)) # Reset to starting position
        self.velocity_x = 0  # Reset velocity when resetting player
        self.velocity_y = 0  # Reset vertical velocity
        self.is_jumping = False
        self.jump_power = JUMP_POWER
        self.is_gravity_inverted = False
        self.gravity = GRAVITY
        
    def run(self):
        self.display.fill('black')
        
        # Draw the player
        pygame.draw.rect(self.display, RED, self.player)
        # Draw the exit
        pygame.draw.rect(self.display, (255,255,0), self.cube)
        
        check_next_level_collision(self.player, self.cube, self.gameStateManager, self.reset_player, 'start')
        
        for block in self.blocks:
            pygame.draw.rect(self.display, GRAY, block)  # Draw blocks

        pygame.draw.rect(self.display, (0, 255, 255), self.gravity_changer1)
        pygame.draw.rect(self.display, (0, 255, 255), self.gravity_changer2)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.velocity_x -= ACCELERATION
            for block in self.blocks:
                if player.colliderect(block):
                    self.player.x += ACCELERATION  # Undo movement
                    break
        elif keys[pygame.K_d]:
            self.velocity_x += ACCELERATION
            for block in self.blocks:
                if self.player.colliderect(block):
                    player.x -= ACCELERATION  # Undo movement
                    break
        else:
            # Deceleration when no keys are pressed
            if self.velocity_x > 0:
                self.velocity_x -= ACCELERATION
            elif self.velocity_x < 0:
                self.velocity_x += ACCELERATION
            
            # Stop completely if velocity is very small
            if abs(self.velocity_x) < ACCELERATION:
                self.velocity_x = 0
        #change gravity
        if ((self.player.bottom == self.gravity_changer1.top and self.player.x < self.gravity_changer1.right and self.player.right > self.gravity_changer1.left) or 
            (self.player.top == self.gravity_changer2.bottom and self.player.x < self.gravity_changer2.right and self.player.right > self.gravity_changer2.left)):
            
            if (self.player.bottom == self.gravity_changer1.top and self.player.x < self.gravity_changer1.right and self.player.right > self.gravity_changer1.left):
                #show text above the size changer
                level_text = get_font(18).render("Press E", True, "White")
                text_rect = level_text.get_rect(center=(self.gravity_changer1.centerx, self.gravity_changer1.top - 65))
                self.display.blit(level_text, text_rect)
            
            if keys[pygame.K_e] and self.gameStateManager.can_change_state():
                self.is_gravity_inverted = not self.is_gravity_inverted
                self.gravity = -GRAVITY if self.is_gravity_inverted else GRAVITY
                self.jump_power = -JUMP_POWER if self.is_gravity_inverted else JUMP_POWER
                
                  
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
        
        
        # Update horizontal position first
        self.player.x += self.velocity_x
        
        # Horizontal collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.velocity_x > 0:  # Moving right
                    self.player.right = block.left
                elif self.velocity_x < 0:  # Moving left
                    self.player.left = block.right
                self.velocity_x = 0
        
        # Update vertical position separately
        self.player.y += self.velocity_y
        
        # Vertical collision check
        for block in self.blocks:
            if self.player.colliderect(block):
                if self.is_gravity_inverted:
                    if self.velocity_y < 0:  # Moving up when inverted
                        self.player.top = block.bottom
                        self.is_jumping = False
                    elif self.velocity_y > 0:  # Moving down when inverted
                        self.player.bottom = block.top
                else:
                    if self.velocity_y > 0:  # Moving down normally
                        self.player.bottom = block.top
                        self.is_jumping = False
                    elif self.velocity_y < 0:  # Moving up normally
                        self.player.top = block.bottom
                self.velocity_y = 0
        
        
        
       
        
        # Clamp velocity to maximum speed
        if self.player.width == PLAYER_SIZE:
            self.velocity_x = max(min(self.velocity_x, MAX_SPEED), -MAX_SPEED)
        else:
            self.velocity_x = max(min(self.velocity_x, MAX_SPEED // 2), -MAX_SPEED // 2)
        
        # Keep player within screen bounds
        screen_boundry(self.player, self.gameStateManager, self.reset_player, 'level8', self.velocity_x)
        
        # Apearing text
        if self.show_text:
            level_text = get_font(50).render(self.gameStateManager.get_state(), True, "White")
            text_rect = level_text.get_rect(center=(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2))
            self.display.blit(level_text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            self.show_text = False
           
        pygame.display.update()
        