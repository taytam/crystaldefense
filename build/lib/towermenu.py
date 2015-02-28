import pygame
from tower import *
from graphics import *
from tower_stats import *

# class for the tower selection menu (buying and placing towers)

class TowerButton(pygame.sprite.Sprite):
	def __init__(self, x, y, type):
		pygame.sprite.Sprite.__init__(self)
		self.towerType = type
		self.name = ''
		self.tileNum = 0
		self.damage = 0
		self.rad = 0
		self.cost = 0
		self.chooseTower()
		#self.image = redTower1 #replace with redTower1Button
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
	def chooseTower(self):
		if self.towerType == "red1":
			self.image = redTower1
			self.tileNum = 2
			self.name = red1name
			self.damage = red1damage
			self.rad = red1rad
			self.cost = red1cost
		if self.towerType == "red2":
			self.image = redTower2
			self.tileNum = 5
			self.name = red2name
			self.damage = red2damage
			self.rad = red2rad
			self.cost = red2cost
		if self.towerType == "red3":
			self.image = redTower3
			self.tileNum = 8
			self.name = red3name
			self.damage = red3damage
			self.rad = red3rad
			self.cost = red3cost
		if self.towerType == "blue1":
			self.image = blueTower1
			self.tileNum = 3
			self.name = blue1name
			self.damage = blue1damage
			self.rad = blue1rad
			self.cost = blue1cost
		if self.towerType == "blue2":
			self.image = blueTower2
			self.tileNum = 6
			self.name = blue2name
			self.damage = blue2damage
			self.rad = blue2rad
			self.cost = blue2cost
		if self.towerType == "blue3":
			self.image = blueTower3
			self.tileNum = 9
			self.name = blue3name
			self.damage = blue3damage
			self.rad = blue3rad
			self.cost = blue3cost
		if self.towerType == "green1":
			self.image = greenTower1
			self.tileNum = 4
			self.name = green1name
			self.damage = green1damage
			self.rad = green1rad
			self.cost = green1cost
		if self.towerType == "green2":
			self.image = greenTower2
			self.tileNum = 7
			self.name = green2name
			self.damage = green2damage
			self.rad = green2rad
			self.cost = green2cost
		if self.towerType == "green3":
			self.image = greenTower3
			self.tileNum = 10
			self.name = green3name
			self.damage = green3damage
			self.rad = green3rad
			self.cost = green3cost

		
