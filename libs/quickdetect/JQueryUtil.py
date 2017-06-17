class JQueryUtil:
	def __init__(self, webdriver):
		self.version = 0.1
		self.beta = True
		self.webdriver = webdriver
		
	def isJQuery(self):
		try:
			result = self.webdriver.execute_script('return this.$.fn.jquery')
			if result == None:
				return False
			return True
		except:
			pass
		return False
		
	def getVersionString(self):
		try:
			result = self.webdriver.execute_script('return this.$.fn.jquery')
			return result
		except:
			pass
		return None


