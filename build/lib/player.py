import pygame
from graphics import *

# class to define player stats
class Player:
	
	def __init__(self):
		self.score = 0
		self.life = 100
		self.money = 100
		self.alive = True
		self.won = False
		self.current_wave = 1
		self.max_wave = 1
	
	def reset(self):
		self.current_wave = 1
		self.score = 0
		self.life = 100
		self.money = 100
		self.alive = True
		self.won = False
		
	def drawStats(self, screen, font):
			screen.blit(moneySign, (160, 30, 40,40))
			playermoney = font.render(str(self.money), 0, WHITE)
			screen.blit(playermoney, (210, 35))
			playerlife = font.render(str(self.life), 0, WHITE)
			screen.blit(lifeIcon, (20, 32))
			screen.blit(playerlife, (70, 35))
			playerscore = font.render("Score: " + str(self.score), 0, WHITE)
			screen.blit(playerscore, (530, 35))
			currwavetext = font.render("Wave: " + str(self.current_wave) + "/" + str(self.max_wave), 0, WHITE)
			screen.blit(currwavetext, (340, 35))