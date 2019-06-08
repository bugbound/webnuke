import curses
from selenium.common.exceptions import WebDriverException

from libs.javascript.javascriptscript import *
from libs.javascript.javascriptcommands import *
from libs.javascript.jswalker import *


class JavascriptScreen:
	def __init__(self, screen, webdriver, curses_util, jsinjector):
		self.version=0.1
		self.screen = screen
		self.driver = webdriver
		self.curses_util = curses_util
		self.jsinjector = jsinjector
		self.commands = JavascriptCommands(self.driver, self.jsinjector)
		self.jswalker = JSWalker(self.driver, self.jsinjector)
		
		
	def show(self):
		showscreen = True
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "Javascript Tools")
			self.screen.addstr(4, 5, "1) Find URLS within Javascript Global Properties")
			self.screen.addstr(5, 5, "2) Show Javascript functions of Document")
			self.screen.addstr(6, 5, "3) Run all js functions without args")
			self.screen.addstr(7, 5, "4) Show Cookies accessable by Javascript")
			self.screen.addstr(8, 5, "5) Walk Javascript Functions")


			
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
				
			if c == ord('1'):
				self.curses_util.close_screen()
				self.commands.search_for_urls()
				
			if c == ord('2'):
				self.curses_util.close_screen()
				self.commands.search_for_document_javascript_methods()

			if c == ord('3'):
				self.curses_util.close_screen()
				self.commands.run_lone_javascript_functions()

			if c == ord('4'):
				self.curses_util.close_screen()
				self.commands.show_cookies()

			if c == ord('5'):
				self.curses_util.close_screen()
				self.jswalker.start_walk_tree()
				#self.commands.walk_functions()
					
		return
		
