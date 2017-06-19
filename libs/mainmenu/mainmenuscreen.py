class MainMenuScreen:
	def __init__(self, screen, curses):
		self.screen = screen
		self.curses = curses
		
	def drawscreen(self):
		self.screen.addstr(2, 2,  "Please enter a command")
		self.screen.addstr(4, 4,  "goto <url>   - opens url")
		self.screen.addstr(5, 4,  "quickdetect  - detect technologies in use on url...")
		self.screen.addstr(6, 4,  "jsconsole    - opens a console bound to a browser javascript console...")
		self.screen.addstr(7 , 4, "html         - HTML tools menu...")
		self.screen.addstr(8 , 4, "javascript   - Javascript tools menu...")
		self.screen.addstr(9 , 4, "angularjs    - AngularJS tools menu...")
		self.screen.addstr(10, 4, "spider       - Spider tools menu...")
		self.screen.addstr(11, 4, "followme     - Activates followme mode...")
		self.screen.addstr(14, 4, "debug        - toggle debug on/off")
		self.screen.addstr(15, 4, "proxy        - set proxy settings...")
		self.screen.addstr(16, 4, "!sh          - escape to unix land...")
		self.screen.addstr(18, 4, "quit         - Exit webnuke")
		# pic from http://ascii.co.uk/art/rockets
		greencolour = self.curses.color_pair(2)
		self.screen.addstr(8, 45, "                 *    ", greencolour)
		self.screen.addstr(9, 45, "     +               ", greencolour)
		self.screen.addstr(10,45, "        *          +   '--'  *", greencolour)
		self.screen.addstr(11,45, "            +   /\\", greencolour)
		self.screen.addstr(12,45, "+             .'  '.   *", greencolour)
		self.screen.addstr(13,45, "      *      /======\\      +", greencolour)
		self.screen.addstr(14,45, "            ;:.      ;", greencolour)
		self.screen.addstr(15,45, "            |:.      |", greencolour)
		self.screen.addstr(16,45, "            |:.      |", greencolour)
		self.screen.addstr(17,45, "  +         |:.      |          *", greencolour)
		self.screen.addstr(18,45, "            ;:.      ;", greencolour)
		self.screen.addstr(19,45, "          .' \\:.    / `.", greencolour)
		self.screen.addstr(20,45, "         / .-'':._.'`-. \\", greencolour)
		self.screen.addstr(21,45, "         |/    /||\\    \\|", greencolour)
