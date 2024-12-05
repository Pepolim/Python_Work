import pygame
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)
        
        self.states = {'start':self.start, 'level':self.level}
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.states[self.gameStateManager.get_state()].run()
        
            pygame.display.update()
            self.clock.tick(FPS)

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
    def run(self):
        self.display.fill('red')
        #testing
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_r]:
            if self.gameStateManager.can_change_state():
                self.gameStateManager.set_state('level')
            
player = pygame.Rect((485,385,30,30))

class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.player = pygame.Rect((485, 385, 30, 30))  # Starting position
    
    def reset_player(self):
        self.player = pygame.Rect((485, 385, 30, 30))  # Reset to starting position
    
    def run(self):
        self.display.fill('blue')
        #testing
        
        pygame.draw.rect(self.display, (255,0,0), self.player)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if self.gameStateManager.can_change_state():
                self.reset_player()
                self.gameStateManager.set_state('start')
        elif keys[pygame.K_a]:
            self.player.x -= 10
        elif keys[pygame.K_d]:
            self.player.x += 10
        elif keys[pygame.K_w]:
            self.player.y -= 10
        elif keys[pygame.K_s]:
            self.player.y += 10
        
        pygame.display.update()
 
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
        # Add a cooldown for state changes
        self.last_state_change = 0
        self.state_cooldown = 300
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state
    def can_change_state(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_state_change >= self.state_cooldown:
            self.last_state_change = current_time
            return True
        return False

if __name__ == '__main__':
    game = Game()
    game.run()