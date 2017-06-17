class JavascriptCommands:
	def __init__(self, webdriver, jsinjector):
		self.version = 0.1
		self.driver = webdriver
		self.jsinjector = jsinjector
		
	def search_for_urls(self):
		self.execute_javascript('wn_findStringsWithUrls()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")

	def search_for_document_javascript_methods(self):
		self.execute_javascript('wn_findMethodsOfThis()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")
		
	def execute_javascript(self, javascript):
		self.install_custom_javascript_functions()
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
		javascript = """window.console = {log: function(data){this.output.push(data);}, warn: function(data){this.output.push("WARN: "+data);}, error: function(data){this.output.push("ERROR: "+data);}, output: [], flushOutput: function(){var rtndata = this.output; this.output=[]; return rtndata;}};			
						
						"""+self.jsinjector.get_js_block()
		try:
			self.driver.execute_script(javascript)
		except:
			raise
	
		
	
