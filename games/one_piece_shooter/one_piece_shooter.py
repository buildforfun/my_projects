import sys
import pygame

# Local imports
from setting import Settings
from character import Character

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
		self.character = Character(self)

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.character.update()
			self._update_screen()

			# Make the most recently drawn screen visible
			pygame.display.flip()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.character.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.character.moving_left = True
				
	
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.character.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.character.moving_left = False




	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_colour)
		self.character.blitme()


if __name__ == '__main__':
	# Make a game instance, and run the game.
	op = OnePieceShooter()
	op.run_game()






