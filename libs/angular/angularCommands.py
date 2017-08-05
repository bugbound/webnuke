from selenium.common.exceptions import WebDriverException
from libs.angular.angularCustomJavascript import *
import selenium.webdriver.support.ui as ui
import time

class AngularCommands:
	def __init__(self, webdriver, jsinjector):
		self.version = 0.1
		self.driver = webdriver
		self.jsinjector = jsinjector
		#self.reload_with_debug_info()
	
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
		self.jsinjector.execute_javascript(self.driver, javascript_function)
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
		
	def show_ngResource_tests(self):
		# ngResource classes generally communicate with api endpoints... run with proxy to capture api calls.
		print "Testing classes, please wait..."
		print ''
		self.jsinjector.execute_javascript(self.driver, "wn_testNgResourceClasses();")
		time.sleep(10)
		result = self.jsinjector.execute_javascript(self.driver, "console.log('all done');")
		print result;
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
		
	def show_http_tests(self):
		# ngResource classes generally communicate with api endpoints... run with proxy to capture api calls.
		print "Testing classes using $http, please wait..."
		print ''
		self.jsinjector.execute_javascript(self.driver, "wn_testHTTPClasses();")
		time.sleep(10)
		result = self.jsinjector.execute_javascript(self.driver, "console.log('All done son.');")
		print result;
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")		
		
