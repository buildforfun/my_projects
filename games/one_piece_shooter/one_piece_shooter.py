import sys
import pygame

# Local imports
from setting import Settings
from character import Character
from bullet import Bullet

class OnePieceShooter:
	"""  """
	
	def __init__(self):
		""" Initialising the game"""
		pygame.init()
		# Make an instance of Settings
		self.settings = Settings()

		# creates window
		self.screen = pygame.display.set_mode((900, 450))
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("One Piece Shooter")
		self.character = Character(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self.screen.fill([0,0,0])
			self._check_events()
			self.character.update()
			self.bullets.update()
			self._update_screen()

			# Make the most recently drawn screen visible
			pygame.display.flip()
			

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
	

	def _check_keydown_events(self, event):				
		if event.key == pygame.K_RIGHT:
			self.character.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.character.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
				
	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.character.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.character.moving_left = False


	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	
	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_colour)
		self.character.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	op = OnePieceShooter()
	op.run_game()