class MenuButton:
	
	def __init__(self, x, y, name, image):
		self.image = image
		self.name = name
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
class TowerMenu:
	
	def __init__(self, startX, startY):
		self.show = True
		self.x = startX
		self.y = startY
		self.placingTower = False #track if we have a tower selected for placement
		self.towerType = ""
		self.selectedTower = ""
		self.buttons = []
		self.viewingButtons = []
		self.populateButtons()
		self.font = pygame.font.Font(None, 20)
		self.bigfont = pygame.font.Font(None, 30)
		#self.showTowerSelection()
	
	#draw the menu, depending on if we're placing a tower or looking at a tower's stats
	def drawMenu(self, screen, player):
		screen.blit(towermenu, (self.x, self.y))
		pygame.draw.rect(screen, (0,0,0), (self.x + 15, self.y + 220, 220, 160), 2)
		menuTitle = self.bigfont.render("Towers", 0, WHITE)
		for button in self.buttons:
			screen.blit(button.image, (button.rect.x, button.rect.y))
			if player.money < button.cost:
				fadedRect = pygame.Surface((40, 40))
				fadedRect.set_alpha(140)
				fadedRect.fill((50,50,50))
				screen.blit(fadedRect, (button.rect.x, button.rect.y))
			if self.placingTower == False: #if we are not placing tower
				menuTitle = self.bigfont.render("Select Towers", 0, WHITE)
				if self.selectedTower == "": #and if a tower is not selected
					pygame.draw.rect(screen, (0,0,0), (button.rect.x, button.rect.y, 40, 40), 2)
				else: #if we aren't placing tower AND tower is selected
					#print("placingtower=True, tower is selected")
					pygame.draw.rect(screen, (0,0,0), (button.rect.x, button.rect.y, 40,40), 2)
					#pygame.draw.rect(screen, (255,150,80), (button.rect.x, button.rect.y, 40, 40), 2)
					towerName = self.font.render(str(self.selectedTower.name), 0, WHITE)
					towerDamage = self.font.render("Damage: " + str(self.selectedTower.damage), 0, WHITE)
					towerRadius = self.font.render("Radius: " + str(self.selectedTower.rad), 0, WHITE)
					towerLevel = self.font.render("Level: " + str(self.selectedTower.level), 0, WHITE)
					upgradeCost = self.font.render("Upgrade: $" + str(self.selectedTower.upgradeCost()), 0, WHITE)
					sellValue = self.font.render("Sell Value: $" + str(self.selectedTower.value), 0, WHITE)
					menuTitle = self.font.render("Viewing your tower", 0, WHITE)
					
					# Draw Tower Stats
					screen.blit(towerName, (self.x + 20, self.y + 230))
					screen.blit(towerDamage, (self.x + 20, self.y + 255))
					screen.blit(towerRadius, (self.x + 20, self.y + 280))
					screen.blit(towerLevel, (self.x + 20, self.y + 305))
					screen.blit(upgradeCost, (self.x + 20, self.y + 330))
					screen.blit(sellValue, (self.x + 127, self.y + 330))
					
					# Draw Upgrade and Sell buttons
					#screen.blit(upgradeButton, (self.x + 40, self.y + 350))
					#screen.blit(sellButton, (self.x + 140, self.y + 350))
					for button in self.viewingButtons:
						screen.blit(button.image, (button.rect.x, button.rect.y))
					pygame.draw.rect(screen, GOLD, (self.selectedTower.rect.x, self.selectedTower.rect.y,40,40),2)
			elif self.placingTower and button.towerType == self.towerType:
				menuTitle = self.font.render("Place your tower on the map", 0, WHITE)
				pygame.draw.rect(screen, GOLD, (button.rect.x, button.rect.y, 40, 40), 2)
				towerName = self.font.render(str(button.name), 0, WHITE)
				towerDamage = self.font.render("Damage: " + str(button.damage), 0, WHITE)
				towerRadius = self.font.render("Radius: " + str(button.rad), 0, WHITE)
				towerCost = self.font.render("Cost: $" + str(button.cost), 0, WHITE)
				screen.blit(towerName, (self.x + 20, self.y + 230))
				screen.blit(towerDamage, (self.x + 20, self.y + 255))
				screen.blit(towerRadius, (self.x + 20, self.y + 280))
				screen.blit(towerCost, (self.x + 20, self.y + 305))
			else:
				pygame.draw.rect(screen, (0,0,0), (button.rect.x, button.rect.y, 40, 40), 2)
		screen.blit(menuTitle, (self.x + 30, self.y + 20))
	
	def populateButtons(self):
		self.viewingButtons.append(MenuButton(self.x + 40, self.y + 350, 'upgrade', upgradeButton))
		self.viewingButtons.append(MenuButton(self.x + 140, self.y + 350, 'sell', sellButton))
		
		self.buttons.append(TowerButton(self.x + 30, self.y + 50, "red1"))
		self.buttons.append(TowerButton(self.x + 100, self.y + 50, "blue1"))
		self.buttons.append(TowerButton(self.x + 170, self.y + 50, "green1"))
		self.buttons.append(TowerButton(self.x + 30, self.y + 110, "red2"))
		self.buttons.append(TowerButton(self.x + 100, self.y + 110, "blue2"))
		self.buttons.append(TowerButton(self.x + 170, self.y + 110, "green2"))
		self.buttons.append(TowerButton(self.x + 30, self.y + 170, "red3"))
		self.buttons.append(TowerButton(self.x + 100, self.y + 170, "blue3"))
		self.buttons.append(TowerButton(self.x + 170, self.y + 170, "green3"))
	
	def getTileNum(self):
		tileNum = 0
		for button in self.buttons:
			if button.towerType == self.towerType:
				tileNum = button.tileNum
		return tileNum
	#draw buttons if we are not viewing a towers stats, COME BACK TO THIS LATER WHEN WE HAVE MORE BUTTONS*
	#def showTowerSelection(self):
	#	self.redtowerbutton = RedTower1Button(self.x + 30, self.y + 50)
	
	def canAfford(self, player):
		canAfford = False
		for button in self.buttons:
			if button.towerType == self.towerType:
				if player.money > button.cost:
					canAfford = True
					return canAfford
		return canAfford
		
	def createTower(self, rect, type):
		#if self.placingTower == True:
		mytower = Tower(rect, type)
		self.towertype = ""
		return mytower