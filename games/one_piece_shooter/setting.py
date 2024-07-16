class Settings:
	"""A class to store all settings for One piece shooter

	Benefit: allows us to work with just one settings object any time we need to access an individual setting

	"""

	def __init__(self):
		""" Initilise the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = (230, 230, 230)

		# Character settings
		self.character_speed = 1.5
 
		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_colour = (60, 60, 60)
		



