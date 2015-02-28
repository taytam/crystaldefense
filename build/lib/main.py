#! /usr/bin/env python

# Crystal Defense - Tower Defense Game
# Coding, graphics, game testing, and design by: Taylor Tamblin

# Version 1.0

# 12/12/14
# Written in Python using Pygame
# Graphics created in GIMP 2

'''
The 'main' module for Crystal Defense
'''

import pygame
from mainmenu import *
from easymap import *
from mediummap import *
from hardmap import *
from graphics import *
from tower import *
from towerradius import *
from towermenu import *
from projectile import *
from enemy import *
from player import *
from wave import *
from buttons import *
import imp
from copy import *

#############################################
#  SCREEN SETTINGS
#############################################
screenWidth = 960
screenHeight = 640
screen = pygame.display.set_mode((screenWidth, screenHeight))

#############################################
#  GAME INITIALIZERS
#############################################

pygame.init()
pygame.display.set_caption('Crystal Defense - Tower Defense Game')

clock = pygame.time.Clock() # create the game clock (after pygame init)
FPS = 50 # defines game frame speed
running = True
pause = False

player = Player() # create the player

###########################
# DEFINED FONTS
###########################
font = pygame.font.Font(None, 40)
font_enemyHealth = pygame.font.Font(None, 15)

screen.fill(bgcolor) # fill default background color
towermenu = TowerMenu(690, 130)

mainmenu = MainMenu()

##############################
# INITIALIZE GAME AT WAVE 1
##############################

enemies = pygame.sprite.Group() # create group for enemies of a wave
towers = pygame.sprite.Group() # create group for towers
projectiles = pygame.sprite.Group() # create group for tower projectiles
tiles = pygame.sprite.Group()
tower_radii = pygame.sprite.Group()

map = EasyMap() # create an easy level map
map.drawMap(screen) # draw the map

mapTiles = deepcopy(map.grassTiles) # copy of grass tiles (can place tower on)
for tile in mapTiles:
	tiles.add(tile)

wave_ticks = 0 #ticks since wave began
myWave = Wave(player.current_wave) #make new wave 0
MAX_WAVE = 20 # set max waves here
player.max_wave = MAX_WAVE

radiusOn = True #shows all tower's radius during the game
wave_launched = False # will keep track of if the wave has been sent by the player yet
endofwave = False

#############################################
#  MAIN GAME LOOP
#############################################
while running:
	if mainmenu.running == True:
		screen.fill(bgcolor)
		mainmenu.draw(screen)
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = 0
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos
			# Start Game "button"
			if mainmenu.startGameRect.collidepoint(x, y):
				mainmenu.running = False
				
				#create the map based on difficulty chosen
				if mainmenu.difficulty == 'Easy':
					map = EasyMap()
				if mainmenu.difficulty == 'Medium':
					map = MediumMap()
				if mainmenu.difficulty == 'Hard':
					map = HardMap()
					
				map.drawMap(screen) # draw the map

				mapTiles = deepcopy(map.grassTiles) # copy of grass tiles (can place tower on)
				for tile in mapTiles:
					tiles.add(tile)
				
			if mainmenu.difficultyRect.collidepoint(x, y):
				mainmenu.changeDifficulty()
			# Instructions "button"
			if mainmenu.instructionsRect.collidepoint(x, y):
				screen.fill(bgcolor)
				mainmenu.runInstructions(screen)
			# Exit "button"
			if mainmenu.quitGameRect.collidepoint(x, y):
				running = 0
				
		myrad = 8
		xoffset = 30
		yoffset = 18
		if mainmenu.startGameRect.collidepoint(pygame.mouse.get_pos()):
			pygame.draw.circle(screen, WHITE, (mainmenu.startGameRect.x - xoffset, mainmenu.startGameRect.y + yoffset), myrad, 0)
		if mainmenu.difficultyRect.collidepoint(pygame.mouse.get_pos()):
			pygame.draw.circle(screen, WHITE, (mainmenu.difficultyRect.x - xoffset, mainmenu.difficultyRect.y + yoffset), myrad, 0)
		if mainmenu.instructionsRect.collidepoint(pygame.mouse.get_pos()):
			pygame.draw.circle(screen, WHITE, (mainmenu.instructionsRect.x - xoffset, mainmenu.instructionsRect.y + yoffset), myrad, 0)
		if mainmenu.quitGameRect.collidepoint(pygame.mouse.get_pos()):
			pygame.draw.circle(screen, WHITE, (mainmenu.quitGameRect.x - xoffset, mainmenu.quitGameRect.y + yoffset), myrad, 0)
			
		pygame.display.flip()
	

	###############################################
	# GAME HAS STARTED, LET'S GET CRACKING
	###############################################
	if not pause and not mainmenu.running:
		wave_ticks += 1 #controls speed of enemy creation
		clock.tick(FPS) #update the clock by FPS
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = 0
		
		##############################################
		# EVENTS FOR LEFT MOUSE CLICK
		##############################################
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos # Set the x, y positions of the mouse click
			
			if launch_button.rect.collidepoint(x, y):
				wave_launched = True
			
			if pause_button.rect.collidepoint(x, y):
				pause = True
				# now let's draw a faded square across the entire gamescreen
				fadedRect = pygame.Surface((screenWidth, screenHeight))
				fadedRect.set_alpha(70)
				fadedRect.fill((255,255,255))
				screen.blit(fadedRect, (0,0))
				
			if radius_button.rect.collidepoint(x, y):
				if radiusOn == True:
					radiusOn = False
				else:
					radiusOn = True
					
			######################################################
			# EXIT GAME BUTTON
			######################################################
			# resets the game state and then runs main menu
			######################################################
			if exit_button.rect.collidepoint(x, y):
				enemies.empty()
				towers.empty()
				projectiles.empty()
				tower_radii.empty()
				
				newMap = EasyMap()
				map = newMap
				mapTiles = []
				mapTiles = map.grassTiles
				for tile in mapTiles:
					tiles.add(tile)
					
				newtowermenu = TowerMenu(690, 130)
				towermenu = newtowermenu
				#newplayer = Player()
				#player = deepcopy(newplayer)
				player.reset()
					
				wave_ticks = 0
				newWave = Wave(player.current_wave)
				myWave = deepcopy(newWave)
				
				radiusOn = True
				wave_launched = False
				endofwave = False
				
				screen.fill(bgcolor)
				mainmenu.running = True
				
			for tile in tiles:
				#if tile clicked was a tower supporting tile... do logic
				#if towermenu.placingTower == False:
				if tile.rect.collidepoint(x, y):
					#print(x, y)
					# if clicked tower that exists, display its stats
					if map.grid[tile.gridX][tile.gridY] >= 2:
						for tower in towers:
							if tower.rect.collidepoint(x, y):
								towermenu.selectedTower = tower
								towermenu.placingTower = False
						#print("we clicked on existing tower!")
						#update towermenu to display tower stats
				if towermenu.placingTower == True:
					if towermenu.selectedTower:
						towermenu.selectedTower = ""
					if tile.rect.collidepoint(x, y) and towermenu.canAfford(player):
						if map.swapTile(tile.gridX, tile.gridY, towermenu.getTileNum()) == True:
							centerX = tile.rect.center[0]
							centerY = tile.rect.center[1]
							towertype = towermenu.towerType
							#mytower = towermenu.createTower(tile.rect.center[0], tile.rect.center[1],towertype) #make center of tower
							mytower = towermenu.createTower(tile.rect, towertype)
							player.money -= mytower.cost
							myrad = TowerRadius(mytower.rad, centerX, centerY, towertype) # make radius at center of selected tile
							mytower.towerRadius = myrad
							mytower.towerRadius.checkTarget()
							#myrad.drawRadius(screen)
							tower_radii.add(myrad) # add this new radius to our group list
							towers.add(mytower) # add this to list of towers
							towermenu.placingTower = False # stop placing tower
							towermenu.towerType = "" #set selected tower back to nothing

			
			# CHECK IF WE'VE CLICKED ON A TOWER PLACEMENT BUTTON
			for button in towermenu.buttons:
				if button.rect.collidepoint(x, y):
					#print("clicked tower!")
					towermenu.towerType = button.towerType
					towermenu.placingTower = True
					#print(towermenu.placingTower)
					
			# CHECK IF WE'VE CLICKED ON A TOWER OBJECT ITSELF (THEN SET TOWERMENU TO TOWER DISPLAY MODE)
			if towermenu.placingTower == False and towermenu.selectedTower:
				for button in towermenu.viewingButtons:
					if button.rect.collidepoint(x, y):
						if button.name == 'upgrade':
							upgradecost = towermenu.selectedTower.upgradeCost()
							if player.money >= upgradecost:
								player.money -= upgradecost
								towermenu.selectedTower.upgrade()
						if button.name == 'sell':
							player.money += towermenu.selectedTower.sell()
							mytower = towermenu.selectedTower
							for tile in tiles:
								if tile.rect.collidepoint(mytower.rect.x, mytower.rect.y):
									#print("deleted tile!")
									map.swapTile(tile.gridX, tile.gridY, 0)
							towermenu.selectedTower = ""
							tower_radii.remove(mytower.towerRadius)
							towers.remove(mytower)
							
		#############################################################################
		# CREATE ENEMIES AT A STEADY PACE, ACCORDING TO THE CURRENT WAVE LIST
		##############################################################################
		if wave_launched:
			if wave_ticks % 60 == 0 and myWave.more:
				enemytype = myWave.getEnemy()
				newenemy = Enemy(map.startX, map.startY, enemytype) # make enemy at start pos
				modifier = 0
				for x in range (0, player.current_wave):
					modifier += (1 + ((player.current_wave-1)*.1)) # 15% increase in enemy health per wave
				newenemy.health = round(newenemy.health*modifier)
				newenemy.baseHealth = copy(newenemy.health)
				enemies.add(newenemy)
		
		###########################################################################
		# REDRAW background, map, stats, towers, radii, projectiles, and menu
		###########################################################################
		if not pause:
			screen.fill(bgcolor)
			
			player.drawStats(screen, font)
			launch_button.draw(screen)
			# blur out wave launched button if we are currently on a wave
			if wave_launched:
				fadedRect = pygame.Surface((139, 49))
				fadedRect.set_alpha(140)
				fadedRect.fill((50,50,50))
				screen.blit(fadedRect, (launch_button.rect.x, launch_button.rect.y))
				
			pause_button.draw(screen)
			radius_button.draw(screen)
			exit_button.draw(screen)
			
			map.drawMap(screen)
			towermenu.drawMenu(screen, player)
			# draw all of the tower radii
			if len(tower_radii) > 0:
				for radius in tower_radii:
					if radiusOn == True:
						radius.visible = True
						radius.drawRadius(screen)
					elif towermenu.selectedTower:
						if radius == towermenu.selectedTower.towerRadius:
							radius.visible = True
							radius.drawRadius(screen)
						else:
							radius.visible = False
							radius.drawRadius(screen)
					else:
						radius.visible = False
						radius.drawRadius(screen)	
		###########################################################
		# MANAGE TOWER RADII HERE (ENEMY TRACKING)
		###########################################################
		if len(tower_radii) > 0:
			for radius in tower_radii:
				for enemy in enemies:
					if enemy.rect.colliderect(radius):
						if len(radius.enemiesInRange) > 0:
							if radius.intersects(enemy.rect.center) and enemy not in radius.enemiesInRange:
								radius.enemiesInRange.append(enemy)
								#print("added enemy to range list")
								#print(len(radius.enemiesInRange))
						elif radius.intersects(enemy.rect.center):
							radius.enemiesInRange.append(enemy)
					else: #if enemy has left our radius... remove it from list
						if radius.enemiesInRange:
							if enemy in radius.enemiesInRange:
								#print("removed enemy from enemiesInRange")
								radius.enemiesInRange.remove(enemy)
								radius.checkTarget()
								#if radius.currTarget not in radius.enemiesInRange:
								#	radius.currTarget = ""
								#print(len(radius.enemiesInRange))

				if len(radius.enemiesInRange) > 0:
					radius.checkTarget()
				
				######################################################
				# CREATE PROJECTILES IF ENEMY IS IN RANGE OF A TOWER
				######################################################
				for tower in towers:
					if radius == tower.towerRadius:
						if(tower.towerRadius.currTarget):
							if tower.towerRadius.enemiesInRange: #if we have enemies in range of a tower
								#pygame.draw.rect(screen, GOLD, (tower.rect.x, tower.rect.y,40,40),2)
								if tower.shooting == False: #if we aren't shooting, lets shoot
									tower.shooting = True
									if tower.towerRadius.currTarget in enemies and tower.towerRadius.currTarget.dead == False: #if we have and alive currtarget, shoot
										#print("added projectile, aimed at:")
										#print(tower.towerRadius.currTarget)
										if tower.shootTicks == 0:
											#make a projectile at the center of the shooting tower
											projectile = Projectile(radius.x, radius.y, tower.type, tower.towerRadius.currTarget, tower.towerRadius.enemiesInRange, tower.damage)
											projectiles.add(projectile)
										else:
											#radius.checkTarget()
											tower.shootTimer()
								else: #if we're currently shooting, increment timer till next shot, also validate enemy list
									for enemy in tower.towerRadius.enemiesInRange: #for enemies currently in radius list
										if enemy in enemies: #if this enemy exists in our game
											if enemy.dead:
												tower.towerRadius.enemiesInRange.remove(enemy) #enemy is in list, but is dead. remove it.
										else: #if this enemy no longer exist, remove it from radius list
											tower.towerRadius.enemiesInRange.remove(enemy) #enemy is in list, but is dead. remove it.
											if tower.towerRadius.currTarget.dead:
												if not tower.towerRadius.checkTarget():
													tower.shooting = False
									#if tower.shooting == True:
									#	pygame.draw.rect(screen, GOLD, (tower.rect.x, tower.rect.y,40,40),2) #if gold border, means tower is currently shooting
									tower.shootTimer()
							#else:
							#	tower.towerRadius.checkTarget()
								#tower.shooting = False
					towerLevel = font_enemyHealth.render(str(tower.level), 0, WHITE)
					screen.blit(towerLevel, (tower.rect.x+2, tower.rect.y+1))
					
					# DEBUG STUFF
					#inrange = font_enemyHealth.render(str(len(tower.towerRadius.enemiesInRange)), 0, RED)
					#screen.blit(inrange, (tower.rect.x+30, tower.rect.y+2))
					#ticks = font_enemyHealth.render(str(tower.shootTicks), 0, GREEN)
					#screen.blit(ticks, (tower.rect.x+18, tower.rect.y+2))
		
		###############################################
		# IF WE HAVE PROJECTILES, DRAW THEM!
		###############################################
		if len(projectiles) > 0:
			for projectile in projectiles:
				if projectile.currTarget.dead and projectile.hitTarget == True:
					projectiles.remove(projectile)
				elif projectile.currTarget.dead and projectile.hitTarget == False:
					if enemies:
						enemylist = enemies.sprites()
						projectile.currTarget = enemylist[0]
						projectile.updatePos(projectile.currTarget.rect.center[0], projectile.currTarget.rect.center[1])

					else:
						projectiles.remove(projectile)
				else:
					projectile.updatePos(projectile.currTarget.rect.center[0], projectile.currTarget.rect.center[1])
			projectiles.draw(screen)
		
			for projectile in projectiles:
				if projectile.rect.colliderect(projectile.currTarget):
					projectile.currTarget.hit(projectile.damage, projectile.type)
					projectiles.remove(projectile)
		
		################################################
		# UPDATE ENEMY DRAWING
		################################################
		if not pause:
			if len(enemies) > 0: #if we have enemies in enemy list... keep making enemies
				for enemy in enemies:
					if enemy.isFrozen: #if it's frozen... speed is cut in half
						enemy.frozen() #decrement its frozen timer
						if wave_ticks % 2 == 0:
							enemy.rect.x += enemy.xVel
							enemy.rect.y += enemy.yVel
					else:
						enemy.rect.x += enemy.xVel
						enemy.rect.y += enemy.yVel
					map.directions(enemy)
					if enemy.dead == True:
						if enemy.end == True:
							player.life -= 5
						else:
							player.money += round(((player.current_wave)/2) * 20)
							player.score += (300 + ((player.current_wave*50)+1)//10)
						for tower in towers:
							if tower.towerRadius.currTarget:
								if tower.towerRadius.currTarget.dead:
									if tower.towerRadius.checkTarget():
										tower.shooting = False
									if enemy in tower.towerRadius.enemiesInRange:
										tower.towerRadius.enemiesInRange.remove(enemy)
							if len(tower.towerRadius.enemiesInRange) == 0:
								tower.shooting = False
								tower.shootTicks = 0
						enemies.remove(enemy)
					else:
						enemyHealth = font_enemyHealth.render(str(enemy.health), 0, WHITE)
						screen.blit(enemyHealth, (enemy.rect.center[0]-12, enemy.rect.center[1] - 29))
						enemy.drawHealthBar(screen)
				enemies.draw(screen)

		#################################################
		# START NEW WAVE + WAVE STATS RESET
		#################################################
		if myWave.more == False and len(enemies) == 0 and player.current_wave < player.max_wave and endofwave == False:
			endofwave = True
			wave_launched = False
			
		# Check the Win Condition here
		if myWave.more == False and len(enemies) == 0 and player.current_wave == player.max_wave and endofwave == False:
			player.won = True
		
		# Conditions for starting the next wave.  Kicks off wave reset logic
		if endofwave and wave_launched and myWave.more == False and len(enemies) == 0 and player.current_wave < player.max_wave:
			player.current_wave += 1
			endofwave = False	
			
			#RESET THE TOWERS' ENEMY TRACKING
			for tower in towers:
				tower.towerRadius.enemiesInRange = []
				tower.towerRadius.currTarget = ""
				tower.shootTicks = 0
				tower.shooting = False
			if projectiles:
				for projectile in projectiles:
					projectiles.remove(projectile)
			
			# INCREMENT PLAYER STATS WHEN NEW WAVE STARTS
			player.score += player.money*2
			player.money = round(player.money * 1.1) #give the player 10% interest on funds leftover after round
			
			# DISPLAY A MESSAGE INDICATING NEW WAVE IS STARTING
			wavetext = font.render('Wave: ' + str(player.current_wave), 0, WHITE)
			screen.blit(wavetext, (315, 300))
			pygame.display.flip()
			pygame.time.delay(2000)
			
			myWave = Wave(player.current_wave) #make new wave
			wave_ticks = 0
			
			screen.fill(bgcolor)	
			player.drawStats(screen, font)
			map.drawMap(screen)
			
			# DRAW ALL THE TOWER RADII
			if len(tower_radii) > 0:
				for radius in tower_radii:
					if radiusOn == True:
						radius.visible = True
						radius.drawRadius(screen)
					elif towermenu.selectedTower is not "":
						if radius == towermenu.selectedTower.towerRadius:
							radius.visible = True
							radius.drawRadius(screen)
						else:
							radius.visible = False
							radius.drawRadius(screen)
					else:
						radius.visible = False
						radius.drawRadius(screen)
				for tower in towers:
					towerLevel = font_enemyHealth.render(str(tower.level), 0, WHITE)
					screen.blit(towerLevel, (tower.rect.x+2, tower.rect.y+2))
					
			towermenu.drawMenu(screen, player)
			
			launch_button.draw(screen)
			fadedRect = pygame.Surface((139, 49))
			fadedRect.set_alpha(140)
			fadedRect.fill((50,50,50))
			screen.blit(fadedRect, (launch_button.rect.x, launch_button.rect.y))
			
			pause_button.draw(screen)
			radius_button.draw(screen)
			exit_button.draw(screen)
			
			gotext = font.render('Go!', 0, WHITE)
			screen.blit(gotext, (335, 300))
			pygame.display.flip()
			pygame.time.delay(1000)
			
		##################################################	
		# CHECK IF PLAYER IS DEAD
		##################################################
		if player.life <= 0:
			player.alive = False
	
	######################################
	# PAUSE CONDITIONS
	######################################	
	if pause:
		pauseText = font.render('Paused', 0, WHITE)
		screen.blit(pauseText, (310, 300))
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			running = 0
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos
			if pause_button.rect.collidepoint(x, y):
				pause = False
	
	#######################################
	# PLAYER WON
	#######################################
	if player.won == True:
		winnerText = font.render('You Rock!', 0, WHITE)
		goback = font.render('Main Menu', 0, WHITE)
		gobackRed = font.render('Main Menu', 0, RED)
		gobackRect = goback.get_rect()
		gobackRect.x = 300
		gobackRect.y = 390
		
		while player.won:
			event = pygame.event.poll()
			screen.blit(goback, (gobackRect.x, gobackRect.y))
			
			if event.type == pygame.QUIT:
				running = 0
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				# RESET GAME AND GO TO MAIN MENU IF GO BACK IS CLICKED
				if gobackRect.collidepoint(x, y):
					enemies.empty()
					towers.empty()
					projectiles.empty()
					tower_radii.empty()
					
					newMap = EasyMap()
					map = newMap
					mapTiles = []
					mapTiles = map.grassTiles
					for tile in mapTiles:
						tiles.add(tile)
						
					newtowermenu = TowerMenu(690, 130)
					towermenu = newtowermenu
					#newplayer = Player()
					#player = deepcopy(newplayer)
					player.reset()
						
					wave_ticks = 0
					newWave = Wave(player.current_wave)
					myWave = deepcopy(newWave)
					
					radiusOn = True
					wave_launched = False
					endofwave = False
					
					screen.fill(bgcolor)
					mainmenu.running = True
					
			if gobackRect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(gobackRed, (gobackRect.x, gobackRect.y))
			
			screen.blit(winnerText, (300, 300))
			
			pygame.display.flip()
			
	##############################################
	# PLAYER DIED
	##############################################
	if player.alive == False:
		gameOver = font.render('You Died! Try Again', 0, WHITE)
		goback = font.render('Main Menu', 0, WHITE)
		gobackRed = font.render('Main Menu', 0, RED)
		gobackRect = goback.get_rect()
		gobackRect.x = 300
		gobackRect.y = 390
		
		while mainmenu.running == False:

			screen.blit(goback, (gobackRect.x, gobackRect.y))
			
			event = pygame.event.poll()
			if event.type == pygame.QUIT:
				running = 0
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				# RESET GAME AND GO TO MAIN MENU IF GO BACK IS CLICKED
				if gobackRect.collidepoint(x, y):
					enemies.empty()
					towers.empty()
					projectiles.empty()
					tower_radii.empty()
					
					newMap = EasyMap()
					map = newMap
					mapTiles = []
					mapTiles = map.grassTiles
					for tile in mapTiles:
						tiles.add(tile)
						
					newtowermenu = TowerMenu(690, 130)
					towermenu = newtowermenu
					#newplayer = Player()
					#player = deepcopy(newplayer)
					player.reset()
						
					wave_ticks = 0
					newWave = Wave(player.current_wave)
					myWave = deepcopy(newWave)
					
					radiusOn = True
					wave_launched = False
					endofwave = False
					
					screen.fill(bgcolor)
					mainmenu.running = True
					
			if gobackRect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(gobackRed, (gobackRect.x, gobackRect.y))
				
			screen.blit(gameOver, (250, 300))
			
			pygame.display.flip()
	
	##################################################
	# MAIN CALL TO UPDATE THE GAME DRAWING
	##################################################	
	pygame.display.flip()