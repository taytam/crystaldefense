import pygame
from math import *
from graphics import *
from copy import deepcopy

class Projectile(pygame.sprite.Sprite):
	def __init__(self, x, y, type, currTarget, enemiesInRange, damage):
		pygame.sprite.Sprite.__init__(self)
		self.type = type
		self.damage = damage #inherited damage from Tower
		self.xVel = 0 #starting x-speed
		self.yVel = 0 #starting y-speed
		self.shootSpeed = 5 #we can set this individually for each projectile as well
		self.currTarget = currTarget
		self.enemiesInRange = deepcopy(enemiesInRange)
		self.hitTarget = False #track if this projectile has come in contact with an enemy
		#self.image.fill(255, 255, 255)
		self.makeProjectile(x, y)
		
	def updatePos(self, x, y):
		deltax = x - self.rect.center[0]
		deltay = y - self.rect.center[1]
		
		distance = sqrt(((deltax)**2) + ((deltay)**2)) # distance to enemy
		
		# Idea here: we have to increment rect.x and y by deltax and deltay, but want a constant velocity
		# Solution: use distance to enemy in the divisor so that as projectile gets closer to enemy,
		# distance goes down but deltax increases (inverse proportionality)
		deltax = (deltax/(distance/self.shootSpeed))
		deltay = (deltay/(distance/self.shootSpeed))
		
		#print(deltax, deltay)
		
		self.rect.x += deltax
		self.rect.y += deltay
			
	def makeProjectile(self, x, y):
		# FIRE PROJECTILES
		if self.type == 'red1':
			self.image = redProj1
			self.rect = self.image.get_rect()
			self.type = 'fire'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery
		if self.type == 'red2':
			self.image = redProj2
			self.rect = self.image.get_rect()
			self.type = 'fire'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery
		if self.type == 'red3':
			self.image = redProj3
			self.rect = self.image.get_rect()
			self.type = 'fire'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery
			
		# ICE PROJECTILES
		if self.type == 'blue1':
			self.image = blueProj1
			self.rect = self.image.get_rect()
			#self.damage = 100
			self.type = 'ice'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery
		if self.type == 'blue2':
			self.image = blueProj2
			self.rect = self.image.get_rect()
			#self.damage = 100
			self.type = 'ice'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery
		if self.type == 'blue3':
			self.image = blueProj3
			self.rect = self.image.get_rect()
			#self.damage = 100
			self.type = 'ice'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery
			
		# EARTH PROJECTILES
		if self.type == 'green1':
			self.image = greenProj1
			self.rect = self.image.get_rect()
			#self.damage = 100
			self.type = 'earth'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery
		if self.type == 'green2':
			self.image = greenProj2
			self.rect = self.image.get_rect()
			#self.damage = 100
			self.type = 'earth'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery
		if self.type == 'green3':
			self.image = greenProj3
			self.rect = self.image.get_rect()
			#self.damage = 100
			self.type = 'earth'
			centerx = self.rect.center[0]
			centery = self.rect.center[1]
			self.rect.x = x - centerx
			self.rect.y = y - centery