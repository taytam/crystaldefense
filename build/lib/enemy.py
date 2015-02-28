import pygame
from graphics import *

'''
Enemy class
'''
class Enemy(pygame.sprite.Sprite):
	
	'''
	The Enemy class defines a Sprite object Enemy that defines an
	enemy's stats (such as health, movement speed, etc) and also
	chooses the image for the enemy based on a type
	'''
	def __init__(self, x, y, type):
	
		'''
		Initializes default stats for an enemy and also calls self.makeEnemy(x, y)
		'''
		pygame.sprite.Sprite.__init__(self)
		self.type = type
		self.health = 100 #default health
		self.baseHealth = 100
		self.xVel = 1 #starting x-speed
		self.yVel = 0 #starting y-speed
		self.dead = False #set to True when enemy dies
		self.end = False #reached the end of map
		self.turn = 1
		self.isFrozen = False #blue towers can slow enemies
		self.frozenTimer = 130 #120 game ticks
		#self.image.fill(255, 255, 255)
		self.makeEnemy(x, y)
		
	def hit(self, damage, damagetype):
		'''
		Applies damage to the enemy based on the type of the enemy and projectile 
		that hit it.
		'''
		# FIRE DAMAGE
		if damagetype == 'fire':
			if self.type == 'blue1' or self.type == 'blue2' or self.type == 'blue3':
				damage *= 2 # double damage for fire on ice
			if self.type == 'green1' or self.type == 'green2' or self.type == 'green3':
				damage *= 0.5 # half damage for fire on rock
		# EARTH	 DAMAGE
		if damagetype == 'earth':
			if self.type == 'red1' or self.type == 'red2' or self.type == 'red3':
				damage *= 2 # double damage for earth on fire
			if self.type == 'blue1' or self.type == 'blue2' or self.type == 'blue3':
				damage *= 0.5 # half damage for earth on ice		
		# ICE DAMAGE
		if damagetype == 'ice':
			if self.isFrozen == False:
				self.isFrozen = True
			if self.type == 'green1' or self.type == 'green2' or self.type == 'green3':
				damage *= 2 # double damage for ice on earth
			if self.type == 'red1' or self.type == 'red2' or self.type == 'red3':
				damage *= 0.5 # half damage for ice on fire	
				
		self.health -= round(damage) # apply damage of the hit after modifiers
		
		if self.health <= 0:
			self.dead = True
			
	def makeEnemy(self, x, y):
		'''
		Based on type, sets an enemy's stats, image, and Rect object
		'''
		# FIRE ENEMIES
		if self.type == 'red1':
			self.image = redEnemy1
			self.rect = self.image.get_rect()
			self.health = 200
			self.rect.x = x
			self.rect.y = y
		if self.type == 'red2':
			self.image = redEnemy2
			self.rect = self.image.get_rect()
			self.health = 500
			self.rect.x = x
			self.rect.y = y
		if self.type == 'red3':
			self.image = redEnemy3
			self.rect = self.image.get_rect()
			self.health = 1100
			self.rect.x = x
			self.rect.y = y
			
		# ICE ENEMIES
		if self.type == 'blue1':
			self.image = blueEnemy1
			self.rect = self.image.get_rect()
			self.health = 200
			self.rect.x = x
			self.rect.y = y
		if self.type == 'blue2':
			self.image = blueEnemy2
			self.rect = self.image.get_rect()
			self.health = 500
			self.rect.x = x
			self.rect.y = y
		if self.type == 'blue3':
			self.image = blueEnemy3
			self.rect = self.image.get_rect()
			self.health = 1100
			self.rect.x = x
			self.rect.y = y
			
		# EARTH ENEMIES
		if self.type == 'green1':
			self.image = greenEnemy1
			self.rect = self.image.get_rect()
			self.health = 200
			self.rect.x = x
			self.rect.y = y
		if self.type == 'green2':
			self.image = greenEnemy2
			self.rect = self.image.get_rect()
			self.health = 500
			self.rect.x = x
			self.rect.y = y
		if self.type == 'green3':
			self.image = greenEnemy3
			self.rect = self.image.get_rect()
			self.health = 1100
			self.rect.x = x
			self.rect.y = y
			
	def drawHealthBar(self, screen):
		'''
		Draw an enemy's healthbar to screen. Healthbar is a ratio of current health / total health
		'''
		xoffset = 13
		yoffset = 18
		pygame.draw.rect(screen, RED, (self.rect.center[0]-xoffset, self.rect.center[1]-yoffset, 30, 3), 0)
		greenRatio = self.health/self.baseHealth
		pygame.draw.rect(screen, GREEN, (self.rect.center[0]-xoffset, self.rect.center[1]-yoffset, 30*greenRatio, 3), 0)

	def frozen(self):
		'''
		Runs a countdown timer for the 'frozen' status of an enemy
		'''
		if self.isFrozen == True:
			self.frozenTimer -= 1
		if self.frozenTimer <= 0:
			self.frozenTimer = 130 # target reached 0 on timer, reset and unfreeze it
			self.isFrozen = False