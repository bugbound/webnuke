import time
from libs.followme.followmecommands import *

followme_count = 0

class FollowmeScreen:
	def __init__(self, screen, webdriver, curses_util, debug, proxy_host, proxy_port, logger):
		self.version=0.1
		self.screen = screen
		self.driver = webdriver
		
		self.curses_util = curses_util
		self.debug = debug
		self.proxy_host = proxy_host
		self.proxy_port = proxy_port
		self.logger = logger
		self.commands = FollowmeCommands(self.driver, self.debug, self.proxy_host, self.proxy_port, self.logger)
		
		
	def run(self):
		showscreen = True		
		global followme_count
		
		while showscreen:
			paused = self.commands.get_paused()
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "Followme "+str(followme_count))
			self.screen.addstr(4,  4, "1) Start new follow me")
			if paused == False:
				self.screen.addstr(6,  4, "2) PAUSE follow me")
			if paused:
				self.screen.addstr(7,  4, "3) RESUME follow me")
			
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			if paused:
				self.screen.addstr(23, 28, " -  P A U S E D   -  ")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
			
			if c == ord('1'):
				self.commands.start_new_instance()
				followme_count+=1

			if c == ord('2'):
				self.commands.pause_all()

			if c == ord('3'):
				self.commands.resume_all()
												
		return
		
		
				
