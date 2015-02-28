import pygame
from graphics import *

# Classes for ingame buttons

class LaunchButton:
	def __init__(self, x, y):
		self.image = launchWaveButton
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
	def draw(self, screen):
		screen.blit(self.image, (self.rect.x, self.rect.y))
		
class PauseButton:
	def __init__(self, x, y):
		self.image = pauseButton
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
	def draw(self, screen):
		screen.blit(self.image, (self.rect.x, self.rect.y))
	
class RadiusButton:
	def __init__(self, x, y):
		self.image = toggleRadiusButton
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
	def draw(self, screen):
		screen.blit(self.image, (self.rect.x, self.rect.y))
		
class ExitButton:
	def __init__(self, x, y):
		self.image = exitButton
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
	def draw(self, screen):
		screen.blit(self.image, (self.rect.x, self.rect.y))

# create buttons and define their placement here
launch_button = LaunchButton(675, 80)
pause_button = PauseButton(815, 80)
radius_button = RadiusButton(710, 540)
exit_button = ExitButton(710, 585)