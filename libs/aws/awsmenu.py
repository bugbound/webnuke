import curses
from selenium.common.exceptions import WebDriverException

from libs.aws.awscommands import *

class AWSScreen:
	def __init__(self, screen, webdriver, curses_util, logger):
		self.version=0.1
		self.screen = screen
		self.driver = webdriver
		self.curses_util = curses_util
		self.logger = logger
		self.commands = AWSCommands(self.driver, self.logger)
		
		
	def show(self):
		showscreen = True
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "AWS")
			self.screen.addstr(4, 5, "1) Find S3 Bucket Urls")


			
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
				
			if c == ord('1'):
				self.curses_util.close_screen()
				self.commands.show_bucket_report()
								
		return
		
