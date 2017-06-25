import curses
from selenium.common.exceptions import WebDriverException
from libs.htmltools.htmlcommands import *
from libs.htmltools.htmltoolsscript import *

class HTMLScreen:
	def __init__(self, screen, webdriver, curses_util, jsinjector):
		self.version=0.1
		self.screen = screen
		self.driver = webdriver
		
		self.curses_util = curses_util
		self.jsinjector = jsinjector
		
		self.commands = HTMLCommands(self.driver, self.jsinjector)
		
		
	def show(self):
		showscreen = True
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "HTML Tools")
			self.screen.addstr(4, 5, "1) Show hidden form elements") # good demo url for this.... https://www.wufoo.com/html5/types/11-hidden.html
			self.screen.addstr(5, 5, "2) Turn password fields into text") 
			self.screen.addstr(6, 5, "3) Turn css visibility on for all HTML elements") 


			
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
				
			if c == ord('1'):
				self.curses_util.close_screen()
				self.commands.show_hidden_form_elements()
				
			if c == ord('2'):
				self.curses_util.close_screen()
				self.commands.show_password_fields_as_text()
				
			if c == ord('3'):
				self.curses_util.close_screen()
				self.commands.see_all_html_elements()
								
		return
		
	
		
	
