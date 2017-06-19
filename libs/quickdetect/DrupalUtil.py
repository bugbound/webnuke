import time		

class DrupalUtil:
	def __init__(self, webdriver):
		self.version = 0.1
		self.beta = True
		self.webdriver = webdriver
		
	def isDrupal(self):
		try:
			result = self.webdriver.execute_script('return this.Drupal')
			if result == None:
				return False
			return True
		except:
			pass
		return False
	
	def getVersionString(self):
		generator = self.getMetaGenerator()
		if generator.startswith('Drupal'):
			return generator
		return None
		
	def getMetaGenerator(self):
		generator = ''
		
		found_generator = False
		try:
			result = self.webdriver.find_element_by_xpath("//meta[@name='Generator']")
			generator = result.get_attribute("content")
			found_generator = True
		except:
			pass
			
		if found_generator == False:
			try:
				result = self.webdriver.find_element_by_xpath("//meta[@name='generator']")
				generator = result.get_attribute("content")
				found_generator = True
			except:
				pass
		
		if found_generator:
			return generator
		return None
		

