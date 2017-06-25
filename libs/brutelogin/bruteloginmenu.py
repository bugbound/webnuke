import curses
from selenium.common.exceptions import WebDriverException

from libs.brutelogin.brutelogincommands import *

class BruteLoginScreen:
	def __init__(self, screen, webdriver, curses_util):
		self.version=0.1
		self.screen = screen
		self.driver = webdriver
		self.curses_util = curses_util
		self.commands = BruteLoginCommands(self.driver)
		
		
	def show(self):
		showscreen = True
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "Brute Force Login")
			self.screen.addstr(4, 5, "1) Start brute forcing")


			
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
				
			if c == ord('1'):
				self.curses_util.close_screen()
				self.commands.start_brute_force()
								
		return
		
