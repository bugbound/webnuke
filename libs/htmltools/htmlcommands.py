from selenium.common.exceptions import WebDriverException

class HTMLCommands:
	def __init__(self, webdriver, jsinjector):
		self.version = 0.1
		self.driver = webdriver
		self.jsinjector = jsinjector
		
	def show_hidden_form_elements(self):
		self.execute_javascript('wn_showHiddenFormElements()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")

	def show_password_fields_as_text(self):
		self.execute_javascript('wn_showPasswordFieldsAsText()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")		

	def see_all_html_elements(self):
		self.execute_javascript('wn_showAllHTMLElements()')
		print ''
		print ''
		raw_input("Press ENTER to return to menu.")		
		
	def execute_javascript(self, javascript):
		try:
			self.install_custom_javascript_functions()
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
