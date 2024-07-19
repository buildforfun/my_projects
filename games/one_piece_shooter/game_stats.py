class GameStats:
    """Track statistics for One Piece shooter"""

    def __init__(self, op_game):
        """Initialise stats"""
        self.settings = op_game.settings
        self.reset_stats()
        
        # Start One Piece in active state
        self.game_active = True


    def reset_stats(self):
        """Initialise stats that can change during the game"""
        self.characters_left = self.settings.character_limit
