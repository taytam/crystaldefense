# creates tower objects
import pygame
from towerradius import *
from graphics import *
from tower_stats import *

'''
Tower class
'''
# class to define a single Tower here.  Define type and stats here.
class Tower(pygame.sprite.Sprite):
	'''
	This class defines a Sprite object tower, and determines a tower's
	damage, cost, upgrade cost, value, radius, type, and name
	'''
	def __init__(self, myrect, type):
		'''
		Sets the Tower's damage, cost, upgradecost, value, radius, type,
		level, name, x-y position
		'''
		pygame.sprite.Sprite.__init__(self)
		self.x = myrect.x
		self.y = myrect.y
		self.damage = 0
		self.cost = 0
		self.upgradecost = 0
		self.value = 0
		self.rad = 0 # tower radius
		self.shooting = False
		self.level = 1
		self.towerRadius = ""
		self.type = ""
		self.name = ""
		self.shootSpeed = 60 #in FPS, this value can be set individually per tower
		self.shootTicks = 0
		if len(type) > 0:
			self.type = type
		#self.image = pygame.image.load("C:\\Python34\\CrystalDefense1.0\\redEnemy.png")
		#self.rect = self.image.get_rect()
		#self.rect.x = x
		#self.rect.y = y
		self.makeTower(myrect)
		#print("we added a tower!")

	def shootTimer(self):
			self.shootTicks += 1
			if self.shootSpeed <= self.shootTicks:
				self.shooting = False
				self.shootTicks = 0
			if self.towerRadius: # if we have a radius
				if not self.towerRadius.currTarget: # and if the radius does not have a target
					self.shooting = False
					#self.shootTicks = 0
				'''elif self.towerRadius.enemiesInRange:
					self.towerRadius.checkTarget()
					self.shooting = False
					self.shootTicks = 0'''
		
	def makeTower(self, myrect):
		# FIRE TOWERS
		if self.type == 'red1':
			self.image = redTower1
			self.rect = self.image.get_rect()
			self.name = red1name
			self.damage = red1damage
			self.rad = red1rad #in pixels
			self.cost = red1cost
			self.rect.x = self.x
			self.rect.y = self.y
		if self.type == 'red2':
			self.image = redTower2
			self.rect = self.image.get_rect()
			self.name = red2name
			self.rad = red2rad
			self.damage = red2damage
			self.cost = red2cost
			self.rect.x = self.x
			self.rect.y = self.y
		if self.type == 'red3':
			self.image = redTower2
			self.rect = self.image.get_rect()
			self.name = red3name
			self.rad = red3rad
			self.damage = red3damage
			self.cost = red3cost
			self.rect.x = self.x
			self.rect.y = self.y
			
		# ICE TOWERS
		if self.type == 'blue1':
			self.image = blueTower1
			self.rect = self.image.get_rect()
			self.name = blue1name
			self.damage = blue1damage
			self.rad = blue1rad
			self.cost = blue1cost
			self.rect.x = self.x
			self.rect.y = self.y
		if self.type == 'blue2':
			self.image = blueTower2
			self.rect = self.image.get_rect()
			self.name = blue2name
			self.damage = blue2damage
			self.rad = blue2rad
			self.cost = blue2cost
			self.rect.x = self.x
			self.rect.y = self.y
		if self.type == 'blue3':
			self.image = blueTower1
			self.rect = self.image.get_rect()
			self.name = blue3name
			self.damage = blue3damage
			self.rad = blue3rad
			self.cost = blue3cost
			self.rect.x = self.x
			self.rect.y = self.y
			
		# EARTH TOWERS
		if self.type == 'green1':
			self.image = greenTower1
			self.rect = self.image.get_rect()
			self.name = green1name
			self.damage = green1damage
			self.rad = green1rad
			self.cost = green1cost
			self.rect.x = self.x
			self.rect.y = self.y
		if self.type == 'green2':
			self.image = greenTower2
			self.rect = self.image.get_rect()
			self.name = green2name
			self.damage = green2damage
			self.rad = green2rad
			self.cost = green2cost
			self.rect.x = self.x
			self.rect.y = self.y
		if self.type == 'green3':
			self.image = greenTower2
			self.rect = self.image.get_rect()
			self.name = green3name
			self.damage = green3damage
			self.rad = green3rad
			self.cost = green3cost
			self.rect.x = self.x
			self.rect.y = self.y
		
		self.value = round(self.cost*.30)
		self.upgradecost = round(self.cost*.25)
		
		# now lets make the radius for the tower
		midpoint_x = self.rect.center[0]
		midpoint_y = self.rect.center[1]
		self.towerRadius = TowerRadius(self.rad, midpoint_x, midpoint_y, self.type)

	def levelUp(self):
		self.level += 1
		self.damage = round(self.damage*1.25)
		
	def upgrade(self):
		if self.level >= 10:
			return
		self.level += 1
		self.damage = round(self.damage*1.25)
		self.value += round(self.cost*((self.level+1)*.08))
		self.rad = round(self.rad*1.05)
		self.towerRadius.radius = self.rad
		
	def sell(self):
		return round(self.value)
		
	def upgradeCost(self):
		return round(self.upgradecost*self.level*.75)