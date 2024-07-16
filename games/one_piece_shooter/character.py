import pygame

class Character:
	""" A class that represents the Character"""

	def __init__(self, op_game):
		"""Initialises the character and sets it's original position"""
		self.screen = op_game.screen
		self.screen_rect = op_game.screen.get_rect()

		# Load character image and get its rect
		self.image = pygame.image.load('images/luffy.bmp')
		self.rect = self.image.get_rect()

		# Movement flag
		self.moving_right = False
		self.moving_left = False

		# Start each new character at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

	def update(self):
		"""Update the character's position based on the movement flag."""
		if self.moving_right:
			self.rect.x += 1
		if self.moving_left:
			self.rect.x -= 1	

	def blitme(self):
		"""Draw the character at its current location"""
		self.screen.blit(self.image, self.rect)


