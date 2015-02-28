import pygame
import os

'''
The graphics module for Crystal Defense
'''

# get the directory (all graphics are under the /Graphics directory)
dirname = os.path.join(os.path.dirname(__file__), '..', 'Graphics')

#############################################
#  DEFINED COLORS
#############################################
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
GOLD = 255,150,80

bgcolor = BLACK

#############################################
# GAME GRAPHICS
#############################################

# Menu and Icons
titleLogo = pygame.image.load(dirname + '/titleLogo.png')
moneySign = pygame.image.load(dirname + '/money.png')
lifeIcon = pygame.image.load(dirname + '/life.png')
towermenu = pygame.image.load(dirname + '/towerMenu.png')
sellButton = pygame.image.load(dirname + '/buttonSell.png')
upgradeButton = pygame.image.load(dirname + '/buttonUpgrade.png')
pauseButton = pygame.image.load(dirname + '/buttonPause1.png')
#soundButton = pygame.image.load(dirname + '/buttonSound.png')
launchWaveButton = pygame.image.load(dirname + '/buttonSendWave.png')
toggleRadiusButton = pygame.image.load(dirname + '/buttonTowerRadius1.png')
exitButton = pygame.image.load(dirname + '/buttonExit.png')
instructions1 = pygame.image.load(dirname + '/instructions1.png')
instructions2 = pygame.image.load(dirname + '/instructions2.png')
instructions3 = pygame.image.load(dirname + '/instructions3.png')
instructions4 = pygame.image.load(dirname + '/instructions4.png')

# Map Tiles
grassTile = pygame.image.load(dirname + '/grassTile.png')
roadTile = pygame.image.load(dirname + '/roadTile.png')

# Tower Tiles
redTower1 = pygame.image.load(dirname + '/redTower1.png')
blueTower1 = pygame.image.load(dirname + '/blueTower1.png')
greenTower1 = pygame.image.load(dirname + '/greenTower1.png')
redTower2 = pygame.image.load(dirname + '/redTower2.png')
blueTower2 = pygame.image.load(dirname + '/blueTower2.png')
greenTower2 = pygame.image.load(dirname + '/greenTower2.png')
redTower3 = pygame.image.load(dirname + '/redTower3.png')
blueTower3 = pygame.image.load(dirname + '/blueTower3.png')
greenTower3 = pygame.image.load(dirname + '/greenTower3.png')

# Enemy Graphics
redEnemy1 = pygame.image.load(dirname + '/redEnemy1.png')
blueEnemy1 = pygame.image.load(dirname + '/blueEnemy1.png')
greenEnemy1 = pygame.image.load(dirname + '/greenEnemy1.png')
redEnemy2 = pygame.image.load(dirname + '/redEnemy2.png')
blueEnemy2 = pygame.image.load(dirname + '/blueEnemy2.png')
greenEnemy2 = pygame.image.load(dirname + '/greenEnemy2.png')
redEnemy3 = pygame.image.load(dirname + '/redEnemy3.png')
blueEnemy3 = pygame.image.load(dirname + '/blueEnemy3.png')
greenEnemy3 = pygame.image.load(dirname + '/greenEnemy3.png')


# Projectile Graphics
redProj1 = pygame.image.load(dirname + '/redProjectile1.png')
blueProj1 = pygame.image.load(dirname + '/blueProjectile1.png')
greenProj1 = pygame.image.load(dirname + '/greenProjectile1.png')
redProj2 = pygame.image.load(dirname + '/redProjectile1.png')
blueProj2 = pygame.image.load(dirname + '/blueProjectile1.png')
greenProj2 = pygame.image.load(dirname + '/greenProjectile1.png')
redProj3 = pygame.image.load(dirname + '/redProjectile1.png')
blueProj3 = pygame.image.load(dirname + '/blueProjectile1.png')
greenProj3 = pygame.image.load(dirname + '/greenProjectile1.png')