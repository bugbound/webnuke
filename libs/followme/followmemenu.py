from libs.utils.WebDriverUtil import *
import thread
import time

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
		
		
		#self.commands = HTMLCommands(self.driver, self.jsinjector)
		
		
	def run(self):
		showscreen = True
		
		newdriver = self.create_browser_instance()
		thread.start_new_thread(self.linkbrowsers, (self.driver, newdriver, self.logger))
		
		
		while showscreen:
			self.screen = self.curses_util.get_screen()
			self.screen.addstr(2, 2, "Followme activated!")
			
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False
												
		return
		
	def create_browser_instance(self):
		self.webdriver_util = WebDriverUtil()
		self.webdriver_util.setDebug(self.debug)
		if self.proxy_host is not '' and int(self.proxy_port) is not 0:
			return self.webdriver_util.getDriverWithProxySupport(self.proxy_host, int(self.proxy_port))
		else:
			return self.webdriver_util.getDriver(self.logger)	
		
	def linkbrowsers(self, maindriver, followmedriver, logger):
		while(True):
			try:
				main_url = maindriver.current_url
				if followmedriver.current_url != main_url:
					followmedriver.get(main_url)
					current_url = followmedriver.current_url
					logger.log("Followme on %s"%current_url)
				#time.sleep(5)
			except:
				pass
			finally:
				time.sleep(0.5)
				
