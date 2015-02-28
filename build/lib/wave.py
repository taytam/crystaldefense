import pygame

# class to control waves (enemies per wave and type of enemy)
class Wave:
	def __init__(self, wave):
		self.more = True # flag saying if we should keep making enemies
		self.wavenum = wave
		self.enemynum = 0
		self.waveEnemies = []
		self.pickWave()
		
	def pickWave(self):
		# WAVE 1
		if self.wavenum == 1:
			self.waveEnemies = ['red1', 'red1', 'red1', 'red1', 'red1',
								'red1', 'red1', 'red1', 'red1', 'red1']
		# WAVE 2
		if self.wavenum == 2:
			self.waveEnemies = ['blue1', 'blue1', 'blue1', 'blue1', 'blue1',
								'blue1', 'blue1', 'blue1', 'blue1', 'blue1']
		# WAVE 3
		if self.wavenum == 3:
			self.waveEnemies = ['green1', 'green1', 'green1', 'green1', 'green1',
								'green1', 'green1', 'green1', 'green1', 'green1']
		# WAVE 4
		if self.wavenum == 4:
			self.waveEnemies = ['red1', 'blue1', 'green1', 'red1', 'blue1',
								'green1', 'red1', 'blue1', 'green1', 'red1']
		# WAVE 5						
		if self.wavenum == 5:
			self.waveEnemies = ['red1', 'red1', 'blue1', 'blue1', 'green1',
								'green1', 'red1', 'blue1', 'green1', 'red1',
								'blue1', 'green1']
		# WAVE 6
		if self.wavenum == 6:
			self.waveEnemies = ['green1', 'blue1', 'red1', 'red1', 'blue1',
								'blue1', 'green1', 'blue1', 'red1', 'red1',
								'green1', 'blue1', 'red1', 'blue1', 'green1']
		# WAVE 7
		if self.wavenum == 7:
			self.waveEnemies = ['red1', 'blue1', 'green1', 'red1', 'green1',
								'red1', 'red1', 'blue1', 'red1', 'green1',
								'red2', 'red2', 'red2']
		# WAVE 8
		if self.wavenum == 8:
			self.waveEnemies = ['blue2', 'blue2', 'blue2', 'blue2', 'blue2',
								'blue2', 'blue2', 'blue2', 'blue2', 'blue2']
		# WAVE 9
		if self.wavenum == 9:
			self.waveEnemies = ['green2', 'green2', 'green2', 'green2', 'green2',
								'green2', 'green2', 'green2', 'green2', 'green2']
		# WAVE 10
		if self.wavenum == 10:
			self.waveEnemies = ['red2', 'red2', 'red2', 'red2', 'red2',
								'red2', 'red2', 'red2', 'red2', 'red2']
		# WAVE 11						
		if self.wavenum == 11:
			self.waveEnemies = ['red2', 'red2', 'blue2', 'blue2', 'green2',
								'green2', 'red2', 'red2', 'blue2', 'blue2',
								'green2', 'green2']
		# WAVE 12
		if self.wavenum == 12:
			self.waveEnemies = ['red2', 'blue2', 'green2', 'red2', 'blue2',
								'green2', 'red2', 'blue2', 'green2', 'red2',
								'blue2', 'green2', 'red2', 'blue2', 'green2']
		# WAVE 13
		if self.wavenum == 13:
			self.waveEnemies = ['red3', 'red3', 'red3', 'red3', 'red3',
								'red3', 'red3', 'red3', 'red3', 'red3']
		# WAVE 14
		if self.wavenum == 14:
			self.waveEnemies = ['blue3', 'blue3', 'blue3', 'blue3', 'blue3',
								'blue3', 'blue3', 'blue3', 'blue3', 'blue3']
		# WAVE 15
		if self.wavenum == 15:
			self.waveEnemies = ['green3', 'green3', 'green3', 'green3', 'green3',
								'green3', 'green3', 'green3', 'green3', 'green3']
		# WAVE 16
		if self.wavenum == 16:
			self.waveEnemies = ['red3', 'blue3', 'green3', 'red3', 'blue3',
								'green3', 'red3', 'blue3', 'green3', 'red3']
		# WAVE 17
		if self.wavenum == 17:
			self.waveEnemies = ['red3', 'blue3', 'green3', 'red3', 'blue3',
								'green3', 'red3', 'blue3', 'green3', 'red3',
								'red3', 'blue3', 'green3']
		# WAVE 18
		if self.wavenum == 18:
			self.waveEnemies = ['red3', 'blue3', 'green3', 'red3', 'blue3',
								'green3', 'red3', 'blue3', 'green3', 'red3',
								'red3', 'blue3', 'green3', 'red3', 'blue3',
								'green3', 'red3', 'blue3', 'green3']
		# WAVE 19
		if self.wavenum == 19:
			self.waveEnemies = ['red3', 'blue3', 'green3', 'red3', 'blue3',
								'green3', 'red3', 'blue3', 'green3', 'red3',
								'red3', 'blue3', 'green3', 'red3', 'blue3',
								'green3', 'red3', 'blue3', 'green3', 'red3',
								'blue3', 'green3']
		# WAVE 20
		if self.wavenum == 20:
			self.waveEnemies = ['red3', 'blue3', 'green3', 'red3', 'blue3',
								'green3', 'red3', 'blue3', 'green3', 'red3',
								'red3', 'blue3', 'green3', 'red3', 'blue3',
								'green3', 'red3', 'blue3', 'green3', 'red3',
								'blue3', 'green3', 'red3', 'blue3', 'green3',
								'red3', 'blue3', 'green3']

	def getEnemy(self):
		currEnemy = self.waveEnemies[self.enemynum]
		self.enemynum += 1
		if self.enemynum >= len(self.waveEnemies):
			self.more = False #we have exhausted the wave, stop producing enemies
		return currEnemy