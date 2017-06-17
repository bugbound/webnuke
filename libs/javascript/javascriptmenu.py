import curses
from selenium.common.exceptions import WebDriverException

from libs.javascript.javascriptscript import *
from libs.javascript.javascriptcommands import *

class JavascriptScreen:
	def __init__(self, screen, webdriver, curses_util, jsinjector):
		self.version=0.1
		self.screen = screen
		self.driver = webdriver
		self.curses_util = curses_util
		self.jsinjector = jsinjector
		self.commands = JavascriptCommands(self.driver, self.jsinjector)
		
		
	def show(self):
		showscreen = True
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "Javascript Tools")
			self.screen.addstr(4, 5, "4) Find URLS within Javascript Global Properties")
			self.screen.addstr(5, 5, "5) Show Javascript functions of Document")
			#self.screen.addstr(6, 5, "6) Run all js functions without args")


			
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
				
			if c == ord('4'):
				self.curses_util.close_screen()
				self.commands.search_for_urls()
				
			if c == ord('5'):
				self.curses_util.close_screen()
				self.commands.search_for_document_javascript_methods()
				
		return
		
