	#import IPython
		#IPython.embed()
	
	
class OpCenter:
	def __init__(self):
		self.version = 0.1
		self.beta = True
		self.debug = False
		self.scope_urls = []
		self.attack_manager = AttackManager()
		
	def setDebug(self, newValue):
		self.debug = newValue
		
	def addUrl(self, url):
		if url not in self.scope_urls:
			self.scope_urls.append(url)
		
	def activate(self):
		print "OpCenter Activated"
		self.attack_manager.setDebug(self.debug)
		self.attack_manager.startAttack(self.scope_urls)
		
		print "OpCenter Deactivated"
			
from pyvirtualdisplay import Display
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time 

from libs.AngularUtil import *
			
class AttackManager:
	def __init__(self):
		self.version = 0.1
		self.beta = True
		self.debug = False
		self.found_objects=[]
		self.found_controllers=[]
		self.object_props = []
		
	def setDebug(self, newValue):
		self.debug = newValue
		
	def startAttack(self, scope_urls):
		webdriver_util = WebDriverUtil()
		webdriver_util.setDebug(self.debug)
		all_components = []
		for url in scope_urls:
			print "ATTACKING %s" % url
				
			angular_util = AngularUtilV2(webdriver_util.getDriver(), url)
			
			if angular_util.isAngularApp():
				print "Angular Application Detected"
				
				app_name = angular_util.get_application_name()
				print "Application Name: "+app_name
				print ''
				
#				components = angular_util.get_components_from_dep_name(app_name)
#				print app_name+" components:"
#				for comp in components:
#					
#					if comp['name'] not in all_components:
#						all_components.append(comp['name'])
#					
#					print '\t%s (%s)' %(comp['name'], comp['angular_type'])
#					
#					urls = []
#					for line in comp['sourcecode'].split():
#						if "'/" in line or '"/' in line:
#							if line not in urls:
#								urls.append(line)
#								print "\t\t"+line	
#				print ''
				
				dep_list=[]
				urls = []
				bah = angular_util.extract_dependencies(app_name, [])
				for dep_record in bah:
					print "%s [%s]" %(dep_record['name'], ','.join(dep_record['dependencies']))
					dep_list.append(dep_record['name'])
					
				

					components = angular_util.get_components_from_dep_name(dep_record['name'])
					for comp in components:
						if comp['name'] not in all_components:
							all_components.append(comp)
						
						
						for line in comp['sourcecode'].split():
							if "'/" in line or '"/' in line or 'http://' in line or 'https://' in line or 'ftp://' in line:
								if line not in urls:
									urls.append(line)
									print "\t\t"+line
#						
#					print ''
#				print ''
#				
#				

#				# try extract data from controller
#				for comp in all_components:
#					more_components = angular_util.get_components_from_controller(comp)					
#					for more_comp in more_components:
#						if more_comp not in all_components:
#							all_components.append(more_comp)


				# if not controller then get from injector
				#for comp in all_components:
				#	props = angular_util.get_components_from_component_name(comp)
				#	for more_comp in more_components:
				#		if more_comp['name'] not in all_components:
				#			all_components.append(more_comp['name'])


#				for comp in all_components:
#					props = angular_util.get_components_from_component_name(comp)
#					for prop in props:
#						if prop['type'] == 'object':
#							if prop['name'] not in all_components:
#								all_components.append(prop['name'])
					
				print "ALL COMPONENTS:"
				for comp in all_components:
					print comp['name']
					for line in comp['sourcecode'].split():
						if "'/" in line or '"/' in line or 'http://' in line or 'https://' in line or 'ftp://' in line:
								print "\t\t"+line
#					props = angular_util.get_components_from_component_name(comp)
#					for prop in props:
#						print "\t %s (%s) = %s" %(prop['name'], prop['type'])
#					print ''

				print ''
												
				
			else:
				print "not an angular app"
			
			#self.extractUrlsFromJavascript(url)
		webdriver_util.close_driver();
			
	def extractUrlsFromJavascript(self, url):
		profile = webdriver.FirefoxProfile()
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.http", "10.0.0.196")
		profile.set_preference("network.proxy.http_port", 8080)
		profile.set_preference("network.proxy.https", "10.0.0.196")
		profile.set_preference("network.proxy.https_port", 8080)
		profile.set_preference("network.proxy.ssl", "10.0.0.196")
		profile.set_preference("network.proxy.ssl_port", 8080)
		profile.update_preferences()
		
		
		if self.debug == False:
			self.display = Display(visible=0, size=(1920, 1080))
			self.display.start()
		#self.driver = webdriver.Firefox(firefox_profile=profile)
		self.driver = webdriver.Firefox()
		self.wait = ui.WebDriverWait(self.driver, 10) # timeout after 10 seconds
		print "loading url "+url
		self.driver.get(url)
		time.sleep(5)
		print "ENDED UP ON "+self.driver.current_url
		#self.driver.execute_script('alert("woop")')
		#print "This: "
		#print self.getJSVar('this.window')
		#print "Drupal: "
		#print self.getJSVar('this.Drupal')
		angular = AngularUtil()
		
		isapp = angular.isAngularApp(self.driver)
		if isapp:
			print "Found Angular Application"
			app_name = angular.getAngularAppName(self.driver)
			print "\tApplication Name: "+app_name
			components = angular.getApplicationParts(self.driver)
			
			for component in components:
				if component not in self.found_objects:
					self.found_objects.append(component)
			
			#self.driver.execute_script('angular.reloadWithDebugInfo()')
			#time.sleep(10)
			
			found_routes = angular.detect_routes_from_ui_router(self.driver)
			# extract controllers from routes...
			for route in found_routes:
				if route['controller'] not in self.found_controllers and route['controller'] != None:
					self.found_controllers.append(route['controller'])
						
			for found_controller in self.found_controllers:
				props = angular.get_controller_info(self.driver, found_controller)
				if len(props) > 0:
					self.object_props.append({'name': found_controller, 'props': props})
					
				#extract objects....
				for myobject in props:
					if myobject['type']=='object':
						if myobject['name'] not in self.found_objects:
							self.found_objects.append(myobject['name'] )
				
			for found_object in self.found_objects:
				if found_object.startswith("$") == False:
					props = angular.get_application_classitem(self.driver, found_object)
					if len(props) > 0:
						self.object_props.append({'name': found_object, 'props': props})
					
					
			# print out found objects...
			print "+++FOUND OBJECTS+++"
			
			for prop in self.object_props:
				name = prop['name']
				values = prop['props']
				print "Classname: "+name
				for class_prop in values:
					print "\t%s (%s) = %s" %(class_prop['name'], class_prop['type'], str(class_prop['value']))
				print "-"*79
				print ''
			print ''
			
		if self.debug == False:
			self.driver.quit()
			self.display.stop()
			
	def getJSVar(self, name):
		# ignore any errors
		try:
			result = self.driver.execute_script('return '+name)
			return result
		except:
			print "ERROR getting jsvar "+name
			raise
		
		return None
		

			
