import pygame
from pygame.sprite import Sprite

class Target(Sprite):
	"""A class to represent a singe target in the fleet"""
	
	def __init__(self, op_game):
		"""Initialise the target and set its starting position"""
		super().__init__()
		self.screen = op_game.screen
		
		# Load the target image and set its rect attribute
		self.image = pygame.image.load('images/pirate_ship.bmp')
		self.rect = self.image.get_rect()
		
		# Start each new target near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the target's exact horizontal position
		self.x = float(self.rect.x)






