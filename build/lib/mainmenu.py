import pygame
from graphics import *

class MainMenu:

	def __init__(self):
		self.running = True
		self.difficulty = 'Easy'
		self.difficultyNum = 0
		self.bigfont = pygame.font.Font(None, 60)
		self.populateMenu()
		
	def populateMenu(self):
		self.byline = self.bigfont.render("By: Taylor Tamblin", 0, WHITE)
		
		self.startGame = self.bigfont.render("Start Game", 0, WHITE)
		self.startGameRect = self.startGame.get_rect()
		self.startGameRect.x = 367
		self.startGameRect.y = 370
		
		self.difficultytext = self.bigfont.render("Difficulty: " + str(self.difficulty), 0, WHITE)
		self.difficultyRect = self.difficultytext.get_rect()
		self.difficultyRect.x = 328
		self.difficultyRect.y = 430
		
		self.instructions = self.bigfont.render("Instructions", 0, WHITE)
		self.instructionsRect = self.startGame.get_rect()
		self.instructionsRect.x = 352
		self.instructionsRect.y = 490
		
		self.quitGame = self.bigfont.render("Exit", 0, WHITE)
		self.quitGameRect = self.quitGame.get_rect()
		self.quitGameRect.x = 440
		self.quitGameRect.y = 550
		
	def draw(self, screen):
		screen.blit(titleLogo, (190, 130))
		screen.blit(self.byline, (295, 255))
		screen.blit(self.startGame, (self.startGameRect.x, self.startGameRect.y))
		screen.blit(self.difficultytext, (self.difficultyRect.x, self.difficultyRect.y))
		screen.blit(self.instructions, (self.instructionsRect.x, self.instructionsRect.y))
		screen.blit(self.quitGame, (self.quitGameRect.x, self.quitGameRect.y))

	def changeDifficulty(self):
		if self.difficultyNum == 2:
			self.difficultyNum = 0
		else:
			self.difficultyNum += 1
			
		if self.difficultyNum == 1:
			self.difficulty = 'Medium'
		elif self.difficultyNum == 2:
			self.difficulty = 'Hard'
		elif self.difficultyNum == 0:
			self.difficulty = 'Easy'
			
		self.difficultytext = self.bigfont.render("Difficulty: " + str(self.difficulty), 0, WHITE)
		self.difficultyRect = self.difficultytext.get_rect()
		self.difficultyRect.x = 328
		self.difficultyRect.y = 430
	
	def runInstructions(self, screen):
		running = True
		prevEnabled = False
		nextEnabled = True
		currpage = 0
		myfont = pygame.font.Font(None, 14)
		howtoplay = self.bigfont.render("How To Play", 0, WHITE)
		
		self.back = self.bigfont.render("Back to Main Menu", 0, WHITE)
		self.backRect = self.back.get_rect()
		self.backRect.x = 285
		self.backRect.y = 550
		
		self.nextText = self.bigfont.render("Next ->", 0, WHITE)
		self.nextTextRed = self.bigfont.render("Next ->", 0, RED)
		self.nextRect = self.nextText.get_rect()
		self.nextRect.x = 730
		self.nextRect.y = 20
		
		self.prevText = self.bigfont.render("<- Prev", 0, WHITE)
		self.prevTextRed = self.bigfont.render("<- Prev", 0, RED)
		self.prevRect = self.prevText.get_rect()
		self.prevRect.x = 50
		self.prevRect.y = 20
		
		myrad = 8
		xoffset = 30
		yoffset = 18
		
		while running:
			screen.fill(bgcolor)
			event = pygame.event.poll()
			if event.type == pygame.QUIT:
				running = 0
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				if self.backRect.collidepoint(x, y):
					running = False
				if nextEnabled:	
					if self.nextRect.collidepoint(x, y):
						currpage += 1
				if prevEnabled:	
					if self.prevRect.collidepoint(x, y):
						currpage -= 1
					
			if running == True:
				screen.blit(howtoplay, (340, 20))
				
				if currpage == 0:
					prevEnabled = False
					nextEnabled = True
					screen.blit(self.nextText, (self.nextRect.x, self.nextRect.y))
					screen.blit(instructions1, (70, 70))
					
				if currpage == 1:
					prevEnabled = True
					nextEnabled = True
					screen.blit(self.prevText, (self.prevRect.x, self.prevRect.y))
					screen.blit(self.nextText, (self.nextRect.x, self.nextRect.y))
					screen.blit(instructions2, (70, 70))
					
				if currpage == 2:
					prevEnabled = True
					nextEnabled = True
					screen.blit(self.prevText, (self.prevRect.x, self.prevRect.y))
					screen.blit(self.nextText, (self.nextRect.x, self.nextRect.y))
					screen.blit(instructions3, (70, 70))
					
				if currpage == 3:
					prevEnabled = True
					nextEnabled = False
					screen.blit(self.prevText, (self.prevRect.x, self.prevRect.y))
					screen.blit(instructions4, (70, 70))
					
				screen.blit(self.back, (self.backRect.x, self.backRect.y))
				
				if self.backRect.collidepoint(pygame.mouse.get_pos()):
					pygame.draw.circle(screen, WHITE, (self.backRect.x - xoffset, self.backRect.y + yoffset), myrad, 0)
				
				if nextEnabled:
					if self.nextRect.collidepoint(pygame.mouse.get_pos()):
						screen.blit(self.nextTextRed, (self.nextRect.x, self.nextRect.y))
				
				if prevEnabled:
					if self.prevRect.collidepoint(pygame.mouse.get_pos()):
						screen.blit(self.prevTextRed, (self.prevRect.x, self.prevRect.y))
					
				pygame.display.flip()