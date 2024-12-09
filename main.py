import pygame
import sys
import Levels

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level1 = Levels.Level1(self.screen, self.gameStateManager)
        self.level2 = Levels.Level2(self.screen, self.gameStateManager)
        self.level3 = Levels.Level3(self.screen, self.gameStateManager)
        self.level4 = Levels.Level4(self.screen, self.gameStateManager)
        self.level5 = Levels.Level5(self.screen, self.gameStateManager)
        self.level6 = Levels.Level6(self.screen, self.gameStateManager)
        self.level7 = Levels.Level7(self.screen, self.gameStateManager)
        self.level8 = Levels.Level8(self.screen, self.gameStateManager)
        
        self.states = {'start':self.start, 'level1':self.level1, 'level2':self.level2, 
                       'level3':self.level3, 'level4':self.level4, 'level5':self.level5, 
                       'level6':self.level6, 'level7':self.level7, 'level8':self.level8}
    
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
        self.display.fill('black')
        #testing
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_r]:
            if self.gameStateManager.can_change_state():
                self.gameStateManager.set_state('level1')
 
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
