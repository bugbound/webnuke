import curses

from os import system

class CursesUtil:
	def __init__(self):
		self.version = 0.1
		self.current_url = "NONE"
		self.x = 0;
		self.y = 0;
	
	def get_screen(self):
		self.screen = curses.initscr()
		
		curses.start_color()
		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
		curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
		
		if self.x == 0:
			starty, startx = self.screen.getmaxyx()
			self.x = startx
			self.y = starty
			
		resize = curses.is_term_resized(self.y, self.x)
		
		# Action in loop if resize is True:
		if resize is True:
			y, x = self.screen.getmaxyx()
			self.screen.clear()
			curses.resizeterm(self.y, self.x)
			self.screen.refresh()
		
		
		self.show_header()
		
		return self.screen

	def close_screen(self):
		curses.endwin()
		
	def show_header(self):
		self.screen.clear()
		self.screen.border(0)
		self.screen.addstr(0, 28, " WEBNUKE V1.5 - BETA ", curses.color_pair(2))
		
		
	def get_param(self, prompt_string):
		self.screen.clear()
		self.screen.border(0)
		self.screen.addstr(2, 2, prompt_string)
		self.screen.refresh()
		input = self.screen.getstr(10, 10, 60)
		return input
		 
	def execute_cmd(self, cmd_string):
		self.close_screen()
		system("clear")
		a = system(cmd_string)
		print ""
		if a == 0:
			print "Command executed correctly"
		else:
			print "Command terminated with error"
		raw_input("Press enter")
		print ""
