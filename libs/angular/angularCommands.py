from selenium.common.exceptions import WebDriverException
from libs.angular.angularCustomJavascript import *
import selenium.webdriver.support.ui as ui
import time

class AngularCommands:
	def __init__(self, webdriver):
		self.version = 0.1
		self.driver = webdriver
		#self.reload_with_debug_info()
		self.install_custom_javascript_functions()
	
	def reload_with_debug_info(self):
		self.driver.execute_script('angular.reloadWithDebugInfo()')
		newurl = self.driver.current_url
		print newurl
		
	def show_app_name(self):
		self.run_javascript('wn_showAngularAppName()')
		
	def show_deps(self):
		self.run_javascript('wn_showAngularDeps()')		
		
	def show_main_classes(self):
		self.run_javascript('wn_showAngularMainClasses()')
	
	def show_all_classes(self):
		self.run_javascript('wn_showAngularAllClasses()')
		
	def show_routes(self):
		self.run_javascript('wn_showAngularRoutes()')
	
	def run_javascript(self, javascript_function):
		self.execute_javascript(javascript_function)
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
		
	def show_ngResource_tests(self):
		# ngResource classes generally communicate with api endpoints... run with proxy to capture api calls.
		print "Testing classes, please wait..."
		print ''
		javascript = """
			wn_testNgResourceClasses();
			"""
		self.driver.execute_script(javascript)
		time.sleep(10)
		result = self.execute_javascript("console.log('all done');")
		print result;
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
		
		
	def execute_javascript(self, javascript):
		try:
			amended_javascript="""window.webnuke = function(){"""+javascript+""";}; webnuke(); return window.console.flushOutput() """
			result = self.driver.execute_script(amended_javascript)
			if result is not None:
				for result_line in result:
					print result_line
		except WebDriverException:
			print "ERROR with webdriver"
			print javascript
			print ''
			raise
		except:
			raise
			
		print ''
		
	def install_custom_javascript_functions(self):		
		try:
			javascript = AngularCustomJavascript().getJavascriptToInjectAsString()
			self.driver.execute_script(javascript)
		except:
			raise
