import curses
from libs.spider.spidercommands import *

class SpiderScreen:
	def __init__(self, screen, curses_util, current_url, proxy_host, proxy_port):
		self.version=0.1
		self.screen = screen
		self.curses_util = curses_util
		self.current_url = current_url
		self.proxy_host = proxy_host
		self.proxy_port = proxy_port
		
		self.commands = SpiderCommands(proxy_host, proxy_port)
		
	def show(self):
		showscreen = True
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "Spider Tools")
			
			self.screen.addstr(4, 4, "1) Set Url to spider")
			self.screen.addstr(5, 24, "URL: "+self.current_url)
			self.screen.addstr(7, 4, "2) Run Kitchensinks in foreground")
				
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
				
			if c == ord('1'):
				self.current_url = self.curses_util.get_param("Enter the url to spider")
				if self.current_url[-1] is not '/':
					self.current_url = self.current_url+'/'
			
			if c == ord('2'):
				self.curses_util.close_screen()
				self.commands.run_kitchensinks_in_foreground(self.current_url)
			
				
				
		return
		
	
		
	
