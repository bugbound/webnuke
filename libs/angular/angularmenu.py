import curses
from libs.angular.angularCommands import *

class AngularScreen:
	def __init__(self, screen, webdriver, curses_util, jsinjector):
		self.version=0.1
		self.screen = screen
		self.driver = webdriver
		self.curses_util = curses_util
		self.jsinjector = jsinjector
		self.commands = AngularCommands(self.driver, self.jsinjector)
		
		
		
	def show(self):
		showscreen = True
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "AngularJS Tools")
			
			self.screen.addstr(4, 4, "1) Show Main Application Name")
			self.screen.addstr(5, 4, "2) Show Routes")
			self.screen.addstr(6, 4, "3) Show Dependencies")
			self.screen.addstr(7, 4, "4) Show Main Classes")
			self.screen.addstr(8, 4, "5) Show All Classes")
			self.screen.addstr(9, 4, "6) Test classes relying on ngResource")
				
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
				
			if c == ord('1'):
				self.curses_util.close_screen()
				self.commands.show_app_name()
			
			if c == ord('2'):
				self.curses_util.close_screen()
				self.commands.show_routes()
			
			if c == ord('3'):
				self.curses_util.close_screen()
				self.commands.show_deps()
				
			if c == ord('4'):
				self.curses_util.close_screen()
				self.commands.show_main_classes()
				
			if c == ord('5'):
				self.curses_util.close_screen()
				self.commands.show_all_classes()
				
			if c == ord('6'):
				self.curses_util.close_screen()
				self.commands.show_ngResource_tests()
				
		return
		
	
		
	
