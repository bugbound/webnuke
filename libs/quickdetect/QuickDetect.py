import curses
from libs.quickdetect.AngularUtil import *
from libs.quickdetect.WordPressUtil import *
from libs.quickdetect.DrupalUtil import *
from libs.quickdetect.JQueryUtil import *
from libs.quickdetect.AWSS3Util import *

class QuickDetect:
	def __init__(self, screen, webdriver, curses_util, logger):
		self.version = 0.1
		self.screen = screen
		self.driver = webdriver
		self.current_url = self.driver.current_url
		self.curses_util = curses_util
		self.logger = logger
		
	def run(self):
		angular_util = AngularUtilV2(self.driver, self.current_url)
		isAngular = angular_util.isAngularApp()
		angular_version = 0
		if isAngular:
			angular_version = angular_util.getVersionString()
		
		wordpress_util = WordPressUtil(self.driver)
		isWordpress = wordpress_util.isWordPress()
		wordpress_version = 0
		if isWordpress:
			wordpress_version = wordpress_util.getVersionString()
			
		
		drupal_util = DrupalUtil(self.driver)
		isDrupal = drupal_util.isDrupal()
		drupal_version = 0
		if isDrupal:
			drupal_version = drupal_util.getVersionString()
		
		jquery_util = JQueryUtil(self.driver)
		isJQuery = jquery_util.isJQuery()
		jquery_version =0
		if isJQuery:
			jquery_version = jquery_util.getVersionString()
			
		dojo_util = DojoUtil(self.driver)
		is_dojo = dojo_util.is_dojo()
		dojo_version = 0
		if is_dojo:
			dojo_version = dojo_util.getVersionString()
		
		s3util = AWSS3Util(self.driver, self.current_url, self.logger)
		isS3 = s3util.hasS3Buckets()
		S3 = ''
		if isS3:
			S3 = s3util.getUrlString()
			
			
		showscreen = True
		
		while showscreen:
			self.curses_util.show_header()
			self.screen.addstr(2, 2, "Technologies:")
			
			
			current_line = 4
			
			if isAngular:
				message = "AngularJS Application Discovered"
				if angular_version is not None:
					message += " ("+angular_version+")"
				self.screen.addstr(current_line, 4, message, curses.color_pair(2))
				current_line += 1
				
			if isWordpress:
				message = "WordPress CMS Discovered"
				if wordpress_version is not None:
					message += " ("+wordpress_version+")"
				self.screen.addstr(current_line, 4, message, curses.color_pair(2))
				current_line += 1
				
			if isDrupal:
				message = "Drupal CMS Discovered"
				if drupal_version is not None:
					message += " ("+drupal_version+")"
					
				self.screen.addstr(current_line, 4, message, curses.color_pair(2))
				current_line += 1
				
			if isJQuery:
				message = "JQuery Discovered"
				if jquery_version is not None:
					message += " ("+jquery_version+")"
				self.screen.addstr(current_line, 4, message, curses.color_pair(2))
				current_line += 1
			
			if is_dojo:
				message = "Dojo Discovered"
				if dojo_version is not None:
					message += " ("+dojo_version+")"
				self.screen.addstr(current_line, 4, message, curses.color_pair(2))
				current_line += 1
			
			if isS3:
				message = "AWS S3 Bucket Detected"
				if S3 is not None:
					message += " ("+S3+")"
				self.screen.addstr(current_line, 4, message, curses.color_pair(2))
				current_line += 1
				
			self.screen.addstr(22, 28, "PRESS M FOR MAIN MENU")
			self.screen.refresh()
			
			c = self.screen.getch()
			if c == ord('M') or c == ord('m'):
				showscreen=False



class DojoUtil:
	def __init__(self, webdriver):
		self.version = 0.1
		self.beta = True
		self.webdriver = webdriver
		
	def is_dojo(self):
		try:
			result = self.webdriver.execute_script('return this.dojo.version')
			if result == None:
				return False
			return True
		except:
			pass
		return False
		
	def getVersionString(self):
		try:
			result = self.webdriver.execute_script('return this.dojo.version')
			return '%d.%d.%d.%d'%(result['major'], result['minor'], result['patch'], result['revision'])
		except:
			pass
		return None
