import sys
import pygame

# Local imports
from setting import Settings

class OnePieceShooter:
	"""  """
	
	def __init__(self):
		""" Initialising the game"""
		pygame.init()
		# Make an instance of Settings
		self.settings = Settings()

		# creates window
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("One Piece Shooter")


	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			# Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			# Redraw the screen during each pass through the loop
			self.screen.fill(self.settings.bg_colour)

			# Make the most recently drawn screen visible
			pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	op = OnePieceShooter()
	op.run_game()






