class WordPressUtil:
	def __init__(self, webdriver):
		self.version = 0.1
		self.beta = True
		self.webdriver = webdriver
		
	def isWordPress(self):
		try:
			result = self.webdriver.find_element_by_xpath("//meta[@name='generator']")
			generator = self.getVersionString()
			if generator.startswith('WordPress'):
				return True
		except:
			pass
		return False
		
	def getVersionString(self):
		try:
			result = self.webdriver.find_element_by_xpath("//meta[@name='generator']")
			generator = result.get_attribute("content")
			return generator
		except:
			pass
		return None

