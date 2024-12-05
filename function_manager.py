def check_next_level_collision(object1, object2, gameStateManager, reset_function, next_state):
    if object1.colliderect(object2):
        if gameStateManager.can_change_state():
            reset_function()
            gameStateManager.set_state(next_state)