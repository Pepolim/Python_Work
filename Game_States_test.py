import pygame
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

class Game:
    """
    The `__init__` method initializes the Game class, setting up the game window, clock, and game state manager. 
    It creates instances of the `Start` and `Level` classes, which represent the different game states, and stores them in the `states` dictionary.
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)
        
        self.states = {'start':self.start, 'level':self.level}
    
    """
    The `run()` method is the main game loop that handles the overall game logic and rendering. 
    It continuously processes user input events, updates the current game state, and refreshes the display. 
    The loop runs indefinitely until the user quits the game.
    """
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.states[self.gameStateManager.get_state()].run()
        
            pygame.display.update()
            self.clock.tick(FPS)

"""
The `Start` class represents the start state of the game. 
It is responsible for handling the game logic and rendering the start screen when the game state is set to 'start'. 
The `run()` method is called each frame to update the start state and handle user input.
"""
class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('red')
        #testing
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.gameStateManager.set_state('level')
            
"""
The `Level` class represents a game level within the `GameStateManager`. 
It is responsible for handling the game logic and rendering the level when the game state is set to 'level'. 
The `run()` method is called each frame to update the level state and handle user input.
"""
class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('blue')
        #testing
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.gameStateManager.set_state('start')
 
"""
The `GameStateManager` class is responsible for managing the current state of the game. 
It provides methods to get and set the current state, which can be used to transition between different game states (e.g. start menu, level, game over).
"""  
class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state


"""
Checks if the script is being run as the main program, rather than being imported as a module. 
This is a common pattern in Python scripts to allow them to be executed directly, while still being importable as a module.
"""
if __name__ == '__main__':
    game = Game()
    game.run()