import pygame
from graphics import *
from math import *
from tower import *

# This class controls the radius for a tower, which is the median between a Tower and an Enemy.
# The radius will detect an enemy, and use stats from the tower to send projectiles at the enemy.
class TowerRadius(pygame.sprite.Sprite):
	def __init__(self, radius, x, y, type):
		#super(self).__init__()
		pygame.sprite.Sprite.__init__(self)
		self.radius = radius
		self.type = type
		self.visible = True
		self.x = x
		self.y = y
		self.currTarget = "" #stores the current enemy we're firing at
		self.enemiesInRange = []
		
		
	def drawRadius(self, screen):
		radcolor = (255,255,255)
		if "red" in self.type:
			radcolor = (255,0,0)
		if "blue" in self.type:
			radcolor = (0,0,255)
		if "green" in self.type:
			radcolor = (0,255,0)
			
		if self.visible == True:
			self.rect = pygame.draw.circle(screen, radcolor, (self.x, self.y), self.radius, 1)
			self.rect.x = self.x - self.radius
			self.rect.y = self.y - self.radius
		else:
			#self.rect = pygame.draw.circle(screen, radcolor, (self.x, self.y), self.radius, 0)
			fadedRect = pygame.Surface((self.radius*2, self.radius*2))
			fadedRect.set_alpha(0)
			fadedRect.fill((255,255,255))
			screen.blit(fadedRect, (self.x-self.radius, self.y-self.radius))
			self.rect = fadedRect.get_rect()
			self.rect.x = self.x - self.radius
			self.rect.y = self.y - self.radius
		#self.mask 
		
	def intersects(self, pos):
		intersects = False
		#print(pos[0], pos[1])
		x = pos[0]
		y = pos[1]
		distance = sqrt(((x-self.x)**2) + ((y-self.y)**2))
		#print(distance, self.radius)
		# we need to adjust the distance since its going off of midpoint, not the edge of the enemy
		adjusted_distance = distance - 8
		if adjusted_distance <= self.radius:
			intersects = True
		return intersects
		
	def checkTarget(self):
		hasTarget = False
		if len(self.enemiesInRange) > 0:
			if self.currTarget is "":
				self.currTarget = self.enemiesInRange[0]
			else:
				self.currTarget = self.enemiesInRange[0]
			hasTarget = True
		return hasTarget