import pygame
import os
from graphics import *

# class to define the easy difficulty map
class Tile(pygame.sprite.Sprite):
	def __init__(self, gridX, gridY, x, y):
		pygame.sprite.Sprite.__init__(self)
		#self.tiles = []
		self.image = grassTile
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.tileNum = 0 #start as grass tile
		self.gridX = gridX
		self.gridY = gridY
		self.isEmpty = True
	
	def update(self, tileNum):
		self.tileNum = tileNum
		return tileNum
		
	def placeTower(self):
		self.isEmpty = False
		
class MediumMap:

	def __init__(self):
		self.square = 40 # 1 side of the square (square x square dimensions)
		self.margin = 1
		self.xLoc = 50 #x location to start drawing map at
		self.yLoc = 135 # y location to start drawing map at
		self.gridX = 10 # how many tiles to draw horizontally
		self.gridY = 15 # how many tiles to draw vertically
		self.grid = [] # map grid
		self.grassTiles = []
		self.startX = 50 # starting x for enemies
		self.startY = 184 # starting y for enemies
		self.grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					[1,1,1,1,1,0,0,0,1,1,1,1,1,1,0],
					[0,0,0,0,1,0,0,0,1,0,0,0,0,1,0],
					[0,0,0,0,1,0,0,0,1,0,0,0,0,1,0],
					[0,0,0,0,1,0,1,1,1,0,0,0,0,1,0],
					[0,0,0,0,1,0,1,0,0,0,0,0,0,1,0],
					[0,0,0,0,1,0,1,1,1,0,0,0,0,1,0],
					[0,0,0,0,1,0,0,0,1,0,0,0,0,1,1],
					[0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
					[0,0,0,0,1,1,1,1,1,0,0,0,0,0,0]]

	def drawMap(self, screen):
		i = 0
		x = self.xLoc
		y = self.yLoc
		currRow = 0
		currCol = 0
		for i in range(0, self.gridX):
			for j in range(0, self.gridY):
				#pygame.draw.rect(screen, (255,255,255), (x, y, gridWidth, gridHeight))
				if self.grid[i][j] == 0:
					screen.blit(grassTile, (x,y,self.square,self.square))
					tile = Tile(i, j, x, y)
					self.grassTiles.append(tile)
					#grassTile.rect = grassTile.get_rect()
					#self.grassTiles.append(tile.rect)
				if self.grid[i][j] == 1:
					screen.blit(roadTile, (x,y,self.square,self.square))
				# Level 1 Towers	
				if self.grid[i][j] == 2:
					screen.blit(redTower1, (x,y,self.square,self.square))
				if self.grid[i][j] == 3:
					screen.blit(blueTower1, (x,y,self.square,self.square))
				if self.grid[i][j] == 4:
					screen.blit(greenTower1, (x,y,self.square,self.square))
				# Level 2 Towers
				if self.grid[i][j] == 5:
					screen.blit(redTower2, (x,y,self.square,self.square))
				if self.grid[i][j] == 6:
					screen.blit(blueTower2, (x,y,self.square,self.square))
				if self.grid[i][j] == 7:
					screen.blit(greenTower2, (x,y,self.square,self.square))
				# Level 3 Towers
				if self.grid[i][j] == 8:
					screen.blit(redTower3, (x,y,self.square,self.square))
				if self.grid[i][j] == 9:
					screen.blit(blueTower3, (x,y,self.square,self.square))
				if self.grid[i][j] == 10:
					screen.blit(greenTower3, (x,y,self.square,self.square))
				x += self.square + self.margin
				#pygame.draw.rect(screen, (255,255,255),(gridWidth, gridHeight), (xLoc, yLoc))
				#pygame.draw.rect(screen, (255,255,255),(gridWidth, gridWidth, gridHeight, gridHeight))
			x = self.xLoc
			y += self.square + self.margin
	
	# Set the turning points for enemies to follow
	# if modifying map (self.grid), these will need to be modified as well
	def directions(self, sprite):
		enemy = sprite
		x = enemy.rect.center[0]
		y = enemy.rect.center[1]
		#Turn 1 
		if enemy.turn == 1 and x == 233:
			enemy.turn += 1
			enemy.xVel = 0
			enemy.yVel = 1
		#Turn 2
		if enemy.turn == 2 and y == 524:
			enemy.turn += 1
			enemy.xVel = 1
			enemy.yVel = 0
		#Turn 3
		if enemy.turn == 3 and x == 398:
			enemy.turn += 1
			enemy.xVel = 0
			enemy.yVel = -1
		#Turn 4
		if enemy.turn == 4 and y == 402:
			enemy.turn += 1
			enemy.xVel = -1
			enemy.yVel = 0
		#Turn 5
		if enemy.turn == 5 and x == 316:
			enemy.turn += 1
			enemy.xVel = 0
			enemy.yVel = -1
		#Turn 6
		if enemy.turn == 6 and y == 320:
			enemy.turn += 1
			enemy.xVel = 1
			enemy.yVel = 0
		#Turn 7
		if enemy.turn == 7 and x == 400:
			enemy.turn += 1
			enemy.xVel = 0
			enemy.yVel = -1
		#Turn 8
		if enemy.turn == 8 and y == 195:
			enemy.turn += 1
			enemy.xVel = 1
			enemy.yVel = 0
		#Turn 9
		if enemy.turn == 9 and x == 603:
			enemy.turn += 1
			enemy.xVel = 0
			enemy.yVel = 1
		#Turn 10
		if enemy.turn == 10 and y == 438:
			enemy.turn += 1
			enemy.xVel = 1
			enemy.yVel = 0
		if enemy.turn == 11 and x == 650:
			enemy.xVel = 0
			enemy.dead = True
			enemy.end = True
			
	def swapTile(self, i, j, newTileNum):
		swappedTile = False
		if newTileNum > 0:
			if newTileNum == self.grid[i][j]: #if this tile already exists
				return swappedTile
			if self.grid[i][j] >= 2: #if ANY tower is on this spot... don't swap it
				return swappedTile
			self.grid[i][j] = newTileNum
			swappedTile = True
		else: # we sold a tower, graphically remove it from tile
			self.grid[i][j] = 0
		#print("swapped tile!")
		return swappedTile